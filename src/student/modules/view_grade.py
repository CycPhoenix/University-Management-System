import os

def view_grades(student_id):
    # Correct path to access 'grades.txt' from the root of the project
    file_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'data', 'grades.txt')

    # Open the grades.txt file
    with open(file_path, 'r') as file:
        records = file.readlines()

    print("Grades Record")
    found = False
    for record in records:
        if record.startswith(student_id):
            student_id, module_code, grade = record.strip().split(',')
            print(f"{module_code}: {grade}")
            found = True
        
    if not found:
        print(f"No grades found for student ID {student_id}.")  