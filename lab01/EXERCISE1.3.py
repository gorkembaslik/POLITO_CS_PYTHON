# In a scheduling program, we want to check whether two appointments overlap.
# For simplicity, appointments start at a full hour, and we use military time (with hours 0–23).
# The following pseudocode describes an algorithm that
# determines whether the appointment with start time start1 and end time end1 overlaps
# with the appointment with start time start2 and end time end2

appointment1 = int(input("First appointment of today starts at: "))
appointment1_ = int(input("First appointment of today finishes at: "))
appointment2 = int(input("Second appointment of today starts at: "))
appointment2_ = int(input("Second appointment of today starts at: "))

if appointment1_ <= appointment2:
    print(f"The appointments don't overlap and first appointment starts at: {appointment1} and it takes: "
          f"{appointment1_ - appointment1} hours, second appointment of today starts at: {appointment2} and it takes: "
          f"{appointment2_ - appointment2} hours")
else:
    print("The appointments overlapping.")
