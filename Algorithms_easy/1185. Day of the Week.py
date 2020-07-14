"""
1185. Day of the Week
Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

 

Example 1:

Input: day = 31, month = 8, year = 2019
Output: "Saturday"
Example 2:

Input: day = 18, month = 7, year = 1999
Output: "Sunday"
Example 3:

Input: day = 15, month = 8, year = 1993
Output: "Sunday"
 

Constraints:

The given dates are valid dates between the years 1971 and 2100.
"""
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int):
        return datetime.date(year, month, day).strftime('%A')

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int):
        week = {
            0: 'Friday',
            1: 'Saturday',
            2: 'Sunday',
            3: 'Monday',
            4: 'Tuesday',
            5: 'Wednesday',
            6: 'Thursday'
        }
        mon = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }

        leap_num = 1 + (year - 1 - 1972) // 4 if year > 1971 else 0
        year_total = (year - 1971) * 365 + leap_num
        month_total = sum([mon[i] for i in mon if i < month])
        if (year % 4 == 0 and year % 100 or year % 400 == 0) and month > 2:
            res = year_total + month_total + day + 1
        else:
            res = year_total + month_total + day

        return week[(res - 1) % 7]
