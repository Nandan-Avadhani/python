student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    if student_scores[key] <= 70:
        student_scores[key] = "Fail"
            
    elif ((student_scores[key] > 70) and (student_scores[key] < 81)):
        student_scores[key] = "Acceptable"
    elif ((student_scores[key] > 80 ) and (student_scores[key] < 91)):
        student_scores[key] = "Exceeds Expectations"
     
    elif ((student_scores[key] > 90 ) and (student_scores[key] < 101)):
        student_scores[key] = "Outstanding"

student_grades = student_scores   

# 🚨 Don't change the code below 👇
print(student_grades)