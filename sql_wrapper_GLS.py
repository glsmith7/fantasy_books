# sql_gls_wrapper.py

import sqlite3
import os
import logging_tools_GLS as log
import datetime
import array

def connect_to_database(path):

    if os.path.isfile(path) == False:
        log.logging.error ("Database name does not exist.")
        raise FileNotFoundError

    try:
        connection = sqlite3.connect(path)

    except OSError as err:
       
        log.logging.error ("The error" + err + " occurred.")
        return(print(f"The error '{err}' occurred"))
        raise

    else:
         log.logging.info ("SLQ connection established: " + str(connection))
         
    return connection
   
   
def retrieve_from_database(connection, query):
    if type(connection) is not sqlite3.Connection:
        log.logging.error ("There is no open connection to a database.")
        return sqlite3.DatabaseError ("There is no open connection to a database.")
    
    # if sqlite3.complete_statement(query) == False:
    #       log.logging.error ("Incomplete or improper SQL query")
    #       return sqlite3.DatabaseError ("Not a complete SQL statement?")
          
    cursor = connection.cursor()
    cursor.execute(query)
    search_result = cursor.fetchall()

    log.logging.info ("Search result of SQL database returned as: " + str(search_result) + "\n")
    return search_result

def print_SQL_results (search_result):
    for row in search_result:
        print (row[1])

def give_column_names(results):
    col_names = []
    for row in results:
        col_names.append(row[1])
    
    log.logging.info ("Column names returned as: " + str(col_names) + "\n")
    return col_names

def get_2d_array(columns, results):
    """ Returns a list with nested dictionaries. Each dictionary is a row of the table, with columns of the table as keywords
    
        j = iterates through each row
        i = iterates through each column
        columns = list containing name of each column
        results = SQL search result
    """

    for j in range (0,len(results)):
        d = {} # Empty the dictionary before each row started

        for i in range (0,len(columns)):
            d[columns[i]] = results[j][i]
        
        results[j] = d # set the row of results to the dictionary value
    
    rows_and_columns_log_message = "There are {} columns and {} rows in the 2D array.".format(len(columns),len(results))
    log.logging.info ("2D array is returned as: " + str(results) + "\n")
    log.logging.info (rows_and_columns_log_message + "\n")

    return results

def get_table_as_array(path, table_name, query = "Select * FROM(_replace_)", ): 
    """ Combines various subroutines to get a 2D array with in a single called step.
    path = path to an SQLite database.
    table_name = table name
    query = optional SQL query. If omitted, returns entire table. If query includes "_replace_", the _replace_ string will be automatically replaced with the table name."""

    dB = connect_to_database(path)
    
    # get column names
    query_column = "PRAGMA table_info({});".format(table_name)
    column_results = retrieve_from_database(dB, query_column)
    column_names = give_column_names(column_results)
    
    # replace the placeholder with tablename if it was included. Otherwise use the passed SQL query as is
    query = query.replace("_replace_",table_name)
    
    # get the full table
    
    full_table_results = retrieve_from_database(dB, query)

    # create 2D array with column names as dictionary key words
    table_as_array = get_2d_array (column_names, full_table_results)
    
    return table_as_array

def convert_die_range_to_low_and_high(d):
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
        pass

    def die_is_high_range(die_range): # eg "12+", twelve or higher
        pass
    
    def die_is_mid_range(die_range): # eg "7-9", ie, between 7 and 12.
        pass

    def die_is_single_digit(die_range): # e.g., 10, ie, 10 and only 10.
        pass

# Edit the rows by adding dice ranges to the dictionary and returning the edited row

    def create_low_range_entries(row):
        return row

    def create_high_range_entries(row):
        return row

    def create_mid_range_entries(row):
        return row

    def create_single_digit_entries(row):
        return row

### Main routine

    for row in d:
        die_range = row["DieRange"]
    
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
       
     
        # if row ['DieRange'] == "2-":
        #     print (row)
        #     row['DieLow'] = -1000
        #     row['DieLhigh'] = 2
        #     print (row)
        
    return d

def main():
     log.setup_logging()
     log.start_logging()
     print ("Begin main.")

     path = "./SQLite_db/ACKS_SQL_01.db3"
     table_as_array = (get_table_as_array(path,"Surprise",query="SELECT * FROM '_replace_'"))
     final_dictionary = (convert_die_range_to_low_and_high(table_as_array))
     
     print (final_dictionary)

     print ("End of program")
     log.end_logging()
 
if __name__ == "__main__":
    main()

