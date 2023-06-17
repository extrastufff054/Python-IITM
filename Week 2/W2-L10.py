# Different ways to import library

import calendar
# The calendar module allows you to output calendars and provides additional useful functions for them.
print(calendar.month(2021, 7))
print('------------------------------------------------')

# Display calendar for a year
print(calendar.calendar(2021))

print('------------------------------------------------')

from calendar import *
print(calendar(2021))
print(month(2021, 2))

print('------------------------------------------------')

from calendar import month
print(month(2021, 2))
# print(calendar(2021)) # This will give error as calendar is not imported

print('------------------------------------------------')

from calendar import month, calendar
print(month(2021, 2))
print(calendar(2021))

print('------------------------------------------------')

import calendar as c # This is aliasing
print(c.month(2022, 2))
print(c.calendar(2022))

print('------------------------------------------------')

from calendar import month as m, calendar as c
print(m(2003, 2))
print(c(2003))