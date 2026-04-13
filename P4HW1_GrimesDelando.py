# Delando Grimes
# 04/12/2026
# P4HW1 - Score List
# This program collects scores, validates them, drops the lowest,
# calculates the average, and assigns a letter grade.

# Pseudocode:
# Ask how many scores
# Create empty list
# Loop to collect scores
# Validate each score (0-100)
# If invalid, ask again
# Add valid scores to list
# Find and remove lowest score
# Calculate average
# Determine letter grade
# Display results

num_scores = int(input("How many scores do you want to enter? "))

scores = []

for i in range(1, num_scores + 1):
    score = float(input(f"Enter score #{i}: "))

    while score < 0 or score > 100:
        print("\nINVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{i} again: "))

    scores.append(score)

lowest = min(scores)
scores.remove(lowest)

average = sum(scores) / len(scores)

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print("\n--------------Results--------------")
print(f"Lowest Score  : {lowest:.1f}")
print(f"Modified List : {scores}")
print(f"Scores Average: {average:.2f}")
print(f"Grade         : {grade}")
print("-----------------------------------")
