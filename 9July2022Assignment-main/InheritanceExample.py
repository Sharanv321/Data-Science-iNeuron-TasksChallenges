# Inheritance example
import logging
logging.basicConfig(filename="logfile1.log",level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
log = logging.getLogger("logfile1.log")


class students:
    def studentdetails(self):
        log.info("student details")

# ineuron class inherits from students class
class ineuron(students):
    def ineuronstudentdetails(self):
        log.info("ineuron student details")

# create object of the ineuron class
try:
    object1 = ineuron()
    object1.studentdetails()  #method from students class
    object1.ineuronstudentdetails() #method from ineuron class
except Exception as e:
    log.info(e)

