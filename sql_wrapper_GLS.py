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
    return search_result

def give_column_names(results):
    col_names = []
    for row in results:
        col_names.append(row[1])
    
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
    
    return results

def get_table_as_array(path, table_name, query = "Select * FROM(_replace_)", ): 
    """ Combines various subroutines to get a 2D array in a single called step.
    path = path to an SQLite database."""

    dB = connect_to_database(path)
    
    # get column names
    query_column = "PRAGMA table_info({});".format(table_name)
    column_results = retrieve_from_database(dB, query_column)
    column_names = give_column_names(column_results)
    
    # get the full table
    query = query.replace("_replace_",table_name)
    query_full_table = query
    full_table_results = retrieve_from_database(dB, query_full_table)

    # create 2D array with column names as dictionary key words
    final_array = get_2d_array (column_names, full_table_results)
    
    return final_array


def print_search_results(search_result):
    for row in search_result:
        print (row[1])

def main():
     log.setup_logging()
     log.start_logging()
     print ("Begin main.")

     path = "./SQLite_db/trialSQL.db3"
     print (get_table_as_array(path,"TestTable01",query="SELECT * FROM '_replace_' WHERE TestUniqueID = 1"))

     print ("End of program")
     log.end_logging()
 
if __name__ == "__main__":
    main()

