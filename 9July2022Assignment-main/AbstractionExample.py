# Abstraction
import logging
logging.basicConfig(filename="logfile1.log",level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
log = logging.getLogger("logfile1.log")

class ineuron:
    __courses = "course variable"

    def coursedetails(self):
        print(ineuron.__courses)

i = ineuron()
# __courses cannot be accessed.
# __courses can be accessed outside class only through function  coursedetails(self)
# this process is called Abstraction

try:
    log.info(i.coursedetails())
except Exception as e:
    log.info(e)