import os
from settings import ATTENDANCE_FILE

def access_attendance_record(student_id):
    # Correct path to access 'attendance.txt' from the root of the project
    file_path = ATTENDANCE_FILE

    # Open the attendance.txt file
    with open(file_path, 'r') as file:
        records = file.readlines()
        
    print("Attendance Record")
    found = False
    for record in records:
        # Split the record by commas
        parts = record.strip().split(',')
        if parts[0] == student_id:  # If the student_id matches
            module_code, attended, total = parts[1], int(parts[2]), int(parts[3])
            percentage = (attended / total) * 100
            print(f"{module_code}: {percentage:.2f}% attendance")
            found = True

    if not found:
        print(f"No attendance record found for student ID {student_id}.")
