# class Example
import logging
logging.basicConfig(filename="logfile1.log",level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
log = logging.getLogger("logfile1.log")

from datetime import datetime
class Student:
    def __init__(self, student_name, student_address, student_dob):
        self.student_name = student_name,
        self.student_address = student_address,
        self.student_dob = student_dob

    def student_age(dob):
        log.info("student age is ",datetime-dob)