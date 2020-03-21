import datetime 
import time 
import calendar
td = time.time()
date = datetime.date.today()
print (date, td)
print ("Year", date.year)
print ("Month", date.month)
print ("Weekday", date.weekday())
tdelta = datetime.timedelta(days = 5)
print ('Current date-5days',date-tdelta)
tdelta = datetime.timedelta(seconds = 5)
print (date+tdelta)
dt = datetime.datetime(2020, 3, 21, 12, 42, 50)
delta = datetime.timedelta(seconds = 5)
print ('Current time+5secs', dt + delta)