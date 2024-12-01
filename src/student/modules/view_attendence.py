import os

def access_attendance_record(student_id):
    # Correct path to access 'attendance.txt' from the root of the project
    file_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'data', 'attendance.txt')

    # Open the attendance.txt file
    with open(file_path, 'r') as file:
        records = file.readlines()
    
    print("Attendance Record:")
    for record in records:
        if record.startswith(student_id):
            _, module_code, attended, total = record.strip().split(',')
            percentage = (int(attended) / int(total)) * 100
            print(f"{module_code}: {percentage:.2f}% attendance")
