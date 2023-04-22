import sqlite3
import os
import logging_tools_GLS as log
import datetime
import array

import settings_GLS as s

class SQL_object_GLS:
          
    def __init__ (self, path = s.PATH_DEFAULT):
       
        self.path = path
        self.connect_to_database(self.path)

    def connect_to_database(self,path):
        
        if os.path.isfile(path) == False:
            log.logging.error ("Database name does not exist.")
            raise FileNotFoundError

        try:
            self.connection = sqlite3.connect(path)

        except OSError as err:
       
            log.logging.error ("The error" + err + " occurred.")
            return(print(f"The error '{err}' occurred"))
            raise

        else:
             log.logging.info ("SLQ connection established: " + str(self.connection))
    
    
    
  
class RPG_table(SQL_object_GLS):

    def __init__ (self,table_name,query = s.SQL_QUERY_DEFAULT):
        super().__init__()

        self.table_name = table_name
        self.query = query
        self.query = self.query.replace("_replace_",self.table_name)
        self.retrieve_from_database()
        self.give_column_names()

    
    
    def retrieve_from_database(self):
        
        if type(self.connection) is not sqlite3.Connection:
            log.logging.error ("There is no open connection to a database.")
            return sqlite3.DatabaseError ("There is no open connection to a database.")
          
        cursor = self.connection.cursor()
        cursor.execute(self.query)
        self.database_results = cursor.fetchall()

        log.logging.info ("Search result of SQL database returned as: " + str(self.database_results) + "\n")

    
    def give_column_names(self):
        self.column_names = []
        for row in self.database_results:
            self.column_names.append(row[1])
    
        log.logging.info ("Column names returned as: " + str(self.column_names) + "\n")

    
  ################################

def main():
    print ("Running main of sql_table_object_GLS.")
    o = SQL_object_GLS()
    print (o)
    print (o.path)
    print (o.connection)

    t = RPG_table("TestTable01")
    print (t)
    print (t.path)
    print (t.connection)
    print (t.table_name)
    print (t.query)
    print (t.column_names)
    print (t.database_results)
    

    print ("End main of sql_table_object-GLS")
 
if __name__ == "__main__":
    main()