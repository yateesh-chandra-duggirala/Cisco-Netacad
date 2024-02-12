'''
Scenario
Your task is to write and test a function which takes three arguments (a year, a month, and a day of the month) and returns the corresponding day of the year, or returns None if any of the arguments is invalid.

Use the previously written and tested functions. 
Add some test cases to the code.
'''

def is_year_leap(year):
    if year%4==0:
       if year%100==0: 
            if year%400==0: return True
            else: return False
       else: return True
    return False

def days_in_month(year, month):
    # Create list with month days for each month as advised in the LAB
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_year_leap(year):
        month_days[1] = 29  # 29 days for February on a leap year.
    return month_days[month - 1]  # month 1 corresponds with index 0 & so on.

def day_of_year(year,month, day):
    total = 0  # initializing the total variable to add results
    # create loop to add only days in the months before the month in the input/test data
    for i in range(1, month):
        result = days_in_month(year, i)
        total += result
    day_num = total + day  # add the value of the day argument to get day of the year
    return day_num

print(day_of_year(2000, 12, 31))
print(day_of_year(2021, 7, 29))
print(day_of_year(1999, 12, 31))
