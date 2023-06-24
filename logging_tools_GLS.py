# logging_tools_GLS.py
import logging
import datetime as dt
import os


ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__)))

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