import os
from ukrainian_word_stress import Stressifier, OnAmbiguity, StressSymbol

out_dir = "stressed"

def stress(file_path) -> str:
    # put all stress marks if the word has more than one stress
    # possibility; I can correct it later
    stressify = Stressifier(
        stress_symbol=StressSymbol.CombiningAcuteAccent,
        on_ambiguity=OnAmbiguity.All)

    # create stressed subdirectory if it doesn't exist
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    # create the translated output file path
    filename = os.path.basename(file_path).split("\.")[0]
    out_path = os.path.join(out_dir, filename)

    # open the input and output files
    with open(file_path, 'r') as input_file, open(out_path, 'w', newline='') as output_file:
        for row in input_file:
            # strip the whitespace from the row
            ukr = row.strip()
            # add the stress
            ukr_stressed = stressify(ukr)
            # right the stressed word to the file
            output_file.write(ukr_stressed + "\n")
    # return the output path
    return out_path

if __name__ == '__main__':
    import argparse

    # create arg parser
    parser = argparse.ArgumentParser(
        prog='str_rus_ukr.py',
        description='Adds stress to a newline delimited list of \
          Ukrainian words')
    parser.add_argument('file_path')
    args = parser.parse_args()
    stress(args.file_path)
