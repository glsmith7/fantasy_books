# logging_tools_GLS.py
import logging
import datetime as dt

def setup_logging():
     
     logging.basicConfig (filename='logGLS.log',filemode ='a',level=logging.DEBUG)
     logging.critical ("\n\n-----------Restart-----------")
     
def start_logging():
     start_time = dt.datetime.now().strftime("%H:%M:%S on %d/%m/%Y") # current time as string
     logging.info ("Logging begins at " + start_time)
    
def end_logging():
     end_time = dt.datetime.now().strftime("%H:%M:%S on %d/%m/%Y") # current time as string
     logging.info ("Logging ended at " + end_time)