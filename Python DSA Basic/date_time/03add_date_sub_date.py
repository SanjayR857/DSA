from  datetime import  datetime, timedelta

current_date = datetime.today()
add_date = current_date+timedelta(12,5)
sub_date = current_date-timedelta(5)

print(current_date)
print(add_date)
print(sub_date)