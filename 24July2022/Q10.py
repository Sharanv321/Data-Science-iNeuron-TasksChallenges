# write a code to trigger alarm for you at scheduled time

import datetime

import time

import playsound

x = datetime.datetime.now()
print(x)

alarm_time = input("Enter the time of alarm to be set:HH:MM:SS AM/PM\n")

s = "The Insightful Coder"
print(s[4:11])

# obtaining the hour
alarm_hour = alarm_time[0:2]
print(type(alarm_hour))

# obtaining the minute
alarm_minute = alarm_time[3:5]
print(type(alarm_minute))

# obtaining the second
alarm_seconds = alarm_time[6:8]
print(type(alarm_seconds))

# obtaining the period
alarm_period = alarm_time[9:11]
print(type(alarm_period))

print(alarm_hour)
print(alarm_minute)
print(alarm_seconds)
print(alarm_period)

print("*****************************")

print(datetime.datetime.now().hour)
print(datetime.datetime.now().minute)
print(datetime.datetime.now().second)
print(datetime.datetime.now().astimezone)

print("*****************************")

print("Alarm Set!")

while True:

    current_hour = str(datetime.datetime.now().hour)
    current_minute = str(datetime.datetime.now().minute)
    current_seconds = str(datetime.datetime.now().second)

    if (alarm_hour == current_hour and alarm_minute == current_minute and alarm_seconds == current_seconds):
        print("Wake Up!")
        playsound('/path/to/a/sound/file/you/want/to/play.mp3')

    break