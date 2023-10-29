#task3 date

# difference between days as microseconds
from datetime import datetime, timedelta
t=datetime.now()
print("Microseconds of today: ", t.strftime("%f"))
