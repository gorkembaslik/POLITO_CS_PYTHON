# The following pseudocode describes how to turn a string containing a ten-digit
# phone number (such as "4155551212") into a more readable string with parentheses
# and dashes, like this: "(415) 555-1212".

number = int(input("TEN-DIGIT PHONE NUMBER: "))
n = str(number)
print(f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]} ")
