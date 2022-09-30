# method overriding example
import logging
logging.basicConfig(filename="logfile1.log",level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
log = logging.getLogger("logfile1.log")

class courses:
    def coursefee(self):
        log.info("course fee details")

    def coursename(self):
        log.info("course name details")

class ineuron(courses):
    def coursefee(self):
        log.info("ineuron course fee details")

try:
    object1 = ineuron()
    # here the method coursefee() is overriding
    object1.coursefee()
except Exception as e:
    log.info(e)