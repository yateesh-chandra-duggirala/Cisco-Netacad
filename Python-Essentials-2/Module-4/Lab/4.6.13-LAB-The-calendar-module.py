'''
Scenario :
During this course, we took a brief look at the Calendar class. 
Your task now is to extend its functionality with a new method called count_weekday_in_year, 
which takes a year and a weekday as parameters, 
and then returns the number of occurrences of a specific weekday in the year.

Use the following tips:
- Create a class called MyCalendar that extends the Calendar class;
- Create the count_weekday_in_year method with the year and weekday parameters. 
- The weekday parameter should be a value between 0-6, where 0 is Monday and 6 is Sunday. 
- The method should return the number of days as an integer;
- In your implementation, use the monthdays2calendar method of the Calendar class.

Test Case 1 :
year=2019, weekday=0
Expected output : 52

Test Case 2 :
year=2000, weekday=6
Expected output : 53
'''

import calendar

class MyCalendar(calendar.Calendar):
    def count_weekday_in_year(self, year, week_day):
        current_month = 1
        counter = 0
        while (current_month <= 12) :
            for row in self.monthdays2calendar(year, current_month):
                if row[week_day][0] != 0:
                    counter += 1
            current_month += 1
        return counter
    
my_cal = MyCalendar()
number_of_weekdays = my_cal.count_weekday_in_year(2019, 0)
print(number_of_weekdays)