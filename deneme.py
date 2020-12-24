print("After submitting your grades press Q to calculate final score")

grades = []
for i in range(99999):
    scores = input("Write your grades: ")
    if scores.upper() != "Q":
        grades.append(int(scores))
    elif scores.upper() == "Q":
        print(f"Final score is {sum(grades)- min(grades)}")
        break
