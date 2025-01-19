import os
from utils.load_data import load_data
from settings import STUDENTS_FILE, ENROLLMENTS_FILE, GRADES_FILE

def issue_transcripts(student_id):
    """Generate and display a transcript for a specific student."""
    # Load student data
    try:
        students = load_data(STUDENTS_FILE)
    except FileNotFoundError:
        print(f"Eror: File '{STUDENTS_FILE}' not found.")
        return
    
    # Find the student record
    student_record = None
    for line in students:
        if line.startswith(student_id):
            student_record = line.strip().split(',')
            break

    if not student_record:
        print(f"Error: Student with ID '{student_id}' not found.")
        return
    
    # Extract student details
    _, student_name, course_type, program, email, contact_number = student_record
    print(f"\n--- Transcript for {student_name} (ID: {student_id}) ---")
    print(f"Course Type: {course_type}")
    print(f"Program: {program}")

    # Load enrollments
    try:
        enrollments = load_data(ENROLLMENTS_FILE)
    except FileNotFoundError:
        print(f"Error: File '{ENROLLMENTS_FILE}' not found.")
        return
    
    # Filter enrollments for the student
    student_enrollments = [line.strip() for line in enrollments if line.startswith(student_id)]
    if not student_enrollments:
        print("No enrollments found for this student.")
        return
    
    # Load grades
    try:
        grades = load_data(GRADES_FILE)
    except FileNotFoundError:
        print(f"Error: File '{GRADES_FILE}' not found.")
        return
    
    # Filter grades for the student
    student_grades = {}
    for line in grades:
        grade_data = line.strip().split(',')
        if grade_data[0] == student_id:
            student_grades[grade_data[1]] = grade_data[2] # {module_code: grade}

    # Display modules and grades
    print("\n--- Modules and Grades ---")
    total_modules = 0
    total_grade_points = 0
    for enrollment in student_enrollments:
        module_code = enrollment.split(',')[1]
        grade = student_grades.get(module_code, "N/A")
        print(f"Module: {module_code}, Grade: {grade}")
        total_modules += 1
        if grade != "N/A":
            try:
                total_grade_points += float(grade) # Assuming grade is numeric
            except ValueError:
                pass

    # Calculate overall summary
    print("\n--- Sumary ---")
    print(f"Total Modules Completed: {total_modules}")
    if total_modules > 0 and total_grade_points > 0:
        average_grade = total_grade_points / total_modules
        print(f"Average Grade: {average_grade:.2f}")
    else:
        print("Average Grade: N/A")

    print("\nTranscript generation completed.")
