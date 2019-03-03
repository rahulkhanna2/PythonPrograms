import os
from datetime import datetime
import logging

# Logger Info
if not os.path.exists("logs"):
    os.makedirs("logs")

filepath = "logs/log_" + str(datetime.now()).split(" ")[0] + ".log"
FORMAT = '%(asctime)s [%(levelname)s] %(filename)s:%(lineno)s %(funcName)s() : %(message)s'
DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
logger = logging.getLogger()
logger.setLevel(logging.INFO)

fh1 = logging.FileHandler(filepath)
fh1.setLevel(logging.DEBUG)
fh1.setFormatter(logging.Formatter(FORMAT, DATETIME_FORMAT))

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(logging.Formatter(FORMAT, DATETIME_FORMAT))

logger.addHandler(fh1)
logger.addHandler(ch)
