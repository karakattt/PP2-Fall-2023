#date
from datetime import datetime, timedelta

# substract 5 days

#task1 date
t=datetime.now()
s=t-timedelta(days=5)
print(s.strftime("%Y-%m-%d"))
