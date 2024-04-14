from datetime import datetime, date

print(datetime.now())
print(datetime.now().isoformat())

# Replace method is used to replace the parameters from the date object.
d = date.today()
print(d)

d = d.replace(year=2019, month=9)
print(d)