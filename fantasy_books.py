import d20 as d20
import random as random
import rpg_tables as rpg
import string as string

global list_of_names_tables_male, list_of_names_tables_female
global name_tables_male, name_tables_len_male, name_table_amalgamated_male 
global name_tables_female, name_tables_len_female, name_table_amalgamated_female
global author_title_tables, epithets_tables
global list_of_words_to_not_capitalize
global complexity_table_list
global adjective_1_list, noun_1_list, noun_2_list, titles_study_of_list, titles_study_in_list, titles_study_on_list, titles_template_list

global CHANCE_OF_BEING_TRANSLATION, ANCIENT_LANGUAGES_WHICH_WOULD_NOT_HAVE_TRANSLATED, CHANCE_OF_EPITHET 

CHANCE_OF_BEING_TRANSLATION = 10 # ten percent chance; can be changed as wished.
CHANCE_OF_EPITHET = 15
ANCIENT_LANGUAGES_WHICH_WOULD_NOT_HAVE_TRANSLATED = 'Ancient'

list_of_words_to_not_capitalize = [
    ("The","the"),
    ("Of","of"),
    ("De","de"),
    ("D'","d'"),

]
list_of_names_tables_male = [
        "_names_arabic_male",
        "_names_anglo_saxon_male", 
        "_names_english_male",
        "_names_famous_male", 
        "_names_french_male", 
        "_names_norse_male", 
        # "_names_saints_male", 
        ]

list_of_names_tables_female = [
        "_names_arabic_female",
        "_names_anglo_saxon_female", 
        "_names_english_female",
        "_names_famous_female", 
        "_names_french_female", 
        "_names_norse_female", 
        # "_names_saints_female", 
        ]

list_of_surnames_tables = [
        ("_names_arabic_surnames"),
        ("_names_anglo_saxon_surnames"), 
        ("_names_english_surnames"),
        ("_names_famous_surnames"), 
        ("_names_french_surnames"), 
        ("_names_norse_surnames_female"),
		("_names_norse_surnames_male"),
        ("_names_roman_surnames"),
        
        ]

complexity_table_list = ["BookComplexityForScope1","BookComplexityForScope2","BookComplexityForScope3","BookComplexityForScope4"]

name_tables_male, name_tables_len_male = {}, {}
name_tables_female, name_tables_len_female = {}, {}
surnames_tables = {}
name_table_amalgamated_male, name_table_amalgamated_female = [], []

author_title_tables = []
epithets_tables = []
adjective_1_list = []
noun_1_list = []
noun_2_list = []
titles_study_of_list = []
titles_study_in_list = []
titles_study_on_list = []
titles_template_list = []


