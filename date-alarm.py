# -*- coding: utf-8 -*-

"""
Small program for ask a date and then ask days number and combine these two data. 
Write out to the disk, and show some information.
Later create an alarm for this.....
"""
#for string conversion (str to int)
#https://www.cyberciti.biz/faq/python-convert-string-to-int-functions/
#date and time manipulation
#https://pymotw.com/3/datetime/
#https://stackoverflow.com/questions/12772057/how-to-format-date-in-iso-using-python
#https://automatetheboringstuff.com/chapter15/
#input-output
#http://www.python-course.eu/python3_file_management.php
#http://www.diveintopython3.net/files.html
#https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
#http://www.theunixschool.com/2013/08/python-how-to-write-list-to-file.html
#http://www.python-course.eu/python3_print.php

import datetime
import calendar
now=datetime.datetime.now() #precise timestamp
ma = datetime.date.today() #only the date
list_of_hebrakolas=[]

whoh=str(input('Ki a fene vagy? '))
whath=str(input('Mi a f*szt csináltál? '))
print("a mai dátum", ma, "pontosabban:", now)
hebrakolas_datuma=input("hebrákolás dátuma (YYYY-mm-dd):")
hebrakolas_datuma=datetime.datetime.strptime(hebrakolas_datuma, "%Y-%m-%d")
print (calendar.TextCalendar(calendar.MONDAY).formatmonth(ma.year, ma.month, 1, 1)) #printeni az előzőleg megadott dátum hónapját, pontos napot jó lenne jelölni...

alarm_days=int(input('hány nap múlva riasszon:'))
#alarm_days=int(alarm_days)
one_day = datetime.timedelta(days=1) #just an example
alarm_days = datetime.timedelta(days = alarm_days)
date_of_alarm = hebrakolas_datuma + alarm_days

list_of_hebrakolas.extend([hebrakolas_datuma, alarm_days, date_of_alarm, whoh, whath])
hebrakolasok=open("hebrakolasok", 'a')
print (list_of_hebrakolas, end="\n", file=hebrakolasok)
hebrakolasok.close()

#the write method - shit
#hebrakolasok = open("hebrakolasok.txt", 'w') #ha 'w' így mindig felülírja a dolgokat 'a' jobb
#for hbr in list_of_hebrakolas:
#    hebrakolasok.write(hbr+';')
#hebrakolasok.write('\n')
#hebrakolasok.close()

print (calendar.TextCalendar(calendar.MONDAY).formatmonth(date_of_alarm.year, date_of_alarm.month, 1, 1))
print ('alarm day:', date_of_alarm.strftime('%Y-%m-%d'))
print ("list_of_hebrakolas:", list_of_hebrakolas)
