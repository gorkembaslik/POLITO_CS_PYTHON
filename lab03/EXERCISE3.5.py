# In reality, this number is not exact and for all dates after 1582 the Gregorian correction
# applies: usually years divisible by 4, such as 1996, are leap years, but years divisible
# by 100, such as 1900, are not; as an exception to the exception, years divisible by
# 400, such as 2000, are leap years. Write a program that asks the user for a year and
# determines if it is a leap year, using a single if statement (with the appropriate Boolean operators). [P3.27]

date = int(input("WHETHER WRITTEN YEAR IS LEAP YEAR OR NOT: "))

if date > 1582:
    if date % 4 == 0:
        year = "a leap year"
        if date % 100 == 0:
            year = "an ordinary day"
            if date % 400 == 0:
                year = "a leap year"
    else:
        year = "an ordinary day"
    print(f"{date} is {year}")
else:
    print("The date should be after 1582")
    exit()
