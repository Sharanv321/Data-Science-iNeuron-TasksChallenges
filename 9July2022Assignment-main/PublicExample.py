# public variables and methods can be accessed inside and outside a class definition
import logging
logging.basicConfig(filename="logfile1.log",level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
log = logging.getLogger("logfile1.log")

class Students2:
    pv3 = "this is a public variable"

    def StudentDetails2(self):
        log.info("public method")

# access public variable and method inside a class
    try:
        log.info(pv3)
        StudentDetails2("dddd")
    except Exception as e:
        log.info(e)

# access public variable and method outside a class
log.info("access outside the class")

try:
    object1 = Students2()
    log.info(object1.pv3)
    log.info(object1.StudentDetails2())
except Exception as e:
    log.info(e)





