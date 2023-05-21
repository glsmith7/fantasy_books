import oop_roll_on_tables_GLS as r

class FantasyBook():
    ''' Fantasy book object.'''
    def __init__(self,         
        topic = "",
        title = "",
        author = "",
        original_language = "",
        translated_language = "N/A",
        translator = "N/A",
        format = "b",
        materials = "a",
        libraries_it_is_in = [],
        scope = 0,
        complexity = 5,
        age = 2,
        number_extant_copies = 0,
        number_pages = 0,
        reading_time = 0,
        reference_time = 0,
        production_value = 0,
        literary_value_base = 0,
        literary_value_modified = 0,
        rarity_modifier = 0,
        value = 0,
        weight = 0,
        number_volumes = 0,):

        self.topic = topic
        self.title = title
        self.author = author
        self.translator = translator
        self.original_language = original_language
        self.translated_language = translated_language
        self.scope = scope
        self.complexity = complexity
        self.age = age
        self.format = format
        self.materials = materials
        self.libraries_it_is_in = libraries_it_is_in
        self.number_extant_copies = number_extant_copies
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
        #if self.libraries_it_is_in:
        self.libraries_it_is_in.append(library)
        #else:
         #   self.libraries_it_is_in = library

    def remove (self,library):
        ''' Remove this book from a given library'''
        try:
            self.libraries_it_is_in.remove(library)
        except ValueError:
            print ("The book _{}_ is not in {} library.".format(self.title, library))
        
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

def create_fantasy_book(type=None):
    ''' Returns a book object. Type can be default (normal), esoteric, or authority'''
    if type == "esoteric":
        return EsotericBook()
    elif type == "authority":
        return AuthoritativeBook()
    else:
        return FantasyBook()
    
def generate_book_details(b,table_for_value):

    # what dice to roll on the table   
    dice = r.what_dice_to_roll(table_for_value) # returns a list
    if dice == []:
        raise ValueError("Empty dice list returned -- does aaDiceTypeToRoll have an entry for this table?")

    dice_string = dice[0] # dice[0] is the only thing returned, and this makes it a string rather than list as dice is.
    
    
    roll_result = r.d20.roll(dice_string) 

    # actually do the roll
    t = r.RPG_table(table_for_value)
    rolled_row = t.roll(roll_result.total) # .total sends only the integer total, nil else.
    return rolled_row['Result']

def loop_thru(a):
    the_list_of_tables = [
        ("BookScope","scope"),
        ("BookOriginalLanguage","original_language")
        ]

    for i,j in the_list_of_tables:
        setattr(a,j,generate_book_details(a,i)) # sets variable J of object a to the rolled results on table i for each element.
        

a = create_fantasy_book()
loop_thru(a)
print (a.scope)
print (a.original_language)




