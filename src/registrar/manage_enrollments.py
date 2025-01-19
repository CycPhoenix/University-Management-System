from utils.load_data import load_data
from utils.write_data import write_data
from settings import ENROLLMENTS_FILE, COURSE_DIR, STUDENTS_FILE
from registrar.manage_enrollments_modules.enroll_student import enroll_student
from registrar.manage_enrollments_modules.unenroll_student import unenroll_student
from registrar.manage_enrollments_modules.view_enrollments import view_enrollments

def manage_enrollments():
    """Manage student enrollments."""
    me_art = r"""
     __ __                            ___                 _  _                    _          
    |  \  \ ___ ._ _  ___  ___  ___  | __>._ _  _ _  ___ | || |._ _ _  ___ ._ _ _| |_ ___
    |     |<_> || ' |<_> |/ . |/ ._> | _> | ' || '_>/ . \| || || ' ' |/ ._>| ' | | | <_-<
    |_|_|_|<___||_|_|<___|\_. |\___. |___>|_|_||_|  \___/|_||_||_|_|_|\___.|_|_| |_| /__/
                          <___'                                                          
    """

    separator_length = max(len(line) for line in me_art.splitlines())
    separator = "=" * separator_length

    # Load students and enrollments
    try:
        students = load_data(STUDENTS_FILE)
        enrollments = load_data(ENROLLMENTS_FILE)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return
    
    # Display students
    print("\n--- Students List ---")
    for line in students:
        student_data = line.strip().split(',')
        print(f"ID: {student_data[0]}\nName: {student_data[1]}\nDepartment: {student_data[2]}\nProgram: {student_data[3]}")
    
    # Select a student
    student_id = input("Enter the Student ID to manage enrollments (or type 'Cancel' to exit):").strip().upper()
    if student_id.lower() == 'cancel':
        print("Action canceled. Returning to registrar menu.")
        return
    
    # Verify student exists
    if not any(student_id in line.split(',')[0] for line in students):
        print(f"Student with ID '{student_id}' not found.")
        return
    
    while True:
        print("\n--- Enrollment Options ---")
        print("1. Enroll in a Module")
        print("2. Unenroll from a Module")
        print("3. View Current Enrollments")
        print("4. Exit Enrollment Management")

        choice = input("Select an option: ").strip()
        if choice == '1':
            enroll_student(student_id, enrollments)
        elif choice == '2':
            unenroll_student(student_id, enrollments)
        elif choice == '3':
            view_enrollments(student_id, enrollments)
        elif choice == '4':
            print("Returning to registrar menu.")
            break
        else:
            print("Invalid option. Please try again.")
