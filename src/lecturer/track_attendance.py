import os
from utils.load_data import load_data
from utils.append_data import append_data
from settings import ATTENDANCE_FILE, STUDENTS_FILE, MODULES_DIR

def track_attendance():
    """Allows the lecturer to track attendance for a specific module."""
    print("\n--- Track Attendance ---")

    # Validate Module Selection
    try:
        print("\nAvailable Module Categories:")
        categories = ['Foudation', 'Diploma', 'Undergraduate', 'Postgraduate']
        for idx, category in enumerate(categories, start=1):
            print(f"{idx}. {category}")
        
        category_choice = input("Select a category: ").strip()
        if not category_choice.isdigit() or int(category_choice) not in range(1, len(categories) + 1):
            print("Invalid category choice. Please try again.")
            return
        
        selected_category = categories[int(category_choice) - 1].lower()
        module_file = os.path.join(MODULES_DIR, f"{selected_category}.txt")

        modules = load_data(module_file)
        if not modules:
            print(f"No modules found in '{module_file}")
            return
        
        print("\nAvailable Modules:")
        for idx, module in enumerate(modules, start=1):
            mod_id, mod_name, *_ = module.strip().split(',')
            print(f"{idx}. {mod_id} - {mod_name}")

        module_id = input("Enter the Module ID to track attendance for: ").strip()
        if not any(module_id == module.split(',')[0] for module in modules):
            print(f"Invalid Module ID: {module_id}. Please try again.")
            return
    except FileNotFoundError:
        print(f"Error: File '{module_file}' not found.")
        return
    
    # Display Enrolled Students
    try:
        students = load_data(STUDENTS_FILE)
        if not students:
            print("No students found. Please ensure students.txt is populated.")
            return
        
        print("\nEnrolled Students:")
        enrolled_students = [student.strip() for student in students if student.split(',')[2] == module_id]
        if not enrolled_students:
            print(f"No students are enrolled in module '{module_id}.")
            return
        
        for idx, student in enumerate(enrolled_students, start=1):
            student_fields = student.split(',')
            student_id, name = student_fields[0], student_fields[1]
            print(f"{idx}. {student_id} - {name}")
        
        # Input Attendance
        print("\nmark Attendance (Present/Absent):")
        attendance_records = []
        for student in enrolled_students:
            student_fields = student.split(',')
            student_id, name = student_fields[0], student_fields[1]
            while True:
                status = input(f"{student_id} - {name} (P/A): ").strip().upper()
                if status in ['P', 'A']:
                    attendance_records.append(f"{module_id},{student_id},{status}")
                    break
                else:
                    print("Invalid input. Please enter 'P' for Present or 'A' for Absent.")
        
        # Save Attendance
        try:
            append_data(ATTENDANCE_FILE, "\n".join(attendance_records))
            print("Attendance recorded successfully!")
        except Exception as e:
            print(f"Error saving attendance: {e}")
    except FileNotFoundError:
        print(f"Error: '{STUDENTS_FILE}' not found.")
