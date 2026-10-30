from pathlib import Path

GRADES_FILE = Path(__file__).resolve().parent /"grades.csv"

TEST_WEIGHT = 0.3
EXAM_WEIGHT = 0.3
DISCUSSION_WEIGHT = 0.2
PROJECT_WEIGHT = 0.2


def main():
    """Read the grades file, compute each student's weighted final
    grade, and print a summary of how many students fall into each
    grade range.

    # TODO - Read GRADES_FILE and build a list of each student's
    #        weighted final grade (skip the header row, and use
    #        process_row() to do the per-student work).

    # TODO - Pass that list to analyze_grade() to print the summary.

    # TODO - Use try/except to handle a missing file and any other
    #        errors that can occur while reading or processing it.
    """
    students_final_grade = []

    try:
        with open(GRADES_FILE, 'r') as grades_file:
            grades_file.readline()


            for grade_line in grades_file:
                grade_final = process_row(grade_line)
                students_final_grade.append(grade_final)

        analyze_grade(students_final_grade)
    

    except FileNotFoundError: 
        print("Error: The file could not be found.")

    except OSError:
        print("Error: Problem while reading or opening the file.")




def process_row(row):
    """Given one row from the grades file, return that student's
    weighted final grade (bypass the Name and StudentID columns)."""
    # TODO - Implement this function.
    grade_columns = row.strip().split(",")
    student_test_scores = []
    student_exam_scores = []
    student_discussion_scores = []
    student_project_scores = float(grade_columns[10])


    for scores in grade_columns[2:6]:
        student_test_scores.append(float(scores))

    for scores in grade_columns[6:8]:
        student_exam_scores.append(float(scores))

    for scores in grade_columns[8:10]:
        student_discussion_scores.append(float(scores))


    test_average = average_subject(student_test_scores)
    exam_average = average_subject(student_exam_scores)
    discussion_average = average_subject(student_discussion_scores)                              

    grade_calculation = weight_final(test_average, exam_average, discussion_average, student_project_scores)

    return grade_calculation

def average_subject(subject_list):
    """Return the average of the scores in subject_list."""
    # TODO - Implement this function.
    average = sum(subject_list) / len(subject_list)
    return average


def weight_final(test_avg, exam_avg, discussion_avg, project_score):
    """Return a student's weighted final grade, combining the test,
    exam, discussion, and project scores using the weight constants
    declared above."""
    # TODO - Implement this function.
    grade_calculation = (test_avg * TEST_WEIGHT) + (exam_avg * EXAM_WEIGHT) + \
    (discussion_avg * DISCUSSION_WEIGHT) + (project_score * PROJECT_WEIGHT)

    return grade_calculation


def analyze_grade(weight_final_list):
    """Count and print how many students fall into each grade range:
    90 or above, 80-89, 70-79, 60-69, and below 60."""
    # TODO - Implement this function.
    grade_A = 0
    grade_B = 0
    grade_C = 0
    grade_D = 0
    grade_F = 0

    for grades in weight_final_list:
        if grades >= 90:
            grade_A += 1

        if grades >= 80:
            grade_B += 1

        if grades >= 70:
            grade_C += 1

        if grades >= 60:
            grade_D += 1

        else:
            grade_F += 1

    print(f"Number of students with final grade 90 or above: {grade_A}")
    print(f"Number of students with final grade 80-89: {grade_B}")
    print(f"Number of students with final grade 70-79: {grade_C}")
    print(f"Number of students with final grade 60-69: {grade_D}")
    print(f"Number of students with final grade below 60: {grade_F}")
    


if __name__ == "__main__":
    main()