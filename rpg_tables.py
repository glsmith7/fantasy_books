import copy as copy
import d20 as d20
import datetime as dt
import numpy as np
import os as os
import pandas
import random as random
import re as regex
import sqlite3 as sqlite3
import string as string

# logging boilerplate
import settings_GLS as s
import logging
import logging_tools_GLS
logger = logging.getLogger(__name__)

#########################################################

class RPG_table ():

    def __init__ (self, table_name, path = s.PATH_DEFAULT):
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

        self.display_all = self.df.to_string()

    def madlib (self, n=1, replace=False):
        ''' returns random value(s) from the "Result" column. Defaults to a single result, but n=X can be set to choose any number. '''
        ''' if replace = True, the same name can be picked more than once. In that case, n cannot be greater than the total number of rows in the list (and if n > than that is pased, it will be set to the number of entries. If replace is True, then as many names as one wishes can be drawn, but there will be duplicates.)'''
        if replace == False:
             if n > len(self.df): n = len(self.df)
        
        rand_result = self.df.sample(n=n, replace=replace) # replace = True lets a given name be chosen more than once.
        return_list = []
        
        if n==1:
             return_list = rand_result.iat[0,0] # get it out of a list for easier use

        else: 
            for i in range (0,n):
                return_list.append(rand_result.iat[i,0])
        
        return return_list
    
    def roll (self,roll):
        ''' Rolls on a table with a given number; if a DiceLow and DiceHigh field exists, then returns a value. Otherwise errors'''
        to_return={}
        
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
            logger.info ("SLQ connection established: " + str(connection))
            return connection

def what_dice_to_roll(table, path = s.PATH_DEFAULT) -> list:
    ''' table is name of the table to roll on in the master table "aaDiceTypeToRoll".
    Returns the dice rolling string for a given table.'''

    conn = connect_to_database(path)
    query = "select DiceFormula from aaDiceTypeToRoll where TableName like '{}'".format(table)
    
    if type(conn) is not sqlite3.Connection:
            logger.error ("There is no open connection to a database.")
            raise sqlite3.DatabaseError ("There is no open connection to a database.")
    
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    logger.info ("Search result of SQL database returned as: " + str(results) + "\n")
    conn.close()
    return results[0][0] # returns a plain dice string

##############################
# main


# g = RPG_table(table_name="_names_anglo_saxon_female")
print (RPG_table(table_name="_names_anglo_saxon_female").madlib(1))














