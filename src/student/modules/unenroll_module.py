import os

def unenroll_module(student_id, module_code):
    # Construct the path to enrollments.txt
    file_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'data', 'admin_data', 'enrollments.txt')

    # Check if the file exists
    if not os.path.exists(file_path):
        print("No enrollment records found.")
        return

    # Read the existing enrollments
    with open(file_path, 'r') as file:
        records = file.readlines()

    # Filter out the record to be unenrolled
    updated_records = []
    found = False
    for record in records:
        enrolled_student_id, enrolled_module_code = record.strip().split(',')
        if enrolled_student_id == student_id and enrolled_module_code == module_code:
            found = True
        else:
            updated_records.append(record)

    # If the record was not found
    if not found:
        print(f"No enrollment found for Student ID: {student_id} in Module: {module_code}.")
        return

    # Write the updated records back to the file
    with open(file_path, 'w') as file:
        file.writelines(updated_records)

    print(f"Student {student_id} has been successfully unenrolled from module {module_code}.")