from datetime import  datetime

string = datetime.strptime('Jul 1 2014 2:43PM','%b %d %Y %I:%M%p')
date_object = datetime.strptime('Jul 1 2014 2:43PM', '%b %d %Y %I:%M%p')
print(date_object)
print(string)

current_time = datetime.now().time()
print(current_time)
