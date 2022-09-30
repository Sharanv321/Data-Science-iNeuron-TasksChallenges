# Q7 write a code to get a time of your system

import datetime
import time

# method 1
print(datetime.datetime.now())
print(datetime.datetime.now().hour)
print(datetime.datetime.now().minute)
print(datetime.datetime.now().second)

# method 2
print(time.ctime())
