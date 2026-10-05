#Constants of weighted scores before multiply into average score
EXAM_WEIGHT = 0.5
ASSIGNMENT_WEIGHT = 0.3
QUIZ_WEIGHT = 0.2

#gets the curriculum scores from the user
midterm_exam_grade = float(input("Please enter midterm grade: "))
final_exam_grade = float(input("Please enter final exam grade: "))
assignment_one = float(input("Please enter first assignment grade: "))
assignment_two = float(input("Please enter second assignment grade: "))
quiz_one = float(input("Please enter first quiz grade: "))
quiz_two = float(input("Please enter second quiz grade: "))

#calculates the average for each grade and multiplies by the weight for that category
exam_grade = (midterm_exam_grade + final_exam_grade) / 2 * EXAM_WEIGHT
assignment_grade = (assignment_one + assignment_two) / 2 * ASSIGNMENT_WEIGHT
quiz_grade = (quiz_one + quiz_two) / 2 * QUIZ_WEIGHT

#calculates the final grade by adding the weighted averages 
final_grade = (exam_grade + assignment_grade + quiz_grade)

#generates the output of the final grade 
print(f'The students final grade is {final_grade:.2f}%')