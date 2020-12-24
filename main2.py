grades = []

for i in range(7):
  scores = input("Write your grades: ")
  grades.append(int(scores))

print(f"Final score is {sum(grades)- min(grades)}")
