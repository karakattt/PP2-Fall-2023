#lab6
#date
from datetime import datetime, timedelta

#task1 date
# t=datetime.now()
# s=t-timedelta(days=5)
# print(s.strftime("%Y-%m-%d"))



#task2 date
# y=datetime.now()-timedelta(days=1)
# tod=datetime.today()
# tom=datetime.now()+timedelta(days=1)
# print("Yesterday: ", y.strftime("%Y-%m-%d"))
# print("Today: ", tod.strftime("%Y-%m-%d"))
# print("Tomorrow: ", tom.strftime("%Y-%m-%d"))




#task3 date
# t=datetime.now()
# print("Microseconds of today: ", t.strftime("%f"))




#task4 date
# import datetime
# d1=datetime.datetime(2023, 10, 20, 12, 20, 45)
# d2=datetime.datetime(2023, 10, 26, 8, 25, 13)
# dif=abs(d1-d2)
# print(int(dif.total_seconds()))