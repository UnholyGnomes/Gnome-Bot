import logging
from dotenv import load_dotenv
import os

load_dotenv()

logpath = os.getenv('LOGPATH')
formatter = logging.Formatter('[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s')

def setup_logger(name, log_file, level=logging.INFO):
    """To setup as many loggers as you want"""

    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger
