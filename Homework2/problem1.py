import datetime 

tday  = datetime.datetime.today()
print ('Current date: ', tday)
num_y = int(input('Given years: '))
num_d = int(input('Given days: '))
ydelta = datetime.timedelta(days = num_y*365)
ddelta = datetime.timedelta(days = num_d)
print ('Final date: ', tday +ydelta + ddelta)