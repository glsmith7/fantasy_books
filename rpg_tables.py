import d20 as d20
import os as os
import pandas
import random as random
import sqlite3 as sqlite3
import string as string

# logging boilerplate
import settings_GLS as s
import logging
import logging_tools_GLS
logger = logging.getLogger(__name__)
#########################################################
class LookUpTable(): 
    
    def __init__ (self,query,path=s.PATH_DEFAULT):

        self.path = path
        self.conn = connect_to_database(self.path)
        self.query = query
        self.df = pandas.read_sql_query(self.query, self.conn)
        self.result = self.df.iat[0,0]
        self.conn.close()

class RPG_table ():
    
    def __init__ (self, table_name, path = s.PATH_DEFAULT):
        ''' Opens an SQL database, returns the full value of a table therein, and also creates "DieLow" and "DieHigh" columns for tables with a "DieRange" column. 
        Each RPG_table has the following attributes:

        .df - Pandas dataframe
        .table_name - the SQL table used to create
        .self_path - path to the SQL database
        .num_rows - number of rows (not counting labels)
        .num_columns (not counting labels)
        .row_labels - List of the row labels
        .column_labels - List of the column labels
        .description - for single tables, the table_name. If table has been created by adding two or more RPG_table objects together, the description describes the combination.
        .display_all - a text list of the entire table (equivalent to calling RPG_table.df.string())

        '''
    
        self.path = path
        self.table_name = table_name
        self.conn = connect_to_database(self.path)
        self.query = "SELECT * from {}".format(self.table_name)
        self.df = pandas.read_sql_query(self.query, self.conn)
        self.conn.close()
    
        if "DieRange" in (self.df.columns):
             for row in self.df.index:
                  cell = self.df.at[row,'DieRange']
                  if cell[-1] == "-":
                       self.df.at[row,'DieLow'] = -1000 # a value or lower
                       self.df.at[row,'DieHigh'] = cell[:-1]
                  elif cell[-1] == "+":
                       self.df.at[row,'DieLow'] = cell[:-1] # a value or higher
                       self.df.at[row,'DieHigh'] = 1000
                  elif "-" in cell:
                       split_values = cell.split("-") # two values with a dash between
                       self.df.at[row,'DieLow'] = split_values[0] 
                       self.df.at[row,'DieHigh'] = split_values[1]
                  else:
                       self.df.at[row,'DieLow'] = cell # no dash, single value
                       self.df.at[row,'DieHigh'] = cell

        self.num_rows = self.df.shape[0]
        self.num_columns = self.df.shape[1]
        self.row_labels = list(self.df.index)
        self.column_labels = list (self.df.columns)
        self.description = self.table_name
        self.display_all = self.df.to_string()
        logger.debug ("RPG_table: _" + (self.description) + "_ providing: " + "\n" + self.display_all + "\n")

    def __add__ (self, the_other):
        """ Places the values for the second table below the values for first table, and renumbers the row numbers so that this can happen. """

        first_num_rows = self.num_rows
        second_num_rows = the_other.num_rows

        # for i in range (first_num_rows,(first_num_rows+second_num_rows)): # creates dictionary of second table to renumber the rows so can be added at bottom of rist table
        #      renumber_rows[i-first_num_rows] = (i)

        first_descript = self.description
        second_descript= the_other.description
        
        logger.debug ("RPG_table: " + (str(first_descript) + " combining with: " + second_descript ))

        first_df = self.df
        second_df = the_other.df
        logger.debug ("First DataForm: _" + str(self.description) + "_ providing: " + "\n" + self.display_all + "\n")
        logger.debug ("Second DataForm: _" + str(the_other.description) + "_ providing: " + "\n" + the_other.display_all + "\n")
        

        _ = RPG_table(table_name=self.table_name, path=self.path)
    
        _.df = pandas.concat([second_df, first_df], ignore_index=True)

        _.description = first_descript + " COMBINED WITH " + second_descript # description used, not table name, since if calling multiple additions \
                                                                             # need table_name to still work as individual table in the SQL database
        _.num_rows = _.df.shape[0]
        _.num_columns = _.df.shape[1]
        _.row_labels = list(_.df.index)
        _.column_labels = list (_.df.columns)
        _.display_all = _.df.to_string()
        logger.debug ("Composite table: _" + str(_.description) + "_ providing: " + "\n" + _.display_all + "\n\n")

        return _
    
    def madlib (self, n=1, replace=False):
        ''' returns random value(s) from the "Result" column. Defaults to a single result, but n=X can be set to any number. 
        If n=1, returns a single value. 
        If n>1, returns a list of values.
        If replace = True, the same row can be picked more than once. 
        If replace = False, n cannot be greater than the total number of rows in the list (and if an n > than that is passed, n will be set to the maximum number of entries).
        If replace = True, then n cab be as many rows as one wishes, but there will be duplicates.
        '''

        if replace == False:
             if n > len(self.df): n = len(self.df)
        
        rand_result = self.df.sample(n=n, replace=replace) # replace = True lets a given name be chosen more than once.
        return_list = []
        
        if n==1:
             return_list = rand_result.iat[0,0] # get it out of a list for easier use
             logger.debug ("Single madlib value called on RPG_table OBJECT _" + (self.description) + "_ returned: " + str(return_list))
        else: 
            for i in range (0,n):
                return_list.append(rand_result.iat[i,0])
                logger.debug ("Multiple madlib values called on RPG_table OBJECT _" + (self.description) + "_ returned: " + str(return_list))

        return return_list
    
    def roll (self,roll=None):
        ''' Rolls on a table with a given number; if a DiceLow and DiceHigh field exists, then returns a value. Otherwise errors.
        Can pass a roll value as roll = X. If no roll value is passed, uses the function _what_dice_to_roll to look up the self.table_name on the master table "aaDiceTypeToRoll", rolls that value, and then returns the value rolled.
        Thus, for RPG_table 'a':
            a.roll() --> looks up what dice should be rolled on table a, rolls, and returns value.
            a.roll(5) --> looks up the value for 5 on table a, and returns it.
            a.roll("1d6") --> rolls 1d6, looks up the result on table a, and returns it.
        
        '''

        to_return={}
        if not roll:
             dice_string = what_dice_to_roll(table_name=self.table_name)
             roll = d20.roll(dice_string).total

        for row in self.df.index:
            low = int(self.df.at[row,'DieLow'])
            high = int(self.df.at[row,'DieHigh'])

            try:
                if roll >= low and roll <= high:
                    to_return = self.df.at[row,'Result'] # ie, this row was rolled.
                    break
            except KeyError:
                error_text = "Table {} in SQL database {} is not configured to have dice rolled on it.".format(self.table_name, self.path)
                logging.exception(error_text)
                raise KeyError (error_text)
                
            except Exception as err:
                error_text = "Table {} in SQL database {} has encountered an error.".format(self.table_name, self.path)
                logging.exception(error_text)
                raise Exception(error_text) from err
               
        if to_return == 0: return 0 # note if rolls value of 0, this will be interpreted as "not to_return" below even though 0 =! {}

        if not to_return: # ie nothing has been put into to_return because no row matches
            error_text = "Nothing was found on table {} when rolling {} on it.".format(self.table_name, roll) 
            logging.error(error_text)
            raise KeyError (error_text)
        
        return to_return


