
import logging
# gives back a log structure diagram
from logging_tree import printout


def default_logger():
    logging.basicConfig(level=logging.DEBUG)
    if logging.root.level == 10:
        print("da isses")
    logging.debug("hello")
    printout()
    

def my_logger():
    # create my own logger
    logger = logging.getLogger(__name__)
    # define handlers
    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler("mylog.log", mode= "a", encoding="utf-8")
    syslog_handler = logging.handlers.SysLogHandler(address=("10.10.2.15", 514))
    # add logger 
    logger.addHandler(console_handler)
    console_handler.setLevel("DEBUG")
    logger.addHandler(file_handler)
    logger.addHandler(syslog_handler)
    # add formater
    formatter = logging.Formatter("{asctime}, - {levelname}, - {message}",
                                  style="{",
                                    datefmt="%Y-%m-%d %H:%M")
    console_handler.setFormatter(formatter)
    syslog_handler.setFormatter(formatter)
    return logger
    


if __name__ == "__main__":
    my_logger = my_logger()
    my_logger.warning("oh my god a warning")
    my_logger.info("oh my god a Info")
    
    

    print(f"log level is: {my_logger.getEffectiveLevel()}")
    # main logger - no handler can go beyond that level
    my_logger.setLevel("INFO")
    my_logger.info("oh my god a Info")
    my_logger.debug("oh my god a debug")
    print(f"log level is: {my_logger.getEffectiveLevel()}")
    # information about the hanlder
    #print(my_logger.handlers)
    printout()