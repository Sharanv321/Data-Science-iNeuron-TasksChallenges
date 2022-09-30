#module example

import Dir1.module1

try:
    Dir1.module1.function1()
except Exception as e:
    log.info(e)