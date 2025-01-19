import os
from utils.load_data import load_data
from utils.write_data import write_data
from settings import ENROLLMENTS_FILE, MFOUNDATION_FILE, MDIPLOMA_FILE, MUNDERGRADUATE_FILE, MPOSTGRADUATE_FILE, STUDENTS_FILE

def enroll_student(student_id, enrollments):
    """Enroll a student in a module."""
    # Load students file to determine the course type
    try:
        students = load_data(STUDENTS_FILE)
    except FileNotFoundError:
        print(f"Error: File '{STUDENTS_FILE}' not found.")
        return
    
    # Find the student in the file
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
        enrollments = [] # Start fresh if no enrollment file exists

    module_file = None
    if course_type.lower() == "foundation":
        module_file = MFOUNDATION_FILE
    elif course_type.lower() == "diploma":
        module_file = MDIPLOMA_FILE
    elif course_type.lower() == "undergraduate":
        module_file = MUNDERGRADUATE_FILE
    elif course_type.lower() == "postgraduate":
        module_file = MPOSTGRADUATE_FILE
    else:
        print(f"Error: Invalid course type '{course_type}' for student.")
        return

    # Load modules
    try:
        modules = load_data(module_file)
        if not modules:
            print(f"No modules found in '{module_file}'.")
            return
    except FileNotFoundError:
        print(f"Error: File '{module_file}' not found.")
        return
    
    # Display available modules
    print("\n--- Available Modules ---")
    for idx, module in enumerate(modules, start=1):
        module_details = module.strip().split(',')
        module_code = module_details[0] if len(module_details) > 1 else "Unknown"
        module_name = module_details[1] if len(module_details) > 1 else module.strip()
        print(f"{idx}. {module_code} - {module_name.strip()}")

    # Select a module
    while True:
        module_choice = input("Select a module by index (or type 'Cancel' to exit): ").strip()
        if module_choice.lower() == 'cancel':
            print("Action canceled.")
            return
        if module_choice.isdigit() and 1 <= int(module_choice) <= len(modules):
            selected_module = modules[int(module_choice) - 1].strip().split(',')[1]
            break
        else:
            print("Invalid choice. Please select a valid module index.")

    # Check if already enrolled
    if any(f"{student_id},{selected_module}" in line for line in enrollments):
        print(f"Student {student_id} is already enrolled in module {selected_module}.")
        return
    
    # Add enrollment
    enrollments.append(f"{student_id},{selected_module}\n")
    write_data(ENROLLMENTS_FILE, enrollments)
    print(f"Student {student_id} successfully enrolled in module {selected_module}.")
