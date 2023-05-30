import rpg_tables as r
import random as random
import string as string
import d20

# logging boilerplate
import settings_GLS as s
import logging
import logging_tools_GLS
logger = logging.getLogger(__name__)
#########################################################

# general

global list_of_words_to_not_capitalize
global complexity_table_list

# names
global list_of_names_tables_male, list_of_names_tables_female
global name_tables_male, name_table_amalgamated_male 
global name_tables_female, name_table_amalgamated_female
global author_title_table, epithets_tables

# titles
global titles_adjective_1_list, titles_noun_1_list, titles_noun_2_list, titles_study_of_list, titles_study_in_list, titles_study_on_list
global titles_template_list, titles_history_of, titles_conjunction_about, titles_conjunction_by, titles_fixed
global titles_negative_subject, titles_places_cities, titles_places_nations, titles_religious_starter, titles_study_verbing, titles_the_1
global titles_person_1, titles_person_2, titles_communication, titles_biography_starter, titles_person_evil
global titles_person_famous_male, titles_person_famous_female, titles_person_famous_amalgamated, titles_saints_male, titles_saints_female, titles_saints_amalgamated
 			
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
        "_names_anglo_saxon_male",
        "_names_arabic_male",
        "_names_english_male",
        "_names_famous_male", 
        "_names_french_male", 
        "_names_norse_male",
        "_names_roman_male", 
        ]

