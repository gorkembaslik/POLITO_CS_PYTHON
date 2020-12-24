# Write a function called returnDay. This function takes in one parameter ( a number from 1-7)
# and returns the day of the week ( 1 is Sunday, 2 is Monday etc. ).
# If the parameter is less than 1 or greater than 7, the function should return None.
# Expected Output returnDay(1) --> Sunday

a = {1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday", 7: "Saturday"}


def returnday(parameter):
    if 1 <= parameter <= 7:
        print(f"retunday({parameter}) --> {a[parameter]}")
    else:
        return None


returnday(0)
