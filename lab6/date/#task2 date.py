#task2 date
from datetime import datetime, timedelta


y=datetime.now()-timedelta(days=1)
tod=datetime.today()
tom=datetime.now()+timedelta(days=1)
print("Yesterday: ", y.strftime("%Y-%m-%d"))
print("Today: ", tod.strftime("%Y-%m-%d"))
print("Tomorrow: ", tom.strftime("%Y-%m-%d"))
