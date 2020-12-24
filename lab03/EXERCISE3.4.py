# The following algorithm yields the season (Spring, Summer, Fall, or Winter) for a given month and day.
# If month is 1, 2, or 3, season = "Winter"
# Else if month is 4, 5, or 6, season = "Spring"
# Else if month is 7, 8, or 9, season = "Summer"
# Else if month is 10, 11, or 12, season = "Fall"
# If month is divisible by 3 and day >= 21
# If season is "Winter", season = "Spring"
# Else if season is "Spring", season = "Summer"
# Else if season is "Summer", season = "Fall"
# Else season = "Winter"

day = int(input("DAY: "))
month = int(input("MONTH: "))
season = ""
order = ""

if day == 1:
    order = "st"
elif day == 2:
    order = "nd"
elif day == 3:
    order = "rd"
elif day > 31:
    print("CHECK IF THE DAY AND/OR MONTH RIGHT")
    exit()
else:
    order = "th"

if month in (1, 2, 3):
    season = "Winter"
elif month in (4, 5, 6):
    season = "Spring"
elif month in (7, 8, 9):
    season = "Summer"
elif month in (10, 11, 12):
    season = "Fall"
else:
    print("CHECK IF THE DAY AND/OR MONTH RIGHT")
    exit()

if month % 3 == 0 and day >= 21:
    if season == 'Winter':
        season = 'Spring'
    elif season == 'Spring':
        season = 'Summer'
    elif season == 'Summer':
        season = 'Fall'
    else:
        season = 'Winter'

a = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
     9: 'September', 10: 'October', 11: 'November', 12: 'December'}

print(f"On the {day}{order} day of the {a[month]}, the season is {season}. ")
