# 1. Write a Python script to display the various Date Time formats -
# a) Current date and time
# b) Current year
# c) Month of year
# d) Week number of the year
# e) Weekday of the week
# f) Day of year
# g) Day of the month
# h) Day of week

import datetime
current_date_time = datetime.datetime.now()
print('current date time ',current_date_time)

current_year = current_date_time.year
print('current year',current_year)

current_month = current_date_time.month
print('current month ',current_month)

currnet_day = current_date_time.day
print('current day ',currnet_day)

# year
current_week  =  datetime.date.today().strftime('%W')
print('current week ', current_week)

#week
current_week  =  datetime.date.today().strftime('%w')
print('current week ', current_week)

print(datetime.date.today().strftime('%B'))
print(datetime.date.today().strftime('%b'))
print(datetime.date.today().strftime('%j'))
print(datetime.date.today().strftime('%d'))
print(datetime.date.today().strftime('%A'))