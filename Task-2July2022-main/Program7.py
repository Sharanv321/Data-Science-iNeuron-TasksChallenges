# 7 . Try to extract all the value element form dict available in list
import logging
logging.basicConfig(filename="logfile1.log",level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')

class Program4:

    log = logging.getLogger("logfile1.log")
    # Declare a list
    try:
        l = [3, 4, 5, 6, 7, [23, 456, 67, 8, 78, 78], [345, 56, 87, 8, 98, 9], (234, 6657, 6),
         {"key1": "sudh", 234: [23, 45, 656]}]

    except Exception as e:
        log.info(e)

    # Try to extract all the value element form dict available in list
    log.info("Try to extract all the value element form dict available in list")
    log.info(l[-1].values())