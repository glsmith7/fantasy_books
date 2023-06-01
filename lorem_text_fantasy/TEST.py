"""Main module."""

import random
import os

global WORDS, ROOT_DIR, THIS_FOLDER

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
THIS_FOLDER = os.path.join(ROOT_DIR, 'lorem_text_fantasy')

WORDS = ()

def import_language():
    dictionary_languages = {
        "Latin" : "latin.txt",
        # "Greek" : "greek.txt",
        # "Akkadian": "akkadian.txt",
        # "Dwarven" : "runes.txt",
        # "Elvish" : "sindarin.txt",
    }
    vocab_dictionary = {}
    for language,file in dictionary_languages.items():
        TARGET_LANGUAGE_FILE = os.path.join(THIS_FOLDER, file)
        the_words_imported = []
        with open(TARGET_LANGUAGE_FILE,encoding = 'utf8', mode='r') as f:
            for line in f.readlines():
                the_words_imported.append(line.strip())
            vocab_dictionary[language] = the_words_imported

    return vocab_dictionary

WORDS = import_language()
print (WORDS)


