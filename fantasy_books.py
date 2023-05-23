import oop_roll_on_tables_GLS as r
import random as random

global the_list_of_tables
global list_of_names_tables_male, list_of_names_tables_female
global name_tables_male, name_tables_len_male, name_table_amalgamated_male 
global name_tables_female, name_tables_len_female, name_table_amalgamated_female
global author_title_tables
global complexity_table_list

the_list_of_tables = [ # SQL table name first, then self.variable for the book object. Make sure has a aaDiceTypeToRoll table entry for each table.
        ("BookScope","scope"),
        ("BookOriginalLanguage","original_language"),
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
        "_names_arabic_surnames",
        "_names_anglo_saxon_surnames", 
        "_names_english_surnames",
        "_names_famous_surnames", 
        "_names_french_surnames", 
        "_names_norse_surnames_female",
		"_names_norse_surnames_male",
        "_names_saints_surnames", 
        ]
complexity_table_list = ["BookComplexityForScope1","BookComplexityForScope2","BookComplexityForScope3","BookComplexityForScope4"]

name_tables_male, name_tables_len_male = {}, {}
name_tables_female, name_tables_len_female = {}, {}
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
        title = "",
        sex = "",
        author = "",
        original_language = "",
        translated_language = "N/A",
        translator = "N/A",
        format = "b",
        materials = "a",
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
        
        self.randomize_book_details() # scope, 

        self.topic = topic
        self.title = title
        self.sex_set(sex)
        self.author_set(author)
        self.translator = translator
        self.original_language = original_language
        self.translated_language = translated_language
        self.set_complexity(complexity)
        self.age = age
        self.format = format
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
    
    def add(self,library):
        ''' Add this book to a given library'''
        self.libraries_it_is_in.append(library)


    def randomize_book_details(self):
        ''' Loops through all variables and assigns randomly based on random SQL table rolls.'''
    
        for i,j in the_list_of_tables:
            setattr(self,j,self.book_details_result_from_tables(i)) # sets variable J of object the_book to the rolled results on table i for each element.
    
    def set_complexity(self,complexity):
        if not complexity:
            complexity_from_table = self.book_details_result_from_tables(complexity_table_list[self.scope-1]) # Minus 1 since index of list starts at zero.

            setattr(self,"complexity",complexity_from_table[0]) # index 0 converts to string eg 1, instead of list ['1']
            print ("pause")
        else:
            self.complexity = complexity

    def remove (self,library):
        ''' Remove this book from a given library'''
        try:
            self.libraries_it_is_in.remove(library)
        except ValueError:
            print ("The book _{}_ is not in {} library.".format(self.title, library))
    
    def sex_set (self, sex):
        if not sex:
            self.sex = random.choice(["Male", "Male","Female"]) # makes males 2/3 of the time for historical reasons.
        else:
            self.sex = sex

    def author_set(self,author_name):

        # name of author
        if author_name:
            self.author = author_name

        else:
            if self.sex == "Male":
                first_name = random.choice(name_table_amalgamated_male)
                author_name = str(first_name[0]) # first item is the name
                author_nationality = str(first_name[1])
            else:
                first_name = random.choice(name_table_amalgamated_female)
                author_name = str(first_name[0]) # first item is the name
                author_nationality = str(first_name[1])

        # title of the author
        print (author_nationality)
        title = str(random.choice(author_title_tables)[0])
            
        # male/female titles are separated by a slash in the SQL database  
        if title.__contains__("/"):
            title_split = title.split("/",2)
            
            if self.sex == "Male":
                title = title_split[0]
            else:
                title = title_split[1]
        
        # put it all together
        full_author = ""
        print ("Title:" + title)
        if title != "None": full_author = full_author.join([title," "])
        full_author += (author_name)
        self.author = full_author

            
    
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
    print ("Lang:" + str(a.original_language))
    print ("Complex:" + str(a.complexity))
    print ("Sex:" + str(a.sex))
    print ("Author:" + str(a.author))
    print ("---")