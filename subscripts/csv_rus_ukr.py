import os
import csv

out_dir = "csv"

def make_csv(rus_file_path, ukr_file_path) -> str:
    # create csv subdirectory if it doesn't exist
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    # create the translated output file path
    rus_filename = os.path.basename(rus_file_path)
    filename = rus_filename.split(".")[0] + ".csv"
    out_path = os.path.join(out_dir, filename)

    fieldnames = ["rus", "ukr"]

    # open the input and output files
    with open(rus_file_path, 'r') as rus_file, open(ukr_file_path, 'r') as ukr_file, open(out_path, 'w', newline='') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        for (rus_raw, ukr_raw) in zip(rus_file, ukr_file):
            # strip the whitespace from the row
            row = {fieldnames[0]: rus_raw.strip(), fieldnames[1]: ukr_raw.strip()}
            writer.writerow(row)
    # return the output path
    return out_path

if __name__ == '__main__':
    import argparse

    # create arg parser
    parser = argparse.ArgumentParser(
        prog='csv_rus_ukr.py',
        description='Joins a list of Russian and Ukrainian words\
            into a CSV file')
    parser.add_argument('rus_file_path')
    parser.add_argument('ukr_file_path')
    args = parser.parse_args()
    make_csv(args.rus_file_path, args.ukr_file_path)
