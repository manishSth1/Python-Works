import datetime   # python executable -> lib folder -> site-packages
todays_date = datetime.date.today()    # gives date
print(todays_date)

print(datetime.MINYEAR)  # -> 1        # The datetime module exports these constants
print(datetime.MAXYEAR)  # -> 9999

time_now = datetime.datetime.now()     # need date first to get time, can't do "time"
print(time_now)

from datetime import datetime, date    # easier to use

print(datetime.now())                  # no need of "datetime" two times as we already imported
print(date.today())

date_1 = date(1997, 4, 2)              # April 2, 1997 -> Let's say date of birth
date_2 = date.today()                  # gives date for today
diff = date_2 - date_1 
print(diff)                            # gives the diff -> 9282 days, 0:00:00
print(diff.total_seconds())            # gives diff in seconds -> 801964800.0    | use .totalseconds()

"""
The datetime.time class accepts hour, minute, second, microsecond, tzinfo (optional)
parameters that has default values of 0. the datetime.time class creates time object.
"""
from datetime import time              # import time

time1 = time(hour=5)    # 05:00:00
time2 = time(hour=5, minute=50) # 05:50:00
time3 = time(hour=5, minute=50, second=30)  # 05:50:30
time4 = time(hour=5, minute=50, second=30, microsecond=100)  # 05:50:30.000100
print(time1)
print(time2)
print(time3)
print(time4)

'''
We can subtract one date or datetime instance from
another date or datetime instance to get the time
difference as timedelta instance.
'''
date_1 = date(1999, 12, 31)
date_2 = date(1999, 10, 15)
diff_1 = date_1 - date_2	        
print(diff_1)                       # 77 days, 0:00:00

datetime_1 = datetime(1999, 12, 31, 12, 30, 50)
datetime_2 = datetime(1999, 10, 15, 19, 45, 21)
diff_2 = datetime_1 - datetime_2	
print(diff_2)                       # 76 days, 16:45:29

'''
We can parse a datetime string by using datetime.strptime() method.
the strptime() method takes 2 arguments date_string and format to parse the string.
'''

datetime1 = datetime.strptime('1999/12/31', '%Y/%m/%d')    # use .strptime('provide date', provide format) -> to parse
print(datetime1)                   # 1999-12-31 00:00:00

'''
We can format a date or datetime instance to a datetime string by using datetime.strftime() method.
'''

d1 = date.today()
print(d1)                        # 2022-08-31

d_str = d1.strftime('%Y/%m/%d')  
print(d_str)                     # 2022/08/31

d_str2 = d1.strftime('%b %d, %Y')  
print(d_str2)                    # Aug 31, 2022

dt1 = datetime.now()
print(dt1)                       # 2022-08-31 22:48:37.985690
dt_str = dt1.strftime('%Y/%m/%d, %HH:%MM:%SS')  
print(dt_str)                    # 2022/08/31, 22H:49M:10S

'''
Some useful datetime formatting codes:

%a: Weekday abbreviated name (Sun, Mon, ..., Sat)
%A: Weekday full name (Sunday, Monday, ..., Saturday)
%d: Day of the month (01, 02, ..., 31)
%b: Month abbreviated name (Jan, Feb, ..., Dec)
%B: Month full name (January, February, ..., December)
%m: Month as number (01, 02, ..., 12)
%Y: Year with Century (1999, 2000, ...)
%H: 24-Hour Clock (00, 01, ..., 23)
%M: Minutes (00, 01, ..., 59)
%S: Seconds (00, 01, ..., 59)
'''