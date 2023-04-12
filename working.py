# working.py
import sql_wrapper_GLS as sql
import logging_tools_GLS as log

def main():
     log.setup_logging()
     log.start_logging()
     print ("Begin main.")
     db = sql.connect_to_database ("testSQL.db3")
     print (sql.sqlretrieve_from_database(db,"B"))
     print ("End of program")
     db.close()
     log.end_logging()
 
if __name__ == "__main__":
    main()