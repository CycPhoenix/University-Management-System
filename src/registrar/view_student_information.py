from utils.load_data import load_data
from settings import STUDENTS_FILE, ENROLLMENTS_FILE, GRADES_FILE

def view_student_information(student_id):
    """View detailed information for a specific student."""
    # Load student data
    try:
        students = load_data(STUDENTS_FILE)
    except FileNotFoundError:
        print(f"Error: File '{STUDENTS_FILE}' not found.")
        return
    
    # Find the student record
    student_record = None
    for line in students:
        if line.startswith(student_id):
            student_record = line.strip().split(',')
            break
    
    if not student_record:
        print(F"Error: Student with ID '{student_id}' not found.")
        return
    
    # Extract student details
    _, student_name, course_type, program, email, contact_number = student_record
    print(f"\n--- Student Information ---")
    print(f"Name: {student_name}")
    print(f"ID: {student_id}")
    print(f"Course Type: {course_type}")
    print(f"Program: {program}")

    # Load enrollments
    try:
        enrollments = load_data(ENROLLMENTS_FILE)
    except FileNotFoundError:
        print(f"Error: File '{ENROLLMENTS_FILE}' not found.")
        return
    
    # Filter enrollmentss for the student
    student_enrollments = [line.strip() for line in enrollments if line.startswith(student_id)]

    # Display enrolled modules
    print("\n--- enrolled Modules ---")
    if not student_enrollments:
        print("No enrollments found for this student.")
    else:
        for enrollment in student_enrollments:
            module_code = enrollment.split(',')[1]
            print(f"Module Code: {module_code}")

    # Load grades
    try:
        grades = load_data(GRADES_FILE)
    except FileNotFoundError:
        print(f"Error: File '{GRADES_FILE}' not found.")
        return
    
    # Filter grades for the student
    print("\n--- Grades ---")
    student_grades = {}
    for line in grades:
        grade_data = line.strip().strip(',')
        if grade_data[0] == student_id:
            student_grades[grade_data[1]] = grade_data[1] # {module_code: grade}

    if not student_grades:
        print("No grades found for this student.")
    else:
        for module, grade in student_grades.items():
            print(f"Module Code: {module}, Grade: {grade}")

    print("\nStudent information retrieved successfully.")