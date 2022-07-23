import logging
from dotenv import load_dotenv
import os

load_dotenv()

logpath = os.getenv('LOGPATH')
logdir = os.getenv('LOGPATH').replace(logpath.split('/')[-1], '')
formatter = logging.Formatter('[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s')

def check_if_logger_exists():
    if os.path.isfile(logpath):
        # print('File Exists...')
        pass
    else:
        print('File Does Not Exist...')
        if os.path.exists(os.path.dirname(logdir)):
            # print('Directory Exists...')
            pass
        else:
            # print('Directory Does Not Exist...')
            os.mkdir(logdir)
            # print('Directory Created...')
            with open(logpath, 'w') as f:
                f.write('Log created\n')

def setup_logger(name, log_file, level=logging.INFO):
    """To setup as many loggers as you want"""

    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger
