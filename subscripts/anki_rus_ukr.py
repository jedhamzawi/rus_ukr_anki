import os
import csv
import json
from apyanki.config import cfg
from apyanki.anki import Anki
from apyanki.note import NoteData

def import_csv(csv_path, cfg, anki):
    # open input CSV file
    with open(csv_path, 'r') as input_file:
        # create CSV reader
        reader = csv.DictReader(input_file)
        for row in reader:
            rus = row['rus']
            ukr = row['ukr']
            fields= {
                'rus': rus,
                'ukr': ukr,
            }
            # create the note
            anki_note = NoteData(
                model='rus-ukr',
                tags='rus-ukr mission',
                fields=fields,
                markdown=False,
                deck='rus-ukr'
            )
            # add the note to the collection
            anki_note.add_to_collection(anki)

def import_and_sync(csv_path, apy_cfg_file = "apy.json"):
    # overwrite with our own local cfg if we have one
    if os.path.exists(apy_cfg_file):
        with open(apy_cfg_file, encoding="utf8") as f:
            new_cfg = json.load(f)
            if not new_cfg['base_path'] is None:
                cfg['base_path'] = new_cfg['base_path']
            if not new_cfg['profile_name'] is None:
                cfg['profile_name'] = new_cfg['profile_name']
    anki = Anki(**cfg)
    # import the CSV file to Anki
    import_csv(csv_path, cfg, anki)
    # sync to Anki web
    anki.sync()


if __name__ == '__main__':
    import argparse
    # create the argument parser to parse the file path
    parser = argparse.ArgumentParser(
        prog='anki_rus_ukr.py',
        description='Imports an Anki pkg to the collection \
            and then synchronizes')
    # add file path arg
    parser.add_argument('csv_path')
    parser.add_argument('-c', '--apy_cfg_file')
    args = parser.parse_args()
    if not args.apy_cfg_file is None:
        import_and_sync(args.csv_path, args.apy_cfg_file)
    else:        
        import_and_sync(args.csv_path)
