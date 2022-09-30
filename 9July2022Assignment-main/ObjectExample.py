# Object example

import logging
logging.basicConfig(filename="logfile1.log",level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
log = logging.getLogger("logfile1.log")

from datetime import date
cyear = date.today().year

class Student:
    def __init__(self, student_name, student_address, student_dob):
        self.student_name = student_name,
        self.student_address = student_address,
        self.student_dob = student_dob


# create object of the class
try:
    std1 = Student("abc","address1",1985)
except Exception as e:
    log.info(e)

log.info(std1.student_name)
log.info(std1.student_address)
log.info(std1.student_dob)



