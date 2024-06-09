# rus_ukr_anki

A quick and diry Python script that translates a list of newline-delimited
Russian words/phrases to Ukrainian using the [DeepL API](https://developers.deepl.com/docs),
adds stress/accent marks to the translations using the excellent
[ukrainian-word-stress](https://github.com/lang-uk/ukrainian-word-stress) library,
then imports the translations to the user's Anki collection and optionally
syncs them with Anki web using [apy(anki)](https://github.com/lervag/apy).


## Configuration

The configuration file `rua.json` is composed of the relevant part of the
apyanki config (see <https://github.com/lervag/apy?tab=readme-ov-file#configuration>)
as well as an API key for DeepL. The 'Free' tier of DeepL provides 500,000 characters
to translate a month, which should be more than enough for personal use.

### Example Config File

The repo contains an example config file called `rua-example.json`:

```JSON
{
  "apy": {
    "base_path": "/home/your_name/.local/share/Anki2/",
    "profile_name": "MyAnkiProfile",
    "presets": {
      "default": { "model": "Custom", "tags": ["marked"] }
    },
  },
  "deepl_api": "<API_KEY>"
}
```

## Quick Start

### Requirements

The Python version I used was 3.10.14, 3.11 and 3.12 will probably work as well.

`ukrainian-word-stress` uses language models to tell from context where the
stress marks should be placed, so CUDA might be a requirement? I happened to have
an Nvidia GPU and CUDA installed already, so I didn't run into issues. Most of my
lines were single Russian words with no context, so the ML stuff was likely not
very helpful.

There might be a better tool for the job, but I didn't find anything better.
Plus if you want to translate longer phrases, this will serve you quite well.

### Installation

You'll need to download the repo, setup a virtual environment
(using venv, pyenv, or similar), and install the needed requirements:

```
git clone https://github.com/jedhamzawi/rus_ukr_anki
cd rus_ukr_anki
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### Running

From there, you can run the script by running:

```
python3 rus_ukr_anki.py <PATH-TO-RUS-WORDS>
````

The script will create intermediary subdirectories for translated text,
stressed text, and joined CSV files and will not delete them afterward in
case you want them later.


## Considerations

### Ukrainian Word Stress Settings

I've hard-coded `ukrainian-word-stress` to use accented letters instead of
inserting an accent symbol after a letter to indicate stress (e.g. тяжки́й
instead of тяжки\`й). It looks better and with Ukrainian's frequent use of
`'` to indicate softness, it's much less confusing. Apparently Windows doesn't
support viewing these symbols though.
