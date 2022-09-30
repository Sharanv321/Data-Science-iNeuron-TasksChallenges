# Encapsulation
import logging
logging.basicConfig(filename="logfile1.log",level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
log = logging.getLogger("logfile1.log")

class ineuron:
    def __init__(self):
        self.__course = "Python"

    def courses(self):
        log.info(self.__course)

    def course_change(self, new):
        self.__course = new

obj1 = ineuron()
#print(obj1.course)

try:
    obj1.__course = "java"
    obj1.courses()

    obj1.course_change("sql")
    obj1.courses()

except Exception as e:
    log.info(e)