############################# FUNCTIONS

def connect_to_database(path):

    if os.path.isfile(path) == False:
        logger.error ("Database name does not exist.")
        raise FileNotFoundError

    try:
        connection = sqlite3.connect(path)

    except OSError as err:

        logger.error ("The error" + err + " occurred.")
        return(print(f"The error '{err}' occurred"))
        raise

    else:
            logger.debug ("SLQ connection established: " + str(connection))
            return connection

def madlib(table_name, path = s.PATH_DEFAULT):
     ''' Returns a single value from a table whose title is passed. A shortcut function to avoid having to use the whole OOP technique when a single random value is
     all that is needed. Eg, x = madlib("TableName")'''
     value = (RPG_table(table_name=table_name, path=path).madlib(1))
     logger.debug ("Madlib value from FUNCTION returned: " + str(value))
     return value

def what_dice_to_roll(table_name, path = s.PATH_DEFAULT):
    ''' table is name of the table to roll on in the master table "aaDiceTypeToRoll".
    Returns the dice rolling string for a given table.'''
    conn = connect_to_database(path)
    query = "select DiceFormula from aaDiceTypeToRoll where TableName like '{}'".format(table_name)
    
    if type(conn) is not sqlite3.Connection:
            logger.error ("There is no open connection to a database.")
            raise sqlite3.DatabaseError ("There is no open connection to a database.")
    
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    logger.debug ("Search result of SQL database returned as: " + str(results))
    conn.close()
    return results[0][0] # returns a plain dice string
    

##############################
# main

if __name__ == "__main__":
    g=RPG_table("ReactionRollStandard")
    h=RPG_table("ReactionRollStandard")

    i=g+h
    print (i.display_all)
    print (i.madlib())
    print (i.madlib(2))
    print (madlib("ReactionRollStandard"))