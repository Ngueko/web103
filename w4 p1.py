# Input: Allow the user to enter two exam scores
exam1_score = float(input("Enter Exam 1 score: "))
exam2_score = float(input("Enter Exam 2 score: "))

# Processing: Calculate the weighted scores and total score
exam1_weighted = exam1_score * 0.60
exam2_weighted = exam2_score * 0.40
total_score = exam1_weighted + exam2_weighted

# Output: Display the total score
print(f"Total Score: {total_score}")