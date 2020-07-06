from datetime import date, datetime

# date
today = date.today()
print(today)
print(today.day)

# datetime

now = datetime.now()
now1 = datetime.today()
print(now, now1, sep='\n')