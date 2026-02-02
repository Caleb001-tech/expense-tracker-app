marks = [90,67,33,45,99,22,12,4,22,12,8,66,55,88,91]
passed = [x for x in marks if x >= 50]
failed = [x for x in marks if x < 50]
bonus = [x + 5 for x in marks]
filtered = [x for x in bonus if x < 0 or x > 100]
grades = [
    "A" if x >= 70 else
    "B" if x >= 60 else
    "C" if x >= 50 else "F"
    for x in bonus]

print("These are the scores", marks)
print("those who passed", passed)
print("those who failed", failed)
print("These are the grades", grades)
print("caleb scored", grades[0])
print("favour scored", grades[1])
print("godswill scored", grades[2])
print("wisdom scored", grades[3])
print("james scored", grades[4])
print("peter scored", grades[5])
print("jam scored", grades[6])
high = max(bonus)
low = min(bonus)
print("The highest score is", high)
print("The lowest score is", low)

