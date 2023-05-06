# sql_gls_wrapper.py

import sqlite3
import os
import logging_tools_GLS as log
import datetime
import array
import settings_GLS as s

def connect_to_database(path=s.PATH_DEFAULT):
    ''' Returns an SQL connection object. If not path passed, uses default.'''

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
         log.logging.info ("SQL connection established: " + str(connection))
         
    print (type(connection))
    return connection
   
def _begin_query(table_name=None, query=None, connection=None, path = s.PATH_DEFAULT): 
    ''' Returns a cursor with a query
    If connection not passed, the path creates connection.
    If path not passed, uses default path.

    NB: Must pass either a query OR the table name.   
    If table_name alone passed, returns entire table. Query returns specific SQL query.

    This routine is used by multiple methods to return the SQL cursor whose data is then manipulated.
    '''

    if not connection:
        connection = connect_to_database(path)

    if type(connection) is not sqlite3.Connection:
        log.logging.error ("There is no open connection to a database.")
        return sqlite3.DatabaseError ("There is no open connection to a database.")

    if not table_name and not query:
        raise KeyError ("Need a query or a table_name! If table_name alone passed, returns entire table. Query returns specific SQL query.")
    
    elif table_name and query: # ie query and a table have been passed
        log.logging.warning ("Table_name _and_ query were passed. The query supercedes the table_name, so the table name has been ignored.")

    elif not query:
        query = 'select * from ' + table_name # returns entire table. If query is passed, will use the query and ignore the table.
     
    cursor = connection.cursor()               
    cursor.execute(query)
    return cursor


def query_database(table_name=None, query=None, connection=None, path = s.PATH_DEFAULT,):

    cursor = _begin_query (query=query, connection=connection, path = path,table_name=table_name) # common beginning to get cursor
    search_result = cursor.fetchall() 
    cursor.close()
    log.logging.info ("Search result of SQL database returned as: " + str(search_result) + "\n")
    
    return search_result

def get_column_names (table_name=None, query = None, connection=None, path = s.PATH_DEFAULT):
    ''' Gets column names. Can be passed a connection, if not, then creates one. Path can be passed, or defaults to default in settings_GLS.py'''

    cursor = _begin_query (table_name=table_name, query=query, path = path, connection = connection, ) # common beginning to get cursor
    column_names = list (map (lambda x: x[0], cursor.description))
    cursor.close()
    log.logging.info ("Columns of SQL database returned as: " + str(column_names) + "\n")

    return column_names

def print_results (search_result):
    for row in search_result:
        print (row[1])

def main():
    print ("Running main of sql_wrapper_GLS.")
    connect_A = connect_to_database(s.PATH_DEFAULT)
    table_name = "MercenaryTableRealms"
    the_query = "SELECT * FROM MercenaryTableRealms WHERE Race LIKE '%Kobold%'"
    
    print (get_column_names(table_name = table_name))
    print("----")
    print (query_database(query = the_query))

if __name__ == "__main__":
    main()

