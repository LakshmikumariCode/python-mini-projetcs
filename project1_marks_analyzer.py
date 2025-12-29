# Project 1: Marks Analyzer
# A simple Python program to calculate and analyze student marks

# The list of student marks
marks = [78, 45, 90, 66, 52]

# It will calculate total, average, highest and lowest marks
total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

# To count passed and failed students
passed = 0
failed = 0

for m in marks:
    if m >= 40:
        passed += 1
    else:
        failed += 1

# Display results
print("Total:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
print("Passed:", passed)
print("Failed:", failed)
