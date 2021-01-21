"""
100 days of Python course
DAY 9
"""

# dictionary provided with student names and their scores
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}


# Create an empty dictionary to store the grade interpretations
student_grades = {}

# Convert scores into grades by looping through the dictionary
# note: it will only give you the keys and not the values
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)
