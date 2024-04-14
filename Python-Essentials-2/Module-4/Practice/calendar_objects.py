import calendar

c = calendar.Calendar()

# for week in c.iterweekdays():
#     print(week, end = ' ')

# for month in c.itermonthdates(2019, 11):
#     print(month, end = ' ')

# for month in c.itermonthdays(2019, 11):
#     print(month, end = ' ')

# for month in c.itermonthdays2(2019, 11):
#     print(month, end = ' ')

# for month in c.itermonthdays3(2019, 11):
#     print(month, end = ' ')

# for month in c.itermonthdays4(2019, 11):
#     print(month, end = ' ')

for month in c.monthdays2calendar(2019, 11):
    print(month, end = ' ')
