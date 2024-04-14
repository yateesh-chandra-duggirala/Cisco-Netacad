from datetime import date
from datetime import datetime, timedelta

delta = timedelta(weeks = 2, days = 3, hours = 2)
print(delta)

delta2 = delta * 2
print(delta2)

d = date(2019, 10, 4) + delta2
print(d)

dt = datetime(2019, 10, 4, 14, 53) + delta2
print(dt)