import logging
import colorlog as log

def main():
    log.basicConfig (filename='logGLS.log',filemode ='a',level=logging.DEBUG)
    log.debug("debug")
    log.info("info")
    log.warning("warning")
    log.error("error")
    log.critical("critical")
    log.error("This is wrong and silly")

if __name__ == "__main__":
    main()
    
    