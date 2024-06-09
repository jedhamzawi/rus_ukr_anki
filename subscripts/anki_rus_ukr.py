import os
import csv
import sys
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

def import_and_sync(csv_path, apy_cfg={}, no_sync=False):
    # overwrite with our own local cfg if we have it
    if not apy_cfg['base_path'] is None:
        cfg['base_path'] = apy_cfg['base_path']
    if not apy_cfg['profile_name'] is None:
        cfg['profile_name'] = apy_cfg['profile_name']
    anki = Anki(**cfg)
    # import the CSV file to Anki
    import_csv(csv_path, cfg, anki)
    # sync to Anki web if we're set to
    if not no_sync:
        anki.sync()


def parse_apy_cfg(apy_cfg_file):
    if not os.path.exists(apy_cfg_file):
        # return an error if the config file doesn't exist
        print("Error: rua config file not found!", file=sys.stderr)
        exit(1)
    else:
        with open(apy_cfg_file, encoding='utf8') as cfg_file:
            # load the config file
            return json.load(cfg_file)


if __name__ == '__main__':
    import argparse
    # create the argument parser and parse args
    parser = argparse.ArgumentParser(
        prog='anki_rus_ukr.py',
        description='Imports an Anki pkg to the collection \
            and then synchronizes')
    parser.add_argument('csv_path')
    parser.add_argument('-c', '--apy_cfg_file')
    parser.add_argument('-n', '--no-sync', action='store_true')
    # parse args
    args = parser.parse_args()
    # parse the apy cfg
    apy_cfg: dict[str, Any]
    if args.apy_cfg_file is not None:
        apy_cfg = parse_apy_cfg(args.apy_cfg_file)
    if args.no_sync is not None:
        import_and_sync(args.csv_path, apy_cfg, args.no_sync)
    else:
        import_and_sync(args.csv_path, apy_cfg)

