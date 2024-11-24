from utils.display_choices import display_choices
from utils.load_data import load_data
from utils.write_data import write_data
from settings import STUDENTS_FILE


def update_student():
    """Update a student's details."""
    print("\n--- Update Student ---")

    # Load existing students
    try:
        students = load_data(STUDENTS_FILE)
        if not students:
            print("No students found. Please add students first.")
            return
    except FileNotFoundError:
        print(f"Error: File '{STUDENTS_FILE}' not found.")
        return
    except Exception as e:
        print(f"Error: Failed to load students. {e}")
        return
    
    # Display students and select one to update
    student_options = {str(i + 1): student.strip() for i, student in enumerate(students)}
    student_options[str(len(students) + 1)] = 'Cancel'

    print("\n--- Existing Students ---")
    for idx, student in student_options.items():
        if idx != str(len(students) + 1):
            print(f"{idx}. {student.strip()}")

    choice = input(f"\nSelect a student to update (1-{len(students)}) or type '{len(students) + 1}' to cancel: ").strip()
    if choice == str(len(students) + 1):
        print("Action canceled. Returning to manage students menu.")
        return
    
    if choice not in student_options:
        print("Invalid choice. Please try again.")
        return
    
    selected_student = student_options[choice]
    print(f"Selected student: {selected_student.strip()}")

    # Split the student record into fields
    student_fields = selected_student.split(',')
    if len(student_fields) != 5:
        print("Error: Selected student data is corrupted or invalid.")
        print(f"Debug: Corrupted data -> {selected_student}")
        return
    
    student_id, student_name, department, email, contact_number = [field.strip() for field in student_fields]

    # Update fields
    new_id = input(f"Enter new Student ID (press Enter to keep '{student_id}'): ").strip() or student_id
    new_name = input(f"Enter new Name (press Enter to keep '{student_name}'): ").strip() or student_name
    new_department = input(f"Enter new Department (press Enter to keep '{department}'): ").strip() or department
    new_email = input(f"Enter new Email (press Enter to keep '{email}'): ").strip() or email
    new_contact_number = input(f"Enter new Contact Number (press Enter to keep '{contact_number}'): ").strip() or contact_number

    # Combine updated fields
    updated_student = f"{new_id.strip()},{new_name.strip()},{new_department.strip()},{new_email.strip()},{new_contact_number.strip()}"
    
    # Write updated data to the file
    try:
        with open(STUDENTS_FILE, 'w', encoding='utf-8') as f:
            for student in students:
                if student.strip() == selected_student:
                    f.write(f"{updated_student}\n")
                else:
                    f.write(f"{student.strip()}\n")
        print(f"Student '{new_name}' updated successfully!")
    except Exception as e:
        print(f"Error: Could not write updates to '{STUDENTS_FILE}'. {e}")
