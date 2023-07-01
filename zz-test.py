from copy import copy
import d20
from lorem_text_fantasy import lorem as lf
from math import ceil
from openpyxl.styles import Font as openpyxl_font
from openpyxl import load_workbook
from openpyxl import Workbook
import os
import random as random
import rpg_tables as r
import string as string
import sys
import uuid
import yaml

# use faster C code for yaml if available, otherwise pure python code
try:
    from yaml import CSafeLoader as SafeLoader

except ImportError:
    from yaml import SafeLoader

# settings file
with open("fantasy_book_settings.yaml") as f:     
    config = yaml.load(f, Loader=SafeLoader)

    ################ GLOBALS #####################

# names

global author_title_table, epithets_tables

# names of male and female
global complete_table_male_names, name_tables_male
global complete_table_female_names, name_tables_female

# book titles

global titles_adjective_1_list, titles_communication, titles_conjunction_about, titles_conjunction_by, titles_fixed
global titles_history_of, titles_negative_subject
global titles_noun_1_list, titles_noun_2_list, titles_person_1, titles_person_2
global titles_places_cities, titles_places_nations, titles_religious_starter
global titles_study_in_list, titles_study_of_list, titles_study_on_list, titles_study_verbing, titles_the_1 
global titles_template_list_general, titles_template_list_history, titles_template_list_occult, titles_template_list_theology 

vocab_dictionary = {}
surnames_tables = {}
name_tables_male = {}
name_tables_female = {}

############# below here tweaked.

gls = config['name_SQL_tables']
g={}

for key,table in gls.items():
    g[key] = r.RPG_table(table)
    

print (g['titles_the_1'])

# complete_table_female_names.description : "Female Names Amalgamated"
# complete_table_male_names.description = "Male Names Amalgamated"

############# above here tweaked.