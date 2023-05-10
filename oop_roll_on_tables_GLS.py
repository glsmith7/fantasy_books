import sqlite3
import os
import datetime
import array
import re
import d20
import settings_GLS as s

# logging boilerplate
import logging
import logging_tools_GLS
logger = logging.getLogger(__name__)


class SQL_object_GLS:
    ''' A connection to an SQLite database object '''

    def __init__ (self, path = s.PATH_DEFAULT):
       
        self.path = path
        self.connect_to_database(self.path)

    def connect_to_database(self,path):
        
        if os.path.isfile(path) == False:
            logger.error ("Database name does not exist.")
            raise FileNotFoundError

        try:
            self.connection = sqlite3.connect(path)

        except OSError as err:
       
            logger.error ("The error" + err + " occurred.")
            return(print(f"The error '{err}' occurred"))
            raise

        else:
             logger.info ("SLQ connection established: " + str(self.connection))
    
class RPG_table(SQL_object_GLS):
    ''' Subclass of SQL database object that represents an RPG table. '''

    def __init__ (self,table_name,query = s.SQL_QUERY_DEFAULT,path=s.PATH_DEFAULT):
        super().__init__(path)
        self.pick_table (table_name,query)
        

    def pick_table (self,table_name,query= s.SQL_QUERY_DEFAULT): # can be used to pick a new table
        ''' Combines all subroutines to prepare an RPG table for reference.'''

        self.table_name = table_name
        self.query = query
        self.query = self.query.replace("_replace_",self.table_name)
        self._retrieve_from_database()
        self.get_column_names()
        self._get_2d_array()
        if "DieRange" in self.column_names:
            self._convert_die_range_to_low_and_high()
        self._get_row_names()
        self._finalize_table()

    def _retrieve_from_database(self):
        ''' Returns the SQL query results'''
        if type(self.connection) is not sqlite3.Connection:
            logger.error ("There is no open connection to a database.")
            raise sqlite3.DatabaseError ("There is no open connection to a database.")
          
        # self.query = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'TestTable01' ORDER BY ORDINAL_POSITION"
        
        cursor = self.connection.cursor()
        cursor.execute(self.query)
        self.database_results = cursor.fetchall()

        logger.info ("Search result of SQL database returned as: " + str(self.database_results) + "\n")


    def get_column_names(self):
        ''' Retrieves and stores the column names for the table '''
        query_column_names = "PRAGMA table_info({});".format(self.table_name) # returns column names from SQLite
        cursor = self.connection.cursor()
        cursor.execute(query_column_names)
        column_results = cursor.fetchall()

        self.column_names = []
        for row in column_results:
            self.column_names.append(row[1])
    
        logger.info ("Column names returned as: " + str(self.column_names) + "\n")

    def _get_row_names(self):
        ''' Uses database_results to get the row names'''
        self.row_names = []
        for x in range (0,len(self.database_results)):
            self.row_names.append(self.database_results[x][self.column_names[0]])


    def _get_2d_array(self):
   
        """ Returns a list with nested dictionaries. Each dictionary is a row of the table, with columns of the table as keywords
    
        j = iterates through each row
        i = iterates through each column
        """
        
        for j in range (0,len(self.database_results)):
            d = {} # Empty the dictionary before each row started

            for i in range (0,len(self.column_names)):
                d[self.column_names[i]] = self.database_results[j][i]
            
            self.database_results[j] = d # set the row of results to the dictionary value
    
        rows_and_columns_log_message = "There are {} columns and {} rows in the 2D array.".format(len(self.column_names),len(self.database_results))
        logger.info ("Pre row-conversion 2D array is returned as: " + str(self.database_results) + "\n")
        logger.info (rows_and_columns_log_message + "\n")

    def _finalize_table(self):

        ''' Makes nested dictionary with row label as the key for the dictionary of each row, with each value keyed by column.'''

        self.final_table = {}  
        for y in range (0,len(self.row_names)):
            self.database_results[y].pop(self.column_names[0]) # use COLUMN as the key to remove the duplicate value that is now the row_name. Will always be first (i.e., leftmost) column 
            self.final_table.update ({self.row_names[y] : self.database_results[y]}) # dictionary key of row will serve as the the sub-dictionary for the rest of the row.
    
        # delete the first element of "column names" (i.e., 0,0 position of table, it has already been used for what we need above)
        self.column_names.pop(0)
    
    def _convert_die_range_to_low_and_high(self):
        """
        Takes a 2-d table array as dictionary, and adds in the high and low dice values for each row.
            
            Converts 2- into 'DiceLow': -1000, 'DiceHigh':2 -- i.e., anything 2 or lower
            Converts 12+ into 'DiceLow': 12, 'DiceHigh':1000 -- i.e., anything 12 or higher
            Converts 3-7 into 'DiceLow': 3, 'DiceHigh':7
            Converts 9 into 'DiceLow': 9, 'DiceHigh':9

        NB: Direct copy/paste from ACKS PDF gives an en-dash, not a minus sign, for the "-" character, so be sure is in properly in the SQL database.
        """

        # determine what kind of value in each row, returns true or false

        def die_is_low_range(die_range): # eg, "2-", two or lower
            
            reg_ex_string = r"\-$" # ie minus sign at end of string

            if (re.search(reg_ex_string,die_range)):
                return True
            else:
                return False        
            

        def die_is_high_range(die_range): # eg "12+", twelve or higher
            reg_ex_string = r"\+$" # ie plus sign at end of string

            if (re.search(reg_ex_string,die_range)):
                return True
            else:
                return False
        
        def die_is_mid_range(die_range): # eg "7-9", ie, between 7 and 12.
            reg_ex_string = r"\-" # ie minus sign anywhere but end (at end will have been caught already)

            if (re.search(reg_ex_string,die_range)):
                return True
            else:
                return False

        def die_is_single_digit(die_range): # e.g., 10, ie, 10 and only 10.
            
            reg_ex_string = "^(\d)+$" # ie a NUMBER of one or more digits in length, with nothing else in the string (e.g., +,-)

            if (re.search(reg_ex_string,die_range)):
                return True # note logic is reverse of the others
            else:
                return False

        # Edit the rows by adding dice ranges to the dictionary and returning the edited row
        # note all values are converted from their string form to their integer form for storage and later comparison to die rolls.

        def create_low_range_entries(row):
            die_range = row["DieRange"]
            reg_ex_string = r"\-$" # ie minus sign at end of string
            split_die_string = re.split(reg_ex_string, die_range, 1)
            
            row ["DieLow"] = -1000
            row ["DieHigh"] = int (split_die_string[0])
            return row

        def create_high_range_entries(row):
            die_range = row["DieRange"]
            reg_ex_string = r"\+$" # ie plus at end of string
            split_die_string = re.split(reg_ex_string, die_range, 1)

            row ["DieLow"] = int(split_die_string[0])
            row ["DieHigh"] = +1000
            return row

        def create_mid_range_entries(row):
            die_range = row["DieRange"]
            reg_ex_string = r"\-" # ie minus within string
            split_die_string = re.split(reg_ex_string, die_range, 1)

            row ["DieLow"] = int (split_die_string[0])
            row ["DieHigh"] = int (split_die_string[1])
            return row

        def create_single_digit_entries(row):
            row["DieRange"] = str(row["DieRange"]) 
            die_range = row["DieRange"]
            row ["DieLow"] = int(die_range) # only one number so both take its value
            row ["DieHigh"] = int(die_range)
            return row

        ### Main die range parsing routine

        for row in self.database_results:
            die_range = row["DieRange"]
            if type (die_range) != "str": die_range = str(die_range) # single digits will be read as integers, not strings, so we convert.
        
            if die_is_low_range (die_range):
                row = create_low_range_entries(row)
        
            elif die_is_high_range(die_range):
                row = create_high_range_entries(row)

            elif die_is_mid_range(die_range):
                row = create_mid_range_entries(row)
            
            elif die_is_single_digit(die_range):
                row = create_single_digit_entries(row)

            else:
                raise ValueError("The dice entry was not trapped anywhere. SQL table error?")

    def roll (self,roll):
        ''' Rolls on a table with a given number; if a DiceLow and DiceHigh field exists, then returns a value. Otherwise errors'''
        to_return={}
        for row in self.database_results:

            try:
                if roll >= row['DieLow'] and roll <= row['DieHigh']:
                    to_return = row # ie, this row was rolled.
                    break
            
            except KeyError:
                error_text = "Table {} in SQL database {} is not configured to have dice rolled on it.".format(self.table_name, self.path)
                logging.exception(error_text)
                raise KeyError (error_text)
                
            except Exception as err:
                error_text = "Table {} in SQL database {} has encountered an error.".format(self.table_name, self.path)
                logging.exception(error_text)
                raise Exception(error_text) from err
               
        if not to_return: # ie nothing has been put into to_return because no row matches
            error_text = "Nothing was found on table {} when rolling {} on it.".format(self.table_name, roll)
            logging.error(error_text)
            raise KeyError (error_text)
        
        return to_return
    
  

  ################################

def main():
    

    print ("Running main of sql_table_object_GLS.")
   
    t = RPG_table(s.TABLE_NAME_DEFAULT)
    
    print (t)
    print (t.path)
    print (t.connection)
    print (t.table_name)
    print (t.query)
    print (t.column_names)
    print (t.row_names)
    print (t.final_table)
    print (t.roll(10000))
    
    t.connection.close()
    print ("End main of sql_table_object-GLS")

if __name__ == "__main__":
    main()