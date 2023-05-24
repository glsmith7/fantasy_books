import oop_roll_on_tables_GLS as r
import random as random
import string as string
import d20

global the_list_of_tables
global list_of_names_tables_male, list_of_names_tables_female
global name_tables_male, name_tables_len_male, name_table_amalgamated_male 
global name_tables_female, name_tables_len_female, name_table_amalgamated_female
global author_title_tables
global complexity_table_list
global CHANCE_OF_BEING_TRANSLATION, ANCIENT_LANGUAGES_WHICH_WOULD_NOT_HAVE_TRANSLATED 

CHANCE_OF_BEING_TRANSLATION = 10 # ten percent chance; can be changed as wished.
ANCIENT_LANGUAGES_WHICH_WOULD_NOT_HAVE_TRANSLATED = 'Ancient,Elvish'

# the_list_of_tables_for_randomize = [ # SQL table name first, then self.variable for the book object. Make sure has a aaDiceTypeToRoll table entry for each table.
#         ("BookScope","scope"),
#         ("BookCurrentLanguage","current_language"),
#         ]


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


def init_program_load_tables():
        
    # names of male and female

    for i in list_of_names_tables_male:
        name_tables_male[i] = r.MadLibTable(i)
        name_tables_len_male[i] = name_tables_male[i].number_of_rows
        name_table_amalgamated_male.extend (name_tables_male[i].content)

    for i in list_of_names_tables_female:
        name_tables_female[i] = r.MadLibTable(i)
        name_tables_len_female[i] = name_tables_female[i].number_of_rows
        name_table_amalgamated_female.extend (name_tables_female[i].content)

    # surnames
    for i in list_of_surnames_tables:
        x = r.MadLibTable(i)
        surnames_tables[i] = x.content 

    # titles
    author_title_tables.extend (r.MadLibTable('_titles_person').content)

def create_fantasy_book(type=None, **kwargs):
    ''' Returns a book object. Type can be default (normal), esoteric, or authority'''
    if type == "esoteric":
        return EsotericBook(**kwargs)
    elif type == "authority":
        return AuthoritativeBook(**kwargs)
    else:
        return FantasyBook(**kwargs)
    


