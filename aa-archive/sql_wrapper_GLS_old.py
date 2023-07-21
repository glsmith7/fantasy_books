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
          
    cursor = connection.cursor()
    cursor.execute(query)
    search_result = cursor.fetchall()

    log.logging.info ("Search result of SQL database returned as: " + str(search_result) + "\n")
    return search_result

def print_SQL_results (search_result):
    for row in search_result:
        print (row[1])

def main():
    print ("Running main of sql_wrapper_GLS.")
 
if __name__ == "__main__":
    main()
