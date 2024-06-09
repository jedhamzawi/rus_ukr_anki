import os
import csv
import genanki

out_dir = "anki"
# random model ID for Anki
anki_model_id = 2126304982
anki_deck_id = 1561550783
anki_model = genanki.Model(
  anki_model_id,
  'rus-ukr',
  fields=[
    {'name': 'rus'},
    {'name': 'ukr'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{rus}}',
      'afmt': '{{FrontSide}}<hr id="ukr">{{ukr}}',
    },
  ])

def make_anki_pkg(file_path) -> str:
    import argparse

    # create translated subdirectory if it doesn't exist
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    # create the output anki pkg file path
    filename = os.path.basename(file_path).split(".")[0] + ".apkg"
    out_path = os.path.join(out_dir, filename)

    anki_deck = genanki.Deck(anki_deck_id, 'rus-ukr')
    # open input CSV file
    with open(file_path, 'r') as input_file:
        # create CSV reader
        reader = csv.DictReader(input_file)
        for row in reader:
            rus = row['rus']
            ukr = row['ukr']
            # create a note out of the rus/ukr values
            anki_note = genanki.Note(
                model=anki_model,
                fields=[rus, ukr])
            # add it to our deck
            anki_deck.add_note(anki_note)
    # package the deck into a file
    genanki.Package(anki_deck).write_to_file(out_path)
    # return the out path
    return out_path


if __name__ == '__main__':
    # create the argument parser to parse the file path
    parser = argparse.ArgumentParser(
        prog='anki_rus_ukr.py',
        description='Converts a CSV of Russian/Ukrainian words to \
            an Anki deck')
    # add file path arg
    parser.add_argument('file_path')
    args = parser.parse_args()
    make_anki_pkg(args.file_path)
