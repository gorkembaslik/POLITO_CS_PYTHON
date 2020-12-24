# EXERCISE 1
# You want to find out which fraction of your car’s use is for commuting to work, and
# which is for personal use. You know the one-way distance from your home to work.
# For a particular period, you recorded the beginning and ending mileage on the
# odometer and the number of workdays. Write an algorithm to settle this question.

one_way_distance = float(input("ONE WAY DISTANCE FROM HOME TO WORK: "))
number_of_work_days = 5
totalMileage = float(input("TOTAL MILEAGE: "))

useForWork = 2 * number_of_work_days * one_way_distance

fractionOfWork = (useForWork / totalMileage) * 100
fractionOfPersonal = 100 - fractionOfWork

print(f"Fraction of your car's use is %{fractionOfWork:.2f} for commuting to work")
print(f"Fraction of your car's use is %{fractionOfPersonal:.2f} for personal use")
