from datetime import datetime
d = datetime(2024, 7, 5, 4, 18, 24)

# %Y returns 4-digited Century name (2024), where as %y returns 2-digited Century Name(24).
print(d.strftime("%Y/%m/%d"))
print(d.strftime("%y/%m/%d"))

# %B returns the Full Month Name
print(d.strftime("%Y/%B/%d %H:%M:%S"))