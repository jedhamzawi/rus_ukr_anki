import os
from subscripts import tr_rus_ukr
from subscripts import str_rus_ukr
from subscripts import csv_rus_ukr
from subscripts import anki_rus_ukr

def main(file_path, apy_cfg_file="apy.json", no_sync=False):
    # translate the russian words
    print(f"Translating file '{file_path}'...")
    translate_file = tr_rus_ukr.translate(file_path)
    # add stress to the translated ukrainian words
    print(f"Adding stress marks to file '{translate_file}'...")
    stress_file = str_rus_ukr.stress(translate_file)
    # join the files to a CSV file
    print(f"Creating CSV file...")
    csv_file = csv_rus_ukr.make_csv(file_path, stress_file)
    # automatic Anki import and sync
    print(f"Importing to Anki and syncing with Anki web...")
    anki_rus_ukr.import_and_sync(csv_file, apy_cfg_file, no_sync)


if __name__ == '__main__':
    import argparse

    # create arg parser
    parser = argparse.ArgumentParser(
        prog='rus_ukr.py',
        description='Translates a newline-delimited list of Russian words \
          to Ukrainian using the DeepL API, adds stress marks, then \
          exports to an Anki pkg')
    # add file path arg
    parser.add_argument('file_path')
    parser.add_argument('-c', '--apy_cfg_file')
    parser.add_argument('-n', '--no-sync', action='store_true')
    args = parser.parse_args()
    if args.apy_cfg_file is not None and args.no_sync is not None:
        main(args.file_path, args.apy_cfg_file, args.no_sync)
    elif args.apy_cfg_file is not None:
        main(args.file_path, args.apy_cfg_file)
    elif args.no_sync is not None:
        main(args.file_path, no_sync=args.no_sync)
    else:
        main(args.file_path)
