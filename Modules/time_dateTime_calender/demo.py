# importing the time , datetime , calendar modules

# import calendar

# c = calendar.isleap(2024) # True

# c = calendar.isleap(2026) # False

# print(c)

# -------------------------------------------------------------------------------------------------------------

# c = calendar.leapdays(2000 , 2026) # it will be take the range of the years and it will be return the numbers of leap years in integers

# print(c)

# -------------------------------------------------------------------------------------------------------------

# c = calendar.monthcalendar(2026 , 2) # it will be return the lists of the days which can be entering by users

# print(c)

# -------------------------------------------------------------------------------------------------------------

# year = int(input("\nEnter the Year : "))

# month = int(input("\nEnter the Month : "))

# print()

# c = calendar.month(year , month) # it will be take the year and month value from the user's and return the month's calendar

# print(c)

# -------------------------------------------------------------------------------------------------------------

# year = int(input("\nEnter the Year : "))

# space = int(input("\nEnter the Space Between Days : ")) # it will be give the space between the year's months' days

# c = calendar.calendar(year , space) # it will be take the value of year from the user and return the whole year calender

# print(c)

# -------------------------------------------------------------------------------------------------------------

# import datetime

# d = datetime.datetime.now() # it will be give the current time with fractional seconds and day - month - year

# -------------------------------------------------------------------------------------------------------------

# d = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") # formating date time will be set here

# -------------------------------------------------------------------------------------------------------------

# d = datetime.datetime.today() # it will be the same as now() function

# -------------------------------------------------------------------------------------------------------------

# d = datetime.datetime(2026 , 2 , 6 , 2 , 59 , 30 , 12345) # as per the argument we are getting the date time

# print(d)

# print(d.year)

# print(d.month)

# print(d.day)

# print(d.hour)

# print(d.minute)

# print(d.second)

# print(d.microsecond)

# -------------------------------------------------------------------------------------------------------------

# import time

# t = time.time() # epoch time return

# -------------------------------------------------------------------------------------------------------------

# t = time.ctime() # formatting like day month day datetime

# -------------------------------------------------------------------------------------------------------------

# t = time.localtime() # it will be returning the structure of the time

# -------------------------------------------------------------------------------------------------------------

# for i in range(10) :
#     time.sleep(2) # for 2 seconds delay the work perfromance and then it will be retrun
#     print(i)

# -------------------------------------------------------------------------------------------------------------

import datetime

from datetime import timedelta

today = datetime.datetime.now()

future_days = today + timedelta(days = 365) # it will be adding more 365 days to the current days and it will be return the current and future days

print("\nCurrent Day :",today)

print("\nFuture Days :",future_days)