# logging_tools_GLS.py
import logging
import datetime as dt

# Adopted from https://stackoverflow.com/a/35804945/1691778
# Adds a new logging method to the logging module
def addLoggingLevel(levelName, levelNum, methodName=None):
    if not methodName:
        methodName = levelName.lower()

    if hasattr(logging, levelName):
        raise AttributeError("{} already defined in logging module".format(levelName))
    if hasattr(logging, methodName):
        raise AttributeError("{} already defined in logging module".format(methodName))
    if hasattr(logging.getLoggerClass(), methodName):
        raise AttributeError("{} already defined in logger class".format(methodName))

    def logForLevel(self, message, *args, **kwargs):
        if self.isEnabledFor(levelNum):
            self._log(levelNum, message, args, **kwargs)

    def logToRoot(message, *args, **kwargs):
        logging.log(levelNum, message, *args, **kwargs)

    logging.addLevelName(levelNum, levelName)
    setattr(logging, levelName, levelNum)
    setattr(logging.getLoggerClass(), methodName, logForLevel)
    setattr(logging, methodName, logToRoot)


# Create the TRACE level
addLoggingLevel("TRACE", logging.DEBUG - 5)

logging.basicConfig(format = '%(levelname)s:\t|%(asctime)s|%(module)s|%(funcName)s|%(lineno)d - %(message)s', datefmt='%m/%d/%Y %I:%M:%S', encoding='utf-8', level=logging.TRACE,filename="logGLS.log",filemode='w')

fileHandler = logging.FileHandler ("logGLS.log")
logger_base = logging.getLogger(__name__)
logger_base.addHandler (fileHandler)

# Use the TRACE level
# logger_base.trace("A trace message")
# logger_base.debug("A debug message")
# logger_base.info("An info message")
# logger_base.warning("A warning message")
# logger_base.error("An error message")
# logger_base.critical("A critical message")

# def setup_logging():
     
#      logging.basicConfig (filename='logGLS.log',filemode ='a',level=logging.DEBUG)
#      logging.critical ("\n-----------Restart-----------")

# def start_logging():
#      start_time = dt.datetime.now().strftime("%H:%M:%S on %d/%m/%Y") # current time as string
#      logging.info ("Logging begins at " + start_time)
    
# def end_logging():
#      end_time = dt.datetime.now().strftime("%H:%M:%S on %d/%m/%Y") # current time as string
#      logging.info ("Logging ended at " + end_time + "\n\n")