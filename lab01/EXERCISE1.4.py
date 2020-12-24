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
    if month == 3 and day >= 21:
        season = "Spring"
elif month in (4, 5, 6):
    season = "Spring"
    if month == 6 and day >= 21:
        season = "Summer"
elif month in (7, 8, 9):
    season = "Summer"
    if month == 9 and day >= 21:
        season = "Fall"
elif month in (10, 11, 12):
    season = "Fall"
    if month == 12 and day >= 21:
        season = "Winter"
else:
    print("CHECK IF THE DAY AND/OR MONTH RIGHT")
    exit()

if month == 1:
    month = "January"
elif month == 2:
    month = "February"
elif month == 3:
    month = "March"
elif month == 4:
    month = "April"
elif month == 5:
    month = "May"
elif month == 6:
    month = "June"
elif month == 7:
    month = "July"
elif month == 8:
    month = "August"
elif month == 9:
    month = "September"
elif month == 10:
    month = "October"
elif month == 11:
    month = "November"
elif month == 12:
    month = "December"

print(f"On the {day}{order} day of the {month}, the season is {season}. ")
