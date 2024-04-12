from datetime import date
import time

# today method is used to get today's date
today = date.today()

print("Today's Calendar : ", today)
print("Today's Date : ", today.day)
print("Today's Month :", today.month)
print("Today's Year :", today.year)

# If we want to manually create a date,
t_day = date(2019, 8, 15)
print(t_day)

timestamp = time.time()
print("Time Stamp : ",timestamp)

d = date.fromtimestamp(timestamp)
print("Date from Timestamp : ", d)