list_of_names_tables_female = [
        "_names_arabic_female",
        "_names_anglo_saxon_female", 
        "_names_english_female",
        "_names_famous_female", 
        "_names_french_female", 
        "_names_norse_female",
        "_names_roman_female", 
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

surnames_tables = {}
name_tables_male = {}
name_tables_female = {}



# titles
author_title_table = r.RPG_table('_titles_person')

#epithets
epithets_table = r.RPG_table('_epithets')

# book title lists
titles_adjective_1_list = r.RPG_table('_book_titles_adjective_1')
titles_noun_1_list = r.RPG_table('_book_titles_noun_1')
titles_noun_2_list = r.RPG_table('_book_titles_noun_2')
titles_study_of_list = r.RPG_table('_book_titles_study_of')
titles_study_in_list = r.RPG_table('_book_titles_study_in')
titles_study_on_list = r.RPG_table('_book_titles_study_on')
titles_template_list = r.RPG_table('_book_titles_templates')
titles_history_of = r.RPG_table('_book_titles_history')
titles_conjunction_about = r.RPG_table('_book_titles_conjunction_about')
titles_conjunction_by = r.RPG_table('_book_titles_conjunction_by')
titles_fixed = r.RPG_table('_book_titles_fixed')
titles_negative_subject = r.RPG_table('_book_titles_negative_subject')
titles_places_cities = r.RPG_table('_book_titles_places_cities')
titles_places_nations = r.RPG_table('_book_titles_places_nations')
titles_religious_starter = r.RPG_table('_book_titles_religious_starter')
titles_study_verbing = r.RPG_table('_book_titles_study_verbing')
titles_the_1 = r.RPG_table('_books_titles_the_1')
titles_saints_male=r.RPG_table('_names_saints_male')
titles_saints_female=r.RPG_table('_names_saints_female')
titles_saints_amalgamated= titles_saints_male + titles_saints_female

titles_person_famous_male=r.RPG_table('_names_famous_male')
titles_person_famous_female=r.RPG_table('_names_famous_female')
titles_person_famous_amalgamated=titles_person_famous_male + titles_person_famous_female


titles_communication=r.RPG_table('_book_titles_communication')
titles_biography_starter=r.RPG_table('_book_titles_biography_starter')
titles_person_evil=r.RPG_table('_names_famous_evil')

# titles_person_1 =r.RPG_table('XXXX')
# titles_person_2=r.RPG_table('XXXX') 			
# XXXXX = r.RPG_table('XXXXX')
# XXXXX = r.RPG_table('XXXXX')
# XXXXX = r.RPG_table('XXXXX')

# blank lists for later use
name_table_amalgamated_male = r.RPG_table('_names_empty')
name_table_amalgamated_male.description = "Male Names Amalgamated"
name_table_amalgamated_female = r.RPG_table('_names_empty')
name_table_amalgamated_female.description = "Female Names Amalgamated"


def init_program_load_tables():
    
    # names of male and female
    global name_table_amalgamated_male, name_tables_male
    global name_table_amalgamated_female,name_tables_female


    for i in list_of_names_tables_male:
        name_tables_male[i] = r.RPG_table(i)
        name_table_amalgamated_male = (name_tables_male[i]) + name_table_amalgamated_male

    for i in list_of_names_tables_female:
        name_tables_female[i] = r.RPG_table(i)
        name_table_amalgamated_female += (name_tables_female[i])

        # surnames
    for i in list_of_surnames_tables:
        surnames_tables[i] = r.RPG_table(i) # creates dictionary containing a table for each nationality.


def create_fantasy_book(book_type=None, **kwargs):
    ''' Returns a book object. Type can be default (normal), esoteric, or authority'''
    book_type = string.capwords(str(book_type))
    if book_type == "Esoteric":
        return EsotericBook(**kwargs)
    elif book_type == "Authority":
        return AuthoritativeBook(**kwargs)
    else:
        return FantasyBook(**kwargs)
    
class FantasyBook():
    ''' Fantasy book object.'''

    # remember to add any variables added here to the self.XXXX list below, AND to the routine randomize_book_statistics 
    # if the value is to be set from a random table.

    def __init__(self,
        book_type = "Standard",         
        topic = "",
        topic_title_form = "",
        book_title = "",
        sex = "",
        author_name = "",
        author_title = "",
        author_epithet = "",
        author_full = "",
        author_nationality = "",
        current_language = "",
        original_language = "",
        is_a_translation = "False",
        translator = "",
        format = "",
        materials = "",
        libraries_it_is_in = [],
        number_extant_copies = 0,
        number_extant_available_to_place = 0,
        scope = 0,
        complexity = 0,
        age_at_discovery = 0,
        number_pages = 0,
        reading_time = 0,
        reference_time = 0,
        production_value = 0,
        literary_value_base = 0,
        literary_value_modified = 0,
        rarity_modifier = 0,
        value = 0,
        weight = 0,
        number_volumes = 0,
        year_discovered = 0,
        year_written = 0,
        ):

        # set all values to whatever they were passed in 
        self.book_type = book_type
        self.topic = topic
        self.topic_title_form = topic_title_form
        self.book_title = book_title
        self.sex = sex
        self.author_name = author_name
        self.author_title = author_title
        self.author_epithet = author_epithet
        self.author_full = author_full
        self.author_nationality = author_nationality
        self.current_language = current_language
        self.original_language = original_language
        self.is_a_translation = is_a_translation
        self.translator = translator
        self.format = format
        self.materials = materials
        self.libraries_it_is_in = libraries_it_is_in
        self.number_extant_copies = number_extant_copies
        self.number_extant_available_to_place = number_extant_available_to_place
        self.scope = scope
        self.complexity = complexity
        self.age_at_discovery = age_at_discovery
        self.number_pages = number_pages
        self.reading_time = reading_time
        self.reference_time = reference_time
        self.production_value = production_value
        self.literary_value_base = literary_value_base
        self.literary_value_modified = literary_value_modified
        self.rarity_modifier = rarity_modifier
        self.value = value
        self.weight = weight
        self.number_volumes = number_volumes
        self.year_discovered = year_discovered
        self.year_written = year_written

        self.scope_set(self.scope)
        self.current_language_set(self.current_language)
        self.age_set(self.age_at_discovery)
        self.translator_set(self.translator) # must be called before original_language_set
        self.original_language_set(self.original_language)
        self.topic_set(self.topic)
        self.topic_title_set(self.topic_title_form)
        self.sex_set(self.sex)
        self.author_epithet_set (self.author_epithet)
        self.author_name_set(self.author_name)
        self.author_title_set (self.author_title)
        self.author_full_set (self.author_full)
        self.complexity_set(self.complexity)
        self.format_set(self.format)
        self.book_title_set(self.book_title)
        self.materials = materials
        self.libraries_it_is_in = libraries_it_is_in
        self.number_extant_copies = number_extant_copies
        self.number_extant_available_to_place = number_extant_available_to_place
        self.number_pages = number_pages
        self.reading_time = reading_time
        self.reference_time = reference_time
        self.production_value = production_value
        self.literary_value_base = literary_value_base
        self.literary_value_modified = literary_value_modified
        self.rarity_modifier = rarity_modifier
        self.value = value
        self.weight = weight
        self.number_volumes = number_volumes
        self.year_discovered = year_discovered
        self.year_written = year_written

    def add(self,library):
        ''' Add this book to a given library'''
        self.libraries_it_is_in.append(library)

    def age_set(self,age):
        if not age:
            table_name = "BookAge_" + self.current_language # Ancient, Dwarvish, Elvish, Classical, Common are options
            dice_string = self.book_details_result_from_tables(table_name)
            if self.is_a_translation == "True": 
                self.age_at_discovery = d20.roll("1d100+20").total # bonus to age if is translation.
            
            self.age_at_discovery = self.age_at_discovery + d20.roll(dice_string).total
        else:
            self.age_at_discovery = age
    
    def author_epithet_set (self, author_epithet):
        if not author_epithet:
            if CHANCE_OF_EPITHET > d20.roll("1d100").total:
                author_epithet = epithets_table.df.sample() # a random option is then chosen
                author_epithet = author_epithet.iloc[0,0]
                          
        self.author_epithet = author_epithet
             

    def author_full_set (self, author_full):
        # put it all together
        if not author_full:

            if self.author_title != "" and self.author_title != "None": author_full = author_full.join([self.author_title," "])
            author_full += (self.author_name)
            if self.author_epithet != "" and self.author_epithet != "None": author_full = author_full + " " + self.author_epithet
        
        self.author_full = author_full
    
    def author_name_set(self,author_name):
        
        if not author_name:        
            
            # first name
            if self.sex == "Male": first_name = name_table_amalgamated_male.df.sample()
            else: first_name = name_table_amalgamated_female.df.sample()
            self.author_nationality = (first_name.iloc[0,1]) # the second column (i.e. index 1 since starts at 0) is the table for this type of name's surname.
            
            # surname
            last_name_table = (surnames_tables[self.author_nationality])
            last_name = last_name_table.df.sample()
            author_name = str(first_name.iloc[0,0]) + " " + str(last_name.iloc[0,0]) # first (0 index) item is the name
            
        self.author_name = author_name

    def author_title_set(self, author_title):
        global author_title_table

         # title of the author
        if not author_title:
            author_title = str(author_title_table.df.sample().iloc[0,0])
           
            #  # male/female titles are separated by a slash in the SQL database  
            if author_title.__contains__("/"):
                title_split = author_title.split("/",2)
                
                if self.sex == "Male":
                    author_title = title_split[0]
                else:
                    author_title = title_split[1]
        
        author_title = string.capwords(author_title)
        self.author_title = author_title

    def book_details_result_from_tables(self,table_for_value):
        ''' Checks table aaDiceTypeToRoll to see what dice to roll, and then rolls and checks the result on the given table.
        All tables that use this should have:
        1) An entry in SQL table aaDiceTypeToRoll with the same table name that matches table to roll on.
        2) The SQL table to be rolled on should have only two columns: one called 'DieRange' and the other 'Result'. '''

        # what dice to roll on the table   
        dice = r.what_dice_to_roll(table_for_value) # returns a list
        if dice == []:
            raise ValueError("Empty dice list returned -- does SQL table 'aaDiceTypeToRoll' have an entry for this table?")
        else:
            dice_string = dice# [0] # dice[0] is the only thing returned, and this makes it a string rather than list as dice is.
            roll_result = r.d20.roll(dice_string) 

        # actually do the roll now that we know what dice we're rolling
        t = r.RPG_table(table_for_value)
        rolled_row = t.roll(roll_result.total) # .total sends only the integer total, nil else.
        return rolled_row 
    
    def book_title_set(
            self,
            adjective_1=None, 
            noun_1=None, 
            noun_2=None, 
            study_of=None, 
            study_in=None, 
            study_on=None, 
            template=None,
            final_title=None,
            conjunction_about=None,
            conjunction_by=None,
            negative_1=None,
            place_city=None,
            place_nation=None,
            religious_starter=None,
            verbing=None,
            saint=None,
            person_1=None,
            person_2=None,
            person_famous=None,
            communication=None,
            biography_starter=None,
            person_evil=None,
            history_of=None,
            the_1=None,

            ):
        
        global titles_adjective_1_list, titles_noun_1_list, titles_noun_2_list, titles_study_of_list, titles_study_in_list, titles_study_on_list
        global titles_template_list, titles_history_of, titles_conjunction_about, titles_conjunction_by, titles_fixed
        global titles_negative_subject, titles_places_cities, titles_places_nations, titles_religious_starter, titles_study_verbing, titles_the_1
        global titles_person_1, titles_person_2, titles_communication, titles_biography_starter, titles_person_evil
        global titles_person_famous_male, titles_person_famous_female, titles_person_famous_amalgamated, titles_saints_male, titles_saints_female, titles_saints_amalgamated

        if final_title: self.book_title = final_title
        
        else:
            if not template: template = titles_template_list.df.sample().iloc[0,0]
            if not adjective_1 and "{adjective_1}" in template: adjective_1 = titles_adjective_1_list.df.sample().iloc[0,0]
            if not noun_1 and "{noun_1}" in template: noun_1 = titles_noun_1_list.df.sample().iloc[0,0]
            if not noun_2 and "{noun_2}" in template: noun_2 = titles_noun_2_list.df.sample().iloc[0,0]
            if not study_of and "{study_of}" in template: study_of = titles_study_of_list.df.sample().iloc[0,0]
            if not study_in and "{study_in}" in template: study_in = titles_study_in_list.df.sample().iloc[0,0]
            if not study_on and "{study_on}" in template: study_on = titles_study_on_list.df.sample().iloc[0,0]
            if not conjunction_about and "{conjunction_about}" in template: conjunction_about = titles_conjunction_about.df.sample().iloc[0,0]
            if not conjunction_by and "{conjunction_by}" in template: conjunction_by = titles_conjunction_by.df.sample().iloc[0,0]
            if not negative_1 and "{negative_1}" in template: negative_1 = titles_negative_subject.df.sample().iloc[0,0]
            if not place_city and "{place_city}" in template: place_city = titles_places_cities.df.sample().iloc[0,0]
            if not place_nation and "{place_nation}" in template: place_nation = titles_places_nations.df.sample().iloc[0,0]
            if not religious_starter and "{religious_starter}" in template: religious_starter = titles_religious_starter.df.sample().iloc[0,0]
            if not verbing and "{verbing}" in template: verbing = titles_study_verbing.df.sample().iloc[0,0]
            if not saint and "{saint}" in template: saint = titles_saints_amalgamated.df.sample().iloc[0,0]
            if not person_famous and "{person_famous}" in template: person_famous = titles_person_famous_amalgamated.df.sample().iloc[0,0]
            if not communication and "{communication}" in template: communication = titles_communication.df.sample().iloc[0,0]
            if not biography_starter and "{biography_starter}" in template: biography_starter = titles_biography_starter.df.sample().iloc[0,0]
            if not person_evil and "{person_evil}" in template: person_evil = titles_person_evil.df.sample().iloc[0,0]
            if not history_of and "{history_of}" in template: history_of = titles_history_of.df.sample().iloc[0,0]
            if not the_1 and "{the_1}" in template: the_1 = titles_the_1.df.sample().iloc[0,0]

            if "{person_1}" in template: person_1 = "PERSON 1"
            if "{person_2}" in template: person_2 = "PERSON 2"
            # if not XXX and "{XXXX}" in template: study_on = titles_fixed.df.sample().iloc[0,0]
            # if not person_1 and "{person_1}" in template: study_on = titles_person_1.df.sample().iloc[0,0]
            # if not person_2 and "{person_2}" in template: study_on = titles_person_2.df.sample().iloc[0,0]

            topic = self.topic_title_form
            self.template = template

            self.book_title = template.format(
                adjective_1=adjective_1, 
                noun_1 = noun_1, 
                noun_2 = noun_2, 
                study_of = study_of, 
                study_in = study_in, 
                study_on = study_on, 
				topic = topic,
				conjunction_about=conjunction_about,
				conjunction_by=conjunction_by,
				negative_1=negative_1,
				place_city=place_city,
				place_nation=place_nation,
				religious_starter=religious_starter,
				verbing=verbing,
				saint=saint,
				person_1=person_1,
				person_2=person_2,
				person_famous=person_famous,
				communication=communication,
				biography_starter=biography_starter,
				person_evil=person_evil,
				history_of=history_of,
                the_1 = the_1
            )






    def complexity_set(self,complexity):
        if not complexity:
            complexity_from_table = self.book_details_result_from_tables(complexity_table_list[self.scope-1]) # Minus 1 since index of list starts at zero.
            self.complexity = complexity_from_table # index 0 converts to string eg 1, instead of list ['1']
        
        else:
            self.complexity = complexity
    
    def current_language_set(self, current_language):
        if not current_language:
            self.current_language = self.book_details_result_from_tables("BookCurrentLanguage")
        else:
            self.current_language = current_language

    def format_set(self,format):
        if not format:
            target_table = "BookAge_Format_"
            if self.age_at_discovery < 11: target_table += "0001_0010"
            elif self.age_at_discovery < 51: target_table += "0011_0050"
            elif self.age_at_discovery < 101: target_table += "0051_0100"
            elif self.age_at_discovery < 501: target_table += "0101_0500"
            elif self.age_at_discovery < 1001: target_table += "0501_1000"
            elif self.age_at_discovery < 2001: target_table += "1001_2000"
            elif self.age_at_discovery < 10001: target_table += "2001_10000"

            self.format = self.book_details_result_from_tables(target_table)
        else:
            self.format = format

    def look_up_table (self,table_name,search_term):
        query = 'SELECT title_string from {} where Result LIKE "{}"'.format(table_name, search_term)
        t = r.LookUpTable(query = query)
        return t.result   
    
    def original_language_set(self, original_language):
        
        if self.is_a_translation == "False":
            return

        if not original_language: # original language is empty
            original_language = self.book_details_result_from_tables("BookOriginalLanguage")

            while original_language == self.current_language:  
                original_language = self.book_details_result_from_tables("BookOriginalLanguage") # reroll until not the same
        
        self.original_language = original_language

    def remove (self,library):
        ''' Remove this book from a given library'''
        try:
            self.libraries_it_is_in.remove(library)
        except ValueError:
            print ("The book _{}_ is not in {} library.".format(self.title, library))
    
    def scope_set(self, scope):
        if not scope:
            self.scope = self.book_details_result_from_tables("BookScope")
        else:
            self.scope = scope
    
    def sex_set (self, sex):
        if not sex:
            self.sex = random.choice(["Male", "Male","Female"]) # makes males 2/3 of the time for historical reasons.
        else:
            self.sex = sex
    
    def topic_set (self, topic):

        if not topic:
            topic = self.book_details_result_from_tables("BookTopicsACKS")
        self.topic = topic
    
    def  topic_title_set(self,topic_title_form):
        if not topic_title_form:

            t = self.look_up_table(table_name= "_book_titles_topics", search_term = self.topic)
            t = t.split(";") # list is made by separating by semicolons
            t = random.choice(t) # a random option is then chosen
            self.topic_title_form = t 
        
        else:
            self.topic_title_form = topic_title_form

    def translator_set (self, translator):
        roll_to_see_if_it_is_a_translation = d20.roll("1d100").total
        if roll_to_see_if_it_is_a_translation > CHANCE_OF_BEING_TRANSLATION or ANCIENT_LANGUAGES_WHICH_WOULD_NOT_HAVE_TRANSLATED.__contains__(self.current_language):
            self.translator = "N/A"
            self.is_a_translation = "False"
        else:
            self.translator = "Some dude"
            self.is_a_translation = "True"


class EsotericBook(FantasyBook):
    ''' Subclass of fantasy book, that has a few extra values.'''
    def __init__ (self,
        book_type = "Esoteric",
        esoteric_complexity = 0, 
        esoteric_scope = 0, 
        esoteric_topic = []):

        super().__init__(self)
        self.book_type = book_type
        self.esoteric_complexity = esoteric_complexity
        self.esoteric_scope = esoteric_scope
        self.esoteric_topic = esoteric_topic

class AuthoritativeBook(FantasyBook):
    ''' Subclass of fantasy book, that has a few extra values.'''
    def __init__ (self,
        book_type = "Authoritative",
        authoritative_field = "", 
        authority_rank = 0,
                ):
        super().__init__(self)
        self.book_type = book_type
        self.authoritative_field = authoritative_field
        self.authority_rank = authority_rank

############################
# main()
init_program_load_tables()
number_to_run = 100

for z in range(0,number_to_run):

    a = create_fantasy_book()
    print ("Book type:" + str(a.book_type))
    print ("Scope:" + str(a.scope))
    print ("Current Lang:" + str(a.current_language))
    print ("Original Lang:" + str(a.original_language))
    print ("Translator:" + a.translator)
    print ("Complex:" + str(a.complexity))
    print ("Sex:" + str(a.sex))
    print ("Epithet:" + str(a.author_epithet))
    print ("Author title:" + str(a.author_title))
    print ("Author:" + str(a.author_full))
    print ("Topic:" + str(a.topic))
    print ("Topic title:" + str(a.topic_title_form))
    print ("Actual title:" + a.book_title)
    print ("Age:" + str(a.age_at_discovery))
    print ("Format:" + str(a.format))
    print ("Template:" + str(a.template))
    print ("---")
