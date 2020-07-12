"""
1360. Number of Days Between Two Dates
Write a program to count the number of days between two dates.

The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

 

Example 1:

Input: date1 = "2019-06-29", date2 = "2019-06-30"
Output: 1
Example 2:

Input: date1 = "2020-01-15", date2 = "2019-12-31"
Output: 15
 

Constraints:

The given dates are valid dates between the years 1971 and 2100.
"""
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) :
        monthday1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        monthday2 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        dat1 = date1.split('-')
        dat2 = date2.split('-')
        year1, month1, day1 = date1.split('-')
        year2, month2, day2 = date2.split('-')

        def count(year, month, day):
            n = 0
            for i in range(0, year):
                if leap(i):
                    n += 366
                else:
                    n += 365
            n += day
            if leap(year):
                for i in range(0, month - 1):
                    n += monthdays2[i]
            else:
                for i in range(0, month - 1):
                    n += monthdays1[i]
            return n

        def leap(year):
            if (year % 4) == 0:
                if (year % 100 == 0):
                    if (year % 400 == 0):
                        return True
                    else:
                        return False
                else:
                    return True
            else:
                return False

        y1 = count(int(year1), int(month1), int(day1))
        y2 = count(int(year2), int(month2), int(day2))
        return abs(y2 - y1)


class Solution:
    def daysBetweenDates(self, date1: str, date2: str):
        return abs(
            datetime.datetime.strptime(date1, '%Y-%m-%d') -
            datetime.datetime.strptime(date2, '%Y-%m-%d')).days
