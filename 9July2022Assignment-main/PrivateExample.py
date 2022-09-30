# private variable and private methods
# in the below example private variable, private method can be accessed only inside the class.
# private variable, private method cannot be accessed outside the class.
import logging
logging.basicConfig(filename="logfile1.log",level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
log = logging.getLogger("logfile1.log")

class Students:

    __pv1 = "this is a private variable1"

    def StudentDetails(self):
        log.info(Students.__pv1)

    def __Privatemethod1(self):
        log.info("This is a private method")

# access private variable inside a class


# access private method inside a class
    __Privatemethod1("dfdf")

try:
    object1 = Students()
except Exception as e:
    log.info(e)

# access private variable from the public method, but not directly
try:
    log.info(object1.StudentDetails())
except Exception as e:
    log.info(e)




