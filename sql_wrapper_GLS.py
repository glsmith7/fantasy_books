# sql_gls_wrapper.py

import sqlite3
import os
import logging_tools_GLS as log
import datetime

def connect_to_database(path):

   if os.path.exists(path) == False:
        log.logging.error ("Database name does not exist.")
        return FileNotFoundError

   try:
     connection = sqlite3.connect(path)
     log.logging.info ("SLQ connection established: " + str(connection))
     return connection
   
   except OSError as err:
       
       log.logging.error ("The error" + err + " occurred.")
       return(print(f"The error '{err}' occurred"))
   

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

def print_search_results(search_result):
    for row in search_result:
        print (row)

def main():
     log.setup_logging()
     log.start_logging()
     print ("Begin main.")
     
     print ("End of program")
     log.end_logging()
 
if __name__ == "__main__":
    main()

