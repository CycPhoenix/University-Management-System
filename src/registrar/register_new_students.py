import os
from utils.append_data import append_data
from utils.load_data import load_data
from settings import STUDENTS_FILE, DEPARTMENTS_FILE, FOUNDATION_FILE, DIPLOMA_FILE, UNDERGRADUATE_DIR, POSTGRADUATE_DIR

def register_new_students():
    """Register a new student to the system."""
    rns_art = r"""
     ___            _        _              _ _               ___    _          _             _          
    | . \ ___  ___ <_> ___ _| |_ ___  _ _  | \ | ___  _ _ _  / __> _| |_ _ _  _| | ___ ._ _ _| |_ ___
    |   // ._>/ . || |<_-<  | | / ._>| '_> |   |/ ._>| | | | \__ \  | | | | |/ . |/ ._>| ' | | | <_-<
    |_\_\\___.\_. ||_|/__/  |_| \___.|_|   |_\_|\___.|__/_/  <___/  |_| `___|\___|\___.|_|_| |_| /__/
              <___'                                                                                  

    """
    separator_length = max(len(line) for line in rns_art.splitlines())
    separator = "=" * separator_length

    while True:
        print()
        print(separator)
        print(rns_art)
        print(separator)

        # Input Student ID
        student_id = input("Enter the student ID (or type 'Cancel to exit): ").strip().upper()
        if student_id.lower() == 'cancel':
            print("Action canceled. Returning to manage registrar menu.")
            return
        if not student_id:
            print("Student ID cannot be empty. Please try again.")
            continue

        # Check if student ID already exists
        try:
            existing_id = load_data(STUDENTS_FILE)
            if any(student_id in line.split(',')[0] for line in existing_id):
                print("Student ID has been registered. Please enter a new ID.")
                continue
        except FileNotFoundError:
            pass # If the file does not exist, treat it as empty
        break

    # Input Student Name
    student_name = input("Enter the student name (or type 'Cancel to exit): ").strip()
    if student_name.lower() == 'cancel':
        print("Action canceled. Returning to manage registrar menu.")
        return
    if not student_name:
        print("Student name cannot be empty.")
        return
    
    # Select Department
    try:
        departments = load_data(DEPARTMENTS_FILE)
        if not departments:
            print("No departments found. Please ensure departments.txt is populated.")
            return

        print("\n--- Available Departments ---")
        for idx, department in enumerate(departments, start=1):
            print(f"{idx}. {department.strip()}")

        while True:
            department_choice = input("Select a department: ").strip()
            if department_choice.isdigit() and 1 <= int(department_choice) <= len(departments):
                selected_department = departments[int(department_choice) - 1].strip()
                break
            else:
                print("Invalid choice. Please enter a valid number corresponsing to a department.")
                return
    except FileNotFoundError:
        print(f"Error: File '{DEPARTMENTS_FILE}' not found.")
        return
    
    # Select Program
    if selected_department in ["Foundation", "Diploma"]:
        # Single file programs
        file_path = os.path.join(FOUNDATION_FILE)
        try:
            programs = load_data(file_path)
            if not programs:
                print(f"No programs found in {selected_department}.")
                return
            
            print(f"\n--- Available Programs in {selected_department} ---")
            for idx, program in enumerate(programs, start=1):
                print(f"{idx}. {program.strip()}")

            while True:
                program_choice = input("Select a program: ").strip()
                if program_choice.isdigit() and 1 <= int(program_choice) <=  len(programs):
                    selected_line = programs[int(program_choice) - 1].strip()
                    selected_program = selected_line.split(',')[1]
                    break
                else:
                    print("Invalid choice. Please enter a valid number corresponsing to a program.")
                    return
        except FileNotFoundError:
            print(f"Error: File for {selected_department} not found.")
            return
    elif selected_department in ["Undergraduate", "Postgraduate"]:
        # Folder-based programs
        folder_path = UNDERGRADUATE_DIR if selected_department == "Undergraduate" else POSTGRADUATE_DIR
        try:
            categories = [f for f in os.listdir(folder_path) if f.endswith(".txt")]
            if not categories:
                print(f"No programs categories found in {selected_department}.")
                return
            
            print(f"\n--- Available Program Categories in {selected_department} ---")
            for idx, category in enumerate(categories, start=1):
                print(f"{idx}. {category.strip()}")

            while True:
                category_choice = input("Select a category: ").strip()
                if category_choice.isdigit() and 1 <= int(category_choice) <= len(categories):
                    selected_category = categories[int(category_choice) - 1]
                    category_path = os.path.join(folder_path, selected_category)
                    programs = load_data(category_path)

                    print(f"\n--- Available Programs in {selected_category.replace('.txt', '').replace('_', ' ')} ---")
                    for idx, program in enumerate(programs, start=1):
                        print(f"{idx}. {program.strip()}")

                    while True:
                        program_choice = input("Select a program: ").strip()
                        if program_choice.isdigit() and 1 <= int(program_choice) <= len(programs):
                            selected_line = programs[int(program_choice) - 1].strip()
                            selected_program = selected_line.split(',')[1]
                            break
                        else:
                            print("Invalid choice. Please enter a valid number corresponding to a program.")
                    break
                else:
                    print("Invalid choice. Please enter a valid number corresponsing to a category.")
        except FileNotFoundError:
            print(f"Error: Directory for {selected_department} not found.")
            return

    # Input Additional Details
    email = input("Enter the student email (optional, press Enter to skip): ").strip()
    if not email:
        email = "N/A"
    contact_number = input("Enter the student contact number (optional, press Enter to skip): ").strip()
    if not contact_number:
        contact_number = "N/A"

    # Combine Student Details
    student_details = f"{student_id},{student_name},{selected_department},{selected_program},{email},{contact_number}"
    
    # Save the Student Details
    try:
        append_data(STUDENTS_FILE, student_details)
        print(f"\nRegistering Student:\nID: {student_id}\nName: {student_name}\nDepartments: {selected_department}\nProgram: {selected_program}\nEmail: {email}\nContact Number: {contact_number}\nStudent Registered Successfully!")
    except Exception as e:
        print(f"Error: Failed to register student. {e}")
