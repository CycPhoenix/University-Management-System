import os
from utils.load_data import load_data
from utils.write_data import write_data
from settings import ENROLLMENTS_FILE

def unenroll_student(student_id, enrollments):
    """Unenroll a student from a module"""
    # Load enrollments
    try:
        enrollments = load_data(ENROLLMENTS_FILE)
    except FileNotFoundError:
        print(f"Error: File '{ENROLLMENTS_FILE}' not found.")

    # Filter the student's enrollments
    student_enrollments = [line for line in enrollments if line.startswith(student_id)]
    if not student_enrollments:
        print(f"No enrollments found for student {student_id}.")
        return
    
    # Display the student's current enrollments
    print("\n--- Current Enrollments ---")
    for idx, line in enumerate(student_enrollments, start=1):
        module_code = line.strip().split(',')[1]
        print(f"{idx}. Module Code: {module_code}")

    # Select a module to unenroll from
    module_choice = input("Select a module to unenroll from (or type 'Cancel' to exit): ").strip()
    if module_choice.lower() == 'cancel':
        print("Action canceled.")
        return
    
    if not module_choice.isdigit() or not (1 <= int(module_choice) <= len(student_enrollments)):
        print("Invalid choice. No changes made.")
        return
    
    # Remove the selected enrollment
    selected_enrollment = student_enrollments[int(module_choice) - 1]
    enrollments.remove(selected_enrollment)

    # Write the updated enrollments back to the file
    write_data(ENROLLMENTS_FILE, enrollments)
    print(f"Successfully unenrolled from module {selected_enrollment.split(',')[1]}.")
