import os
import sys
import json
from subscripts import tr_rus_ukr
from subscripts import str_rus_ukr
from subscripts import csv_rus_ukr
from subscripts import anki_rus_ukr

def main(args):
    # get our args
    file_path = args.file_path
    rua_cfg_file = args.rua_cfg_file
    if args.rua_cfg_file is None:
        rua_cfg_file = "rua.json"
    no_sync = args.no_sync
    if args.no_sync is None:
        no_sync = False
    rua_cfg: dict[str, Any]
    if not os.path.exists(rua_cfg_file):
        # return an error if the config file doesn't exist
        print("Error: rua config file not found!", file=sys.stderr)
        exit(1)
    else:
        with open(rua_cfg_file, encoding='utf8') as cfg_file:
            # load the config file
            rua_cfg = json.load(cfg_file)
    # translate the russian words
    print(f"Translating file '{file_path}'...")
    translate_file = tr_rus_ukr.translate(file_path, rua_cfg['deepl_api'])
    # add stress to the translated ukrainian words
    print(f"Adding stress marks to file '{translate_file}'...")
    stress_file = str_rus_ukr.stress(translate_file)
    # join the files to a CSV file
    print(f"Creating CSV file...")
    csv_file = csv_rus_ukr.make_csv(file_path, stress_file)
    # automatic Anki import and sync
    print(f"Importing to Anki and syncing with Anki web...")
    anki_rus_ukr.import_and_sync(csv_file, rua_cfg['apy'], no_sync)


if __name__ == '__main__':
    import argparse

    # create arg parser
    parser = argparse.ArgumentParser(
        prog='rus_ukr.py',
        description='Translates a newline-delimited list of Russian words \
          to Ukrainian using the DeepL API, adds stress marks, then \
          imports to the Anki collection and optionally syncs to Anki web')
    # add file path arg
    parser.add_argument('file_path')
    parser.add_argument('-c', '--rua_cfg_file')
    parser.add_argument('-n', '--no-sync', action='store_true')
    args = parser.parse_args()
    main(args)

