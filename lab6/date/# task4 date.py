# task4 date

# date difference seconds

import datetime
d1=datetime.datetime(2023, 10, 20, 12, 20, 45)
d2=datetime.datetime(2023, 10, 26, 8, 25, 13)
dif=abs(d1-d2)
print(int(dif.total_seconds()))