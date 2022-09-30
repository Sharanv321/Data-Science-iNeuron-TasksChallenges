# package example

import logging
logging.basicConfig(filename="logfile1.log",level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
log = logging.getLogger("logfile1.log")

import datetime

class Package():
    try:
        log.info(datetime.date.today())
    except Exception as e:
        log.info(e)