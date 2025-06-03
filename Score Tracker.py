# Student Grade Tracker Program
# This program collects scores for students and calculates their averages

# Initialize dictionary to store student names as keys and their scores as values
student_scores = {}

# CRITIQUE: This loop is hardcoded to only handle exactly 3 students
# The program lacks flexibility - users cannot choose how many students to enter
for i in range(3):
    # Get student name from user
    name = input(f'Enter the name of Student #{i+1}: ')
    
    # Get comma-separated scores from user
    # CRITIQUE: No input validation whatsoever - program will crash if:
    # - User enters non-numeric values (ValueError)
    # - User enters empty input or just spaces
    # - User doesn't use comma separation properly
    # - User enters fewer or more scores than expected
    scores = input(f'Enter 3 comma-seperated scores of {name}: ')
    
    # Parse the input string into a list of integers
    # CRITIQUE: This comprehension will throw exceptions on invalid input
    # No error handling for malformed data
    scores_list = [int(scores.strip()) for scores in scores.split(",")]
    
    # Store the student name and scores in our dictionary
    # CRITIQUE: Duplicate names will overwrite previous entries
    student_scores[name] = scores_list

# Display results section
print("\n--- Student Results ---")
for name in student_scores:
    # Get scores for current student
    scores = student_scores[name]
    
    # Calculate average score
    # CRITIQUE: No validation that scores are reasonable (could be negative, over 100, etc.)
    average = sum(scores)/len(scores)
    
    # Display formatted average (rounded to 2 decimal places)
    print(f'Average for {name} - {average:.2f}')

# Find and display the top performing student
print("\n--- Top Performer ---")

# Use max() with lambda function to find student with highest average
# The key parameter tells max() to compare students by their average scores
top_student = max(student_scores, key = lambda name: sum(student_scores[name])/len(student_scores[name]))

# Calculate the top student's average for display
bestAvg = sum(student_scores[top_student])/len(student_scores[top_student])

# Display the top student and their average
print(f'Top Student - {top_student} with an average of {bestAvg:.2f}!')

# MAJOR LIMITATIONS:
# 1. Hardcoded to exactly 3 students - no user choice
# 2. No input validation - crashes on invalid data
# 3. Assumes exactly 3 scores per student
# 4. No handling of edge cases (empty names, duplicate names)
# 5. No bounds checking on scores
# 6. Inefficient repeated calculations
