"""Main module."""

import random
import os

global WORDS, ROOT_DIR, THIS_FOLDER

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
THIS_FOLDER = os.path.join(ROOT_DIR, 'lorem_text_fantasy')

WORDS = ()

def import_language(lang):
    dictionary_languages = {
        "Latin" : "latin.txt",
        "Greek" : "greek.txt",
        "Akkadian": "akkadian.txt",
        "Ancient" : "akkadian.txt",
        "Runes" : "runes.txt",
        "Dwarven" : "runes.txt",
        "Dwarf" : "runes.txt",
        "Elvish" : "sindarin.txt",
        "Elf" : "sindarin.txt",
        "Sindarin": "sindarin.txt",
    }
    latin_words = []
    TARGET_LANGUAGE_FILE = os.path.join(THIS_FOLDER, 'latin.txt')

    with open(TARGET_LANGUAGE_FILE,encoding = 'utf8', mode='r') as f:
        for line in f.readlines():
            latin_words.append(line.strip())
    f.close()

    return latin_words

WORDS = import_language("Latin")
print (WORDS)
print (len(WORDS))


