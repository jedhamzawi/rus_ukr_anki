import os
from subscripts import tr_rus_ukr
from subscripts import str_rus_ukr
from subscripts import csv_rus_ukr
from subscripts import anki_rus_ukr

def main(file_path):
    # translate the russian words
    print(f"Translating file '{file_path}'...")
    translate_file = tr_rus_ukr.translate(file_path)
    # add stress to the translated ukrainian words
    print(f"Adding stress marks to file '{translate_file}'...")
    stress_file = str_rus_ukr.stress(translate_file)
    # join the files to a CSV file
    print(f"Create CSV file...")
    csv_file = csv_rus_ukr.make_csv(file_path, stress_file)
    # convert the CSV file to an ANKI PKG
    print(f"Converting to Anki pkg...")
    anki_file = anki_rus_ukr.make_anki_pkg(csv_file)
    print(f"Successfully created Anki pkg '{anki_file}'")


if __name__ == '__main__':
    import argparse

    # create arg parser
    parser = argparse.ArgumentParser(
        prog='tr-rus-ukr.py',
        description='Translates a newline-delimited list of Russian words \
          to Ukrainian using the DeepL API, adds stress marks, then \
          exports to an Anki pkg')
    # add file path arg
    parser.add_argument('file_path')
    args = parser.parse_args()
    main(args.file_path)
