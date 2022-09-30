# Multi level inheritance
import logging
logging.basicConfig(filename="logfile1.log",level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
log = logging.getLogger("logfile1.log")


class students:
    def students_course(self):
        log.info("student courses")


class ineuron1students:
    def ineuron1_students_course(self):
        log.info("ineuron1 student courses")

# class ineuron2students is inheriting from both classes students, ineuron1students
class ineuron2students(students, ineuron1students):
    def ineuron2_students_course(self):
        log.info("ineuron2 student courses")

try:
    obj1 = ineuron2students()
    obj1.students_course()
    obj1.ineuron1_students_course()
    obj1.ineuron2_students_course()
except Exception as e:
    log.info(e)