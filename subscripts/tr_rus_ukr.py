import os
import deepl

out_dir = "translated"
auth_key = "<API_KEY>"

def translate(file_path) -> str:
    translator = deepl.Translator(auth_key)

    # create translated subdirectory if it doesn't exist
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    # create the translated output file path
    filename = os.path.basename(file_path)
    out_path = os.path.join(out_dir, filename)

    # open files
    with open(file_path, 'r') as input_file, open(out_path, 'w', newline='') as output_file:
        for row in input_file:
            # remove whitespace from the row
            rus = row.strip()
            # translate the text
            ukr = translator.translate_text(rus, source_lang="RU", target_lang="UK")
            # write the translated text
            output_file.write(str(ukr) + "\n")
    # return the output path
    return out_path
    

if __name__ == '__main__':
    import argparse

    # create the argument parser to parse the file path
    parser = argparse.ArgumentParser(
        prog='tr-rus-ukr.py',
        description='Translates a newline-delimited list of Russian words \
          to Ukrainian using the DeepL API')
    # add file path arg
    parser.add_argument('file_path')
    args = parser.parse_args()
    translate(args.file_path)
