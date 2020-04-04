import datetime 
import time
import calendar
bday = datetime.date(1995, 2, 21)
print('My birthday: ', bday)
print ('Year: ', bday.year)
print ('Month: ', bday.month)
print ('Day: ', bday.day)
print ('Weekday: ', bday.isoweekday())
next_bday = datetime.date(2021, 2, 21)
today = datetime.date.today()
till_bday = next_bday - today
print ('Until my next birthday: ', till_bday)
cal = calendar.month(2017, 5)
print (cal)
today = datetime.date.today()
a_day = datetime.timedelta(days = 1)
yesterday = today - a_day
print('Yesterday', yesterday)
current_time = time.asctime()
print('Current time : ', current_time)
ndelta = datetime.timedelta(days = 2)
print('Yesterday + 2 days: ', yesterday + ndelta)
pdelta = datetime.timedelta(days = 3)
print('Yesterday - 3 days: ', yesterday - pdelta)