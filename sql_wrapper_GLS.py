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
        log.logging.error ("KeyError: Need a query or a table_name! If table_name alone passed, returns entire table. Query returns specific SQL query.")

    elif table_name and query: # ie query and a table have been passed
        log.logging.warning ("Table_name _and_ query were passed. The query supercedes the table_name, so the table name has been ignored.")

    elif not query:
        query = 'select * from ' + table_name # returns entire table. If query is passed, will use the query and ignore the table.
     
    cursor = connection.cursor()               
    cursor.execute(query)
    log.logging.debug ("A cursor object is returned:" + str(cursor))
    return cursor


def query_database(table_name=None, query=None, connection=None, path = s.PATH_DEFAULT,):
    ''' Does the entire query from connect to return whatever the search was'''

    cursor = _begin_query (query=query, connection=connection, path = path,table_name=table_name) # common beginning to get cursor
    search_result = cursor.fetchall() 
    log.logging.info ("Search result of SQL database returned as: " + str(search_result) + "for search query:" + str(query) + "\n")

    return search_result

def get_column_names (table_name=None, query = None, connection=None, path = s.PATH_DEFAULT):
    ''' Gets column names. Can be passed a connection, if not, then creates one. Path can be passed, or defaults to default in settings_GLS.py
    This will not usually be used alone, but available just to make simpler if need just column names for some reason.'''
    column_names, _ , _ = get_table_as_dict(table_name=table_name, query=query, connection=connection, path = path)

    log.logging.info ("Columns of SQL database returned from get_column_names as: " + "\n\t" + str(column_names) + "\n")

    return column_names

def get_row_names (table_name=None, query = None, connection=None, path = s.PATH_DEFAULT):
    ''' Gets row names. Can be passed a connection, if not, then creates one. Path can be passed, or defaults to default in settings_GLS.py
    This will not usually be used alone, but available just to make simpler if need just row names for some reason.'''

    _, row_names, _ = get_table_as_dict(table_name=table_name, query=query, connection=connection, path = path)
    
    log.logging.info ("Columns of SQL database returned from get_row_names as: " + "\n\t" +  str(row_names) + "\n")

    return row_names

def get_table_as_dict (table_name=None, query = None, connection=None, path = s.PATH_DEFAULT):
    
    ''' Gets entire table as dictionary. Can be passed a connection, if not, then creates one. Path can be passed, or defaults to default in settings_GLS.py
    Given this table:
       
    Col A   B   C
    X   1   2   3
    Y   4   5   6
    Z   7   8   9
    
    Returns these values in order:
        1) column_names - returns list of column names, i.e., ['A','B','C'] (note that "Col" is not returned)
        2) row_names - returns list of row names, i.e., ['X','Y','Z']
        3) dict_final = 2D dictionary with each row keyed to a subdictionary that is keyed to each column for every line

    {'X': {'A': 1, 'B': 2, 'C': 3}, 'Y': {'A': 4, 'B': 5, 'C': 6}, 'Z': {'A': 7, 'B': 8, 'C': 9}}
    
    '''

    cursor = _begin_query (table_name=table_name, query=query, connection=connection, path = path)
    
    # get column names
    
    column_names = list (map (lambda x: x[0], cursor.description))
    
    # get unedited whole table

    whole_table = cursor.fetchall()

    # Dictionary keys created for each line of the table using the columns
    result_list = [dict(zip(column_names, r)) for r in whole_table]
    log.logging.info ("Initial SQL database returned as list of dictionaries in get_table_as_dict: " + "\t\n" + str (result_list) + "\n")

    # Extract list of row names 
    row_names = []
    for x in range (0,len(result_list)):
        row_names.append(result_list[x][column_names[0]]) # (far left cell of each row, ie., the first column)

    # create 2D dictionary
    final_dict = {}  
    for y in range (0,len(row_names)):
        result_list[y].pop(column_names[0]) # use COLUMN as the key to remove the duplicate value that is now the row_name. Will always be first (i.e., leftmost) column 
        final_dict.update ({row_names[y] : result_list[y]}) # dictionary key of row will serve as the the sub-dictionary for the rest of the row.
    
    # delete the first element of "column names" (i.e., 0,0 position of table, it has already been used for what we need above)
    column_names.pop(0)

    # log
    log.logging.info ("Columns of SQL database returned as list from get_table_as_dict: " + "\n\t" + str (column_names) + "\n")
    log.logging.info ("Rows of SQL database returned as list from get_table_as_dict: " + "\n\t" + str (row_names) + "\n")
    log.logging.info ("Table of SQL database returned as 2D-Dict from get_table_as_dict: " + "\n\t" + str (final_dict) + "\n")

    # return
    return column_names,row_names, final_dict

def print_results (search_result):
    for row in search_result:
        print (row[1])

def main():
    print ("Running main of sql_wrapper_GLS.")
    log.setup_logging()
    log.start_logging
    log.logging.info ("Begin of main.")

    connect_A = connect_to_database(s.PATH_DEFAULT)
    table_name = "TestTable02"
    the_query = "SELECT * FROM TestTable02"
    
    # print (get_column_names(table_name = table_name,connection=connect_A))
    get_table_as_dict(query = the_query,connection=connect_A)
    get_row_names(query = the_query,connection=connect_A)
    get_column_names(query = the_query,connection=connect_A)
    

    connect_A.close()
    log.end_logging()
if __name__ == "__main__":
    main()