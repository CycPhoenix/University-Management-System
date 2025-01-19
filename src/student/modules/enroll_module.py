import os

def enroll_module(student_id, module_code):
    file_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'data', 'admin_data', 'enrollments.txt')

    # Ensure file exists
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            pass  # Create an empty file if it doesn't exist

    # Read the file to check for existing enrollments
    with open(file_path, 'r') as file:
        records = file.readlines()

    # Check for duplicate enrollment
    for record in records:
        enrolled_student_id, enrolled_module_code = record.strip().split(',')
        if enrolled_student_id == student_id and enrolled_module_code == module_code:
            print(f"Student {student_id} is already enrolled in module {module_code}.")
            return

    # Append new enrollment
    with open(file_path, 'a') as file:
        file.write(f"{student_id},{module_code}\n")
    print(f"Student {student_id} has been successfully enrolled in module {module_code}.")
