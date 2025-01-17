import os
from datetime import datetime
from utils.load_data import load_data
from utils.write_data import write_data
from settings import ATTENDANCE_FILE, STUDENTS_FILE, MODULES_DIR

def track_attendance():
    """Allows the lecturer to track attendance for a specific module."""
    print("\n--- Track Attendance ---")

    # Validate Module Selection
    try:
        print("\nAvailable Module Categories:")
        categories = ['foundation.txt', 'diploma.txt', 'undergraduate.txt', 'postgraduate.txt']
        for idx, category in enumerate(categories, start=1):
            print(f"{idx}. {category.replace('.txt', '').capitalize()}")
        
        category_choice = input("Select a category: ").strip()
        if not category_choice.isdigit() or int(category_choice) not in range(1, len(categories) + 1):
            print("Invalid category choice. Please try again.")
            return
        
        selected_category = categories[int(category_choice) - 1]
        module_file = os.path.join(MODULES_DIR, selected_category)

        print(f"Loading modules from: {module_file}")
        modules = load_data(module_file)
        if not modules:
            print(f"No modules found in '{module_file}'.")
            return
        
        print("\nAvailable Modules:")
        for idx, module in enumerate(modules, start=1):
            mod_id, mod_name, *_ = module.strip().split(',')
            print(f"{idx}. {mod_id} - {mod_name}")

        module_choice = input("Enter the module number to track attendance for: ").strip()
        if not module_choice.isdigit() or int(module_choice) not in range(1, len(modules) + 1):
            print(f"Invalid module number: {module_choice}. Please try again.")
            return

        selected_module = modules[int(module_choice) - 1].strip()
        module_id = selected_module.split(',')[0] # Extract Module ID
    except FileNotFoundError:
        print(f"Error: File '{module_file}' not found.")
        return

    # Prompt for Attendance Date
    attendance_date = input("\nEnter the date for attendance (YYYY-MM-DD) or press Enter for today's date: ").strip()
    if not attendance_date:
        attendance_date = datetime.today().strftime('%Y-%m-%d')
    else:
        try:
            datetime.strptime(attendance_date, '%Y-%m-%d') # Validate the date format
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return

    # Display Enrolled Students
    try:
        students = load_data(STUDENTS_FILE)
        if not students:
            print("No students found. Please ensure students.txt is populated.")
            return
        
        enrolled_students = [student.strip() for student in students if student.split(',')[2] == module_id]
        if not enrolled_students:
            print(f"No students are enrolled in module '{module_id}'.")
            return
        
        print("\nEnrolled Students:")
        for idx, student in enumerate(enrolled_students, start=1):
            student_fields = student.split(',')
            student_id, name = student_fields[0], student_fields[1]
            print(f"{idx}. {student_id} - {name}")
        
        # Load Existing Attendance Records
        try:
            existing_records = load_data(ATTENDANCE_FILE)
            attendance_records = [
                record.strip().split(',') for record in existing_records if record.split(',')[0] == module_id
            ]
        except FileNotFoundError:
            existing_records = []
            attendance_records = []

        # Input Attendance
        print("\nMark Attendance (Present/Absent):")
        new_records = []
        for student in enrolled_students:
            student_fields = student.split(',')
            student_id, name = student_fields[0], student_fields[1]

            # Check if attendance already exists for this date and student
            existing_record = next(
                (record for record in attendance_records if record[1] == student_id and record[2] == attendance_date),
                None
            )
            if existing_record:
                print(f"Attendance already marked for {student_id} - {name} on {attendance_date}.")
                continue

            # Mark Attendance
            while True:
                status = input(f"{student_id} - {name} (P/A): ").strip().upper()
                if status in ['P', 'A']:
                    new_records.append(f"{module_id},{student_id},{attendance_date},{status}")
                    break
                else:
                    print("Invalid input. Please enter 'P' for Present or 'A' for Absent.")
        
        # Save Attendance
        try:
            combined_records = existing_records + new_records
            combined_records.sort(key=lambda x: datetime.strptime(x.split(',')[2], '%Y-%m-%d')) # Sort by date
            write_data(ATTENDANCE_FILE, combined_records)
            print("Attendance recorded successfully!")
        except Exception as e:
            print(f"Error saving attendance: {e}")
    except FileNotFoundError:
        print(f"Error: '{STUDENTS_FILE}' not found.")
