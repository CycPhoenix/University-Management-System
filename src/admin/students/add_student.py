from utils.display_choices import display_choices
from utils.load_data import load_data
from utils.write_data import write_data
from settings import STUDENTS_FILE, DEPARTMENTS_FILE

def add_student():
    """Add a new student to the system."""
    print("\n--- Add New Student ---")

    # Input Student ID
    while True:
        student_id = input("Enter the student ID (or type 'Cancel' to exit): ").strip()
        if student_id.lower() == 'cancel':
            print("Action canceled. Returning to manage students menu.")
            return
        if student_id == '':
            print("Student ID cannot be empty. Please try again.")
            continue
    
        # Check if student ID already exists
        existing_students = load_data(STUDENTS_FILE)
        if any(student_id.lower() == line.split(',')[0].strip().lower() for line in existing_students):
            print(f"Student ID '{student_id}' already exists. Please enter a new ID.")
            continue
        break

    # Input Student Name
    student_name = input("Enter the student name (or type 'Cancel' to exit): ").strip()
    if student_name.lower() == 'cancel':
        print("Action canceled. Returning to manage students menu.")
        return
    if student_name == '':
        print("Student name cannot be empty.")
        return
    
    # Select Department
    try:
        departments = [dep.strip() for dep in load_data(DEPARTMENTS_FILE)]
        if not departments:
            print("No departments found. Please ensure departments.txt is populated.")
            return
        department = display_choices({str(i + 1): dep for i, dep in enumerate(departments)})
    except FileNotFoundError:
        print(f"Error: File '{DEPARTMENTS_FILE}' not found.")
        return
    
    # Input Additional Details
    email = input("Enter the student email (optional, press Enter to skip): ").strip()
    contact_number = input("Enter the student contact number (optional, press Enter to skip): ").strip()

    # Confirm and Save Student
    student_details = f"{student_id},{student_name},{department},{email},{contact_number}"
    try:
        write_data(STUDENTS_FILE, student_details)
        print(f"Student '{student_name}' added successfully!")
    except Exception as e:
        print(f"Error: Failed to add student. {e}")
