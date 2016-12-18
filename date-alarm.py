# -*- coding: utf-8 -*-

"""
Small program for ask a date and then ask days number and combine these two data.
Later create an alarm for this.
"""
#for string conversion (str to int)
#https://www.cyberciti.biz/faq/python-convert-string-to-int-functions/
#date and time manipulation
#https://pymotw.com/3/datetime/
#https://stackoverflow.com/questions/12772057/how-to-format-date-in-iso-using-python
#https://automatetheboringstuff.com/chapter15/

import datetime
import calendar
now=datetime.datetime.now() #precise timestamp
ma = datetime.date.today() #only the date

print("a mai dátum", ma, "pontosabban:", now)
hebrakolas_datuma=input("hebrákolás dátuma (YYYY-mm-dd):")
hebrakolas_datuma=datetime.datetime.strptime(hebrakolas_datuma, "%Y-%m-%d")
print (calendar.TextCalendar(calendar.MONDAY).formatmonth(ma.year, ma.month, 1, 1)) #printeni az előzőleg megadott dátum hónapját, pontos napot jó lenne jelölni...

alarm_days=int(input('hány nap múlva riasszon:'))
#alarm_days=int(alarm_days)
one_day = datetime.timedelta(days=1) #just an example
alarm_days = datetime.timedelta(days = alarm_days)
date_of_alarm = hebrakolas_datuma + alarm_days

print (calendar.TextCalendar(calendar.MONDAY).formatmonth(date_of_alarm.year, date_of_alarm.month, 1, 1))
print ('alarm day:', date_of_alarm.strftime('%Y-%m-%d'))
