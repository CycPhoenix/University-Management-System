import os
from settings import GRADES_FILE

def view_grades(student_id):
    # Correct path to access 'grades.txt' from the root of the project
    file_path = GRADES_FILE

    try:
        if not os.path.exists(file_path):
            print(f"Error: File '{file_path}' not found.")
            return
        
        with open(file_path, 'r') as file:
            records = file.readlines()

        print("\n--- Grades Record ---")
        found = False
        for record in records:
            fields = record.strip().split(',')
            if len(fields) == 4 and fields[1] == student_id:
                module_name, numeric_grade, letter_grade = fields[0], fields[2], fields[3]
                print(f"{module_name}: {numeric_grade} ({letter_grade})")
                found = True

        if not found:
            print(f"No grades found for student ID '{student_id}'.")
    except Exception as e:
        print(f"Error reading grades: {e}")
