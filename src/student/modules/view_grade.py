def view_grades(student_id):
    with open('grades.txt', 'r') as file:
        grades = file.readlines()
    print("Your Grades:")
    for grade in grades:
        if grade.startswith(student_id):
            _, module_code, grade_value = grade.strip().split(',')
            print(f"{module_code}: {grade_value}")