class FantasyBook():
    ''' Fantasy book object.'''

    # remember to add any variables added here to the self.XXXX list below, AND to the routine randomize_book_statistics 
    # if the value is to be set from a random table.

    def __init__(self,         
        topic = "",
        topic_title_form = "",
        title = "",
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
        age = 0,
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
        ):

        # set all values to whatever they were passed in 
        self.topic = topic
        self.topic_title_form = topic_title_form
        self.title = title
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
        self.age = age
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

        self.scope_set(self.scope)
        self.current_language_set(self.current_language)
        self.age_set(self.age)
        self.translator_set(self.translator) # must be called before original_language_set
        self.original_language_set(self.original_language)
        self.topic_set(self.topic)
        self.topic_title_set(self.topic_title_form)
        self.sex_set(self.sex)
        self.author_name_set(self.author_name)
        self.author_title_set (self.author_title)
        self.author_epithet_set (self.author_epithet)
        self.author_full_set (self.author_full)
        self.complexity_set(self.complexity)
        
        self.format_set(self.format)

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

    def add(self,library):
        ''' Add this book to a given library'''
        self.libraries_it_is_in.append(library)

    def age_set(self,age):
        if not age:
            table_name = "BookAge_" + self.current_language
            dice_string = self.book_details_result_from_tables(table_name)
            if self.is_a_translation == "True": 
                self.age = d20.roll("1d100+20").total # bonus to age if is translation.
            
            self.age = self.age + d20.roll(dice_string).total
        else:
            self.age = age

    def author_name_set(self,author_name):
        
        if not author_name:        
            
            # first name
            if self.sex == "Male": first_name = random.choice(name_table_amalgamated_male)
            else: first_name = random.choice(name_table_amalgamated_female)
            self.author_nationality = str(first_name[1]) # the second row (i.e. index 1 since starts at 0) is the table for this type of name's surname.
            
            # surname
            last_name = random.choice(surnames_tables[self.author_nationality])
            author_name = str(first_name[0]) + " " + str(last_name[0]) # first (0 index) item is the name
            
        self.author_name = author_name
    
    def author_title_set(self, author_title):
         # title of the author
        if not author_title:

            author_title = str(random.choice(author_title_tables)[0])
            
           
            #  # male/female titles are separated by a slash in the SQL database  
            if author_title.__contains__("/"):
                title_split = author_title.split("/",2)
                
                if self.sex == "Male":
                    author_title = title_split[0]
                else:
                    author_title = title_split[1]
        
        author_title = string.capwords(author_title)
        self.author_title = author_title
    
    def author_epithet_set (self, author_epithet):
        pass

    def author_full_set (self, author_full):
        # put it all together
        if not author_full:

            if self.author_title != "None": author_full = author_full.join([self.author_title," "])
            author_full += (self.author_name)
        
        self.author_full = author_full

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
            dice_string = dice[0] # dice[0] is the only thing returned, and this makes it a string rather than list as dice is.
            roll_result = r.d20.roll(dice_string) 

        # actually do the roll now that we know what dice we're rolling
        t = r.RPG_table(table_for_value)
        rolled_row = t.roll(roll_result.total) # .total sends only the integer total, nil else.
        return rolled_row['Result'] 
    
    def complexity_set(self,complexity):
        if not complexity:
            complexity_from_table = self.book_details_result_from_tables(complexity_table_list[self.scope-1]) # Minus 1 since index of list starts at zero.
            setattr(self,"complexity",complexity_from_table[0]) # index 0 converts to string eg 1, instead of list ['1']
        
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
            if self.age < 11: target_table += "0001-0010"
            elif self.age < 51: target_table += "0011-0050"
            elif self.age < 101: target_table += "0051-0100"
            elif self.age < 501: target_table += "0101-0500"
            elif self.age < 1001: target_table += "0501-1000"
            elif self.age < 2001: target_table += "1001-2000"
            elif self.age < 10001: target_table += "2001-10000"

            self.format = self.book_details_result_from_tables(target_table)
        else:
            self.format = format

    def look_up_table (self,table_name,search_term):
        query = 'SELECT title_string from {} where Result LIKE "{}"'.format(table_name, search_term)
        t = r.LookUpTable(table_name = table_name, query = query)
        return t.content[0] # gets the tuple that returns out of the list.
    
    
    def original_language_set(self, original_language):
        if self.is_a_translation == "False":
            return

        if not original_language: # original language is empty
            original_language = self.book_details_result_from_tables("BookOriginalLanguage")

            while original_language == self.current_language:  
                original_language = self.book_details_result_from_tables("BookOriginalLanguage") # reroll until not the same
        
        self.original_language = original_language
        

    # def randomize_book_details(self):
    #     ''' Loops through all variables and assigns randomly based on random SQL table rolls.'''
    
    #     for i,j in the_list_of_tables_for_randomize:
    #         setattr(self,j,self.book_details_result_from_tables(i)) # sets variable J of object the_book to the rolled results on table i for each element.

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

            t = self.look_up_table(table_name= "_topic_for_titles", search_term = self.topic)
            t = t[0].split(";") # first and only item of tuple to get rid of ('Response') and give Response. This is split by semicolons to make a list of various options.
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
        esoteric_complexity = 0, 
        esoteric_scope = 0, 
        esoteric_topic = []):

        super().__init__(self)
        self.esoteric_complexity = esoteric_complexity
        self.esoteric_scope = esoteric_scope
        self.esoteric_topic = esoteric_topic

class AuthoritativeBook(FantasyBook):
    ''' Subclass of fantasy book, that has a few extra values.'''
    def __init__ (self,
        authoritative_field = "", 
        authority_rank = 0,
                ):
        super().__init__(self)
        self.authoritative_field = authoritative_field
        self.authority_rank = authority_rank

############################
# main()
init_program_load_tables()
number_to_run = 100

for z in range(0,number_to_run):

    a = create_fantasy_book()
    print ("Scope:" + str(a.scope))
    print ("Current Lang:" + str(a.current_language))
    print ("Original Lang:" + str(a.original_language))
    print ("Translator:" + a.translator)
    print ("Complex:" + str(a.complexity))
    print ("Sex:" + str(a.sex))
    print ("Author:" + str(a.author_full))
    print ("Topic:" + str(a.topic))
    print ("Topic title:" + str(a.topic_title_form))
    # print ("Actual title:" + a.title)
    print ("Age:" + str(a.age))
    print ("Format:" + str(a.format))

    print ("---")