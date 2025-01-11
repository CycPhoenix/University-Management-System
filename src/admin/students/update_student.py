import os
from utils.load_data import load_data
from utils.write_data import write_data
from settings import STUDENTS_FILE, DEPARTMENTS_FILE, FOUNDATION_FILE, DIPLOMA_FILE, UNDERGRADUATE_DIR, POSTGRADUATE_DIR

def update_student():
    """Update a student's details."""
    us_art = r"""
     _ _         _        _         ___    _          _             _      
    | | | ___  _| | ___ _| |_ ___  / __> _| |_ _ _  _| | ___ ._ _ _| |_ 
    | ' || . \/ . |<_> | | | / ._> \__ \  | | | | |/ . |/ ._>| ' | | |  
    `___'|  _/\___|<___| |_| \___. <___/  |_| `___|\___|\___.|_|_| |_|  
         |_|                                                            
    """
    separator_length = max(len(line) for line in us_art.splitlines())
    separator = "=" * separator_length

    print()
    print(separator)
    print(us_art)
    print(separator)

    # Load existing students
    try:
        students = load_data(STUDENTS_FILE)
        if not students:
            print("No students found. Please add students first.")
            return
    except FileNotFoundError:
        print(f"Error: File '{STUDENTS_FILE}' not found.")
        return
    
    # Search for the student by ID
    student_id = input("Enter the Student ID to update (or type 'Cancel' to exit): ").strip().upper()
    if student_id.lower() == 'cancel':
        print("Action canceled. Returning to registrar menu.")
        return
    
    # Find the student record
    found = False
    updated_students = []
    for line in students:
        student_data = line.strip().split(',')
        if student_data[0] == student_id:
            found = True
            print(f"\nCurrent Details:\nID: {student_data[0]}\nName: {student_data[1]}\nDepartment: {student_data[2]}\nProgram: {student_data[3]}\nEmail: {student_data[4]}\nContact Number: {student_data[5]}")

            # Update Name
            new_name = input(f"Enter new Name (press Enter to keep current): ").strip() or student_data[1]
            if not new_name:
                new_name = student_data[1]

            # Update Department
            try:
                departments = load_data(DEPARTMENTS_FILE)
                if not departments:
                    print("No deparments found in departments.txt.")
                    return
                
                print("\n--- Available Departments ---")
                for idx, department in enumerate(departments, start=1):
                    print(f"{idx}. {department.strip()}")

                while True:
                    department_choice = input("Select a department (or press Enter to keep current): ").strip()
                    if not department_choice:
                        new_department = student_data[2]
                        break
                    if department_choice.isdigit() and 1 <= int(department_choice) <= len(departments):
                        new_department = departments[int(department_choice) - 1].strip()
                        break
                    else:
                        print("Invalid choice. Please enter a valid number corresponding to a department.")
            except FileNotFoundError:
                print(f"Error: File '{DEPARTMENTS_FILE}' not found.")
                return
            
            # Update Program
            if new_department in ["Foundation", "Diploma"]:
                if new_department == "Foundation":
                    file_path = os.path.join(FOUNDATION_FILE)
                elif new_department == "Diploma":
                    file_path = os.path.join(DIPLOMA_FILE)

                try:
                    programs = load_data(file_path)
                    if not programs:
                        print(f"No programs found in {new_department}.")
                        return
                    print(f"\n--- Available Programs in {new_department} ---")
                    for idx, program in enumerate(programs, start=1):
                        print(f"{idx}. {program.strip()}")

                    while True:
                        program_choice = input("Select a program (or press Enter to keep current): ").strip()
                        if not program_choice:
                            new_program = student_data[3]
                            break
                        if program_choice.isdigit() and 1 <= int(program_choice) <= len(programs):
                            selected_line = programs[int(program_choice) - 1].strip()
                            new_program = selected_line.split(',')[1]
                            break
                        else:
                            print("Invalid choice. Please enter a valid number corresponding to a program.")
                except FileNotFoundError:
                    print(f"Error: File for {new_department} not found.")
                    return
                
            if new_department in ["Undergraduate", "Postgraduate"]:
                folder_path = UNDERGRADUATE_DIR if new_department == "Undergraduate" else POSTGRADUATE_DIR
                try:
                    categories = [f for f in os.listdir(folder_path) if f.endswith(".txt")]
                    if not categories:
                        print(f"No program categories found in {new_department}.")
                        return
                    
                    print(f"\n--- Available Program Categories in {new_department} ---")
                    for idx, category in enumerate(categories, start=1):
                        print(f"{idx}. {category.replace('.txt', '').replace('_', ' ')}")

                    while True:
                        category_choice = input("Select a program (or press Enter to keep current): ").strip()
                        if not category_choice:
                            new_program = student_data[3]
                            break
                        if category_choice.isdigit() and 1 <= int(category_choice) <= len(categories):
                            selected_category = categories[int(category_choice) - 1]
                            category_path = os.path.join(folder_path, selected_category)
                            programs = load_data(category_path)
                            
                            print(f"\n--- Available Programs in {selected_category.replace('.txt', '').replace('_', ' ')} ---")
                            for idx, program in enumerate(programs, start=1):
                                print(f"{idx}. {program.strip()}")

                            while True:
                                program_choice = input("Select a program (or press Enter to keep current): ").strip()
                                if not program_choice:
                                    new_program = student_data[3]
                                    break
                                if program_choice.isdigit() and 1 <= int(program_choice) <= len(programs):
                                    selected_line = programs[int(program_choice) - 1].strip()
                                    new_program = selected_line.split(',')[1]
                                    break
                                else:
                                    print("Invalid choice. Please enter a valid number corresponding to a program.")
                            break
                        else:
                            print("Invalid choice. Please enter a valid number corresponding to a category.")
                except FileNotFoundError:
                    print(f"Error: Directory for {new_department} not found.")
                    return
                
            new_email = input(f"Enter new Email (press Enter to keep current): ").strip() or student_data[4]
            if not new_email:
                new_email = student_data[4]

            new_contact_number = input(f"Enter new Contact Number (press Enter to keep current): ").strip() or student_data[5]
            if not contact_number:
                contact_number = student_data[5]
            
            # Append updated student data
            updated_students.append(f"{student_data[0],{new_name},{new_department},{new_program},{new_email},{new_contact_number}}")
        else:
            updated_students.append(line)
    if not found:
        print(f"Student with ID '{student_id}' not found.")
        return
    
    # Save updated records
    try:
        write_data(STUDENTS_FILE, updated_students)
        print(f"\nStudent record with ID '{student_id}' updated successfully.")
    except Exception as e:
        print(f"Error: Failed to update student. {e}")
