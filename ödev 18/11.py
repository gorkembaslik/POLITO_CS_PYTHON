# You are given quiz scores of a student.
# Compute the final score which is the sum of all scores except for lowest one
# For example if scores are  1 2 3 5 7 8 9  Final score is 30

# FIRST ONE - BEST

print("After submitting your grades press Q to calculate final score")

grades = []
for i in range(99999):
    scores = input("Write your grades: ")
    if scores.upper() != "Q":
        grades.append(int(scores))
    else:
        print(f"Final score is {sum(grades)- min(grades)}")
        break

# SECOND ONE - SIMPLE ONE

grades = []

for i in range(7):
  scores = input("Write your grades: ")
  grades.append(int(scores))

print(f"Final score is {sum(grades)- min(grades)}")
