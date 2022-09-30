# protected members can be accessed within the class and in the inherited classes
# protected members are defined by single underscore
import logging
logging.basicConfig(filename="logfile1.log",level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
log = logging.getLogger("logfile1.log")

class Students3:
    _pv3 = "this is a protected variable1"

    def StudentDetails3(self):
        log.info(Students3._pv1)

    def _protectedmethod3(self):
        log.info("This is a protected method")

# access protected members inside a class**********
    log.info("access protected members inside a class**********")
    try:
        log.info(_pv3)
        _protectedmethod3("dfdf")
    except Exception as e:
        log.info(e)

# access protected members outside a class
log.info("We are accessing protected memeber outside a class **********")
try:
    object1 = Students3()
    log.info(object1._pv3)
    log.info(object1._protectedmethod3())
except Exception as e:
    log.info(e)

# access protected members in inherited class
log.info("access protected members in inherited class***************")
try:
    class newstudents(Students3):
        log.info(Students3._pv3)
        Students3._protectedmethod3("dfdf")
except Exception as e:
    log.info(e)





