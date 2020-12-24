for i in range(7): # repeat at most 7 times
  scores = input("Write your grades: ") # require user input
  if scores.upper() != "Q":  # if user input is not Q
    grades.append(int(scores)) # convert the string to int and put the scores (value as string) in the list
  else: # otherwise (user input Q)
    break # stop the for loop

print(f"Final score is {sum(grades)- min(grades)}")
