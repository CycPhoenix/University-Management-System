import os
from utils.load_data import load_data
from utils.write_data import write_data
from settings import ENROLLMENTS_FILE, MODULES_DIR, MFOUNDATION_FILE, MDIPLOMA_FILE, MUNDERGRADUATE_DIR, MPOSTGRADUATE_DIR, STUDENTS_FILE

def enroll_student(student_id, enrollments, COURSE_DIR):
    """Enroll a student in a module."""
    # Load students file to determine the course type
    try:
        students = load_data(STUDENTS_FILE)
    except FileNotFoundError:
        print(f"Error: File '{STUDENTS_FILE}' not found.")
        return
    
    # Find the sutdent in the file
    student_record = None
    for line in students:
        if line.startswith(student_id):
            student_record = line.strip().split(',')
            break

    if not student_record:
        print(f"Error: Student with ID '{student_id}' not found.")
        return
    
    # Extract student's department (course type)
    _, student_name, course_type, program, email, contact_number = student_record
    print(f"\nStudent Name: {student_name}")
    print(f"Course Type: {course_type}")
    print(f"Program: {program}")
    print(f"Email: {email}")
    print(f"Contact Number: {contact_number}")

    # Load enrollments
    try:
        enrollments = load_data(ENROLLMENTS_FILE)
    except FileNotFoundError:
        enrollments = [] # If no enrollment file, start fresh

    # Determine the path based on the course type
    if course_type.lower() in ["foundation", "diploma"]:
        # Single file for Foundation and Diploma
        module_file = os.path.join(MODULES_DIR, f"{course_type.lower()}.txt")
        try:
            modules = load_data(module_file)
        except FileNotFoundError:
            print(f"Error: File '{module_file}' not found.")
            return
    
    elif course_type.lower() in ["undergraduate", "postgraduate"]:
        # Folder-based for Undergraduate and Postgraduate
        folder_path = os.path.join(MODULES_DIR, course_type.lower())
        try:
            # Find the program file for the student
            category_file = f"{program.replace(' ', '_').lower()}.txt"
            module_file = os.path.join(folder_path, category_file)
            modules = load_data(module_file)
        except FileNotFoundError:
            print(f"Error: Program file '{category_file}' not found in '{folder_path}'.")
            return
    else:
        print(f"Error: Invalid course type '{course_type}' for student.")
        return
    
    # Display available modules
    print("--- Available Modules ---")
    for idx, module in enumerate(modules, start=1):
        print(f"{idx}. {module.strip()}")

    # Select a module
    module_choice = input("Select a module to enroll in (or type 'Cancel' to exit): ").strip()
    if module_choice.lower() == 'cancel':
        print("Action canceled.")
        return
    
    if not module_choice.isdigit() or not (1 <= int(module_choice) <= len(modules)):
        print("Invalid choice. Returning to enrollment menu.")
        return
    
    selected_module = modules[int(module_choice) - 1].strip().split(',')[0]

    # Check if already enrolled
    if any(f"{student_id},{selected_module}" in line for line in enrollments):
        print(f"Student {student_id} is already enrolled in module {selected_module}.")
        return
    
    # Add enrollment
    enrollments.append(f"{student_id},{selected_module}\n")
    write_data(ENROLLMENTS_FILE, enrollments)
    print(f"Student {student_id} successfully enrolled in module {selected_module}.")

    # Debugging to ensure enrollments is a valid list of strings
    print('DEBUG: Enrollments before writing:", enrollments')

    # Write updated enrollments to file
    write_data(ENROLLMENTS_FILE, enrollments)
    print(f"Student {student_id} successfully enrolled in module {selected_module}.")
