import os
from utils.load_data import load_data
from utils.append_data import append_data
from settings import GRADES_FILE, STUDENTS_FILE,ENROLLMENTS_FILE, MODULES_DIR

# Grade mapping based on the provided ranges
GRADE_MAPPING = {
    "A+": range(80, 100),
    "A": range(75, 79),
    "B+": range(70, 74),
    "B": range(65, 69),
    "C+": range(60, 65),
    "C": range(55, 59),
    "C-": range(50, 54),
    "D": range(40, 49),
    "F+": range(30, 39),
    "F": range(20, 29),
    "F-": range(0, 19),
}

def get_letter_grade(score):
    """Converts a numerical grade to a letter grade."""
    for letter, grade_range in GRADE_MAPPING.items():
        if score in grade_range:
            return letter
    return "Invalid" # Handle out of range values

def record_grades():
    """Allows the lecturer to record grades for students in a specific module."""
    print("\n--- Record Grades ---")

    # Validate Module Selection
    try:
        print("\nAvailable Module Categories:")
        categories = ["Foundation", "Diploma", "Undergraduate", "Postgraduate"]
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
            print(f"No modules found in '{module_file}'.")
            return
        
        print("\nAvailable Modules:")
        for idx, module in enumerate(modules, start=1):
            mod_id, mod_name, *_ = module.strip().split(',')
            print(f"{idx}. {mod_id} - {mod_name}")
        
        while True:
            module_choice = input("Select a module by index: ").strip()
            if module_choice.isdigit() and 1 <= int(module_choice) <= len(modules):
                selected_module = modules[int(module_choice) - 1]
                module_id, module_name, *_ = selected_module.strip().split(',')
                print(f"Selected Module: {module_name} (ID: {module_id})")
                break
            else:
                print("Invalid choice. Please enter a valid module index.")
    except FileNotFoundError:
        print(f"Error: File '{module_file}' not found.")
        return
    
    # Get enrolled students from enrollments.txt
    try:
        enrollments = load_data(ENROLLMENTS_FILE)
        if not enrollments:
            print("No enrollments found. Please ensure enrollments.txt is populated.")
            return

        enrolled_students = [
            enrollment.strip().split(',')[0]
            for enrollment in enrollments if module_name in enrollment.split(',')[1]
        ]

        if not enrolled_students:
            print(f"No students are enrolled in module '{module_id}'.")
            return

        # Map student IDs to their full names from students.txt
        students = load_data(STUDENTS_FILE)
        enrolled_students_data = []
        for student in students:
            student_fields = student.strip().split(',')
            student_id, name = student_fields[0], student_fields[1]
            if student_id in enrolled_students:
                enrolled_students_data.append((student_id, name))

        print("\nEnrolled Students:")
        for idx, (student_id, name) in enumerate(enrolled_students_data, start=1):
            print(f"{idx}. {name} (ID: {student_id})")

        while True:
            student_choice = input("Select a student by index: ").strip()
            if student_choice.isdigit() and 1 <= int(student_choice) <= len(enrolled_students_data):
                selected_student_id, selected_student_name = enrolled_students_data[int(student_choice) - 1]
                print(f"Selected Student: {selected_student_name} (ID: {selected_student_id})")
                break
            else:
                print("Invalid choice. Please enter a valid student index.")
    except FileNotFoundError:
        print(f"Error: File '{ENROLLMENTS_FILE}' or '{STUDENTS_FILE}' not found.")
        return
    
    # Input Numerical Grade and Convert to Letter Grade
    while True:
        try:
            numeric_grade = int(input("Enter the numerical grade (0-100): ").strip())
            if 0 <= numeric_grade <= 100:
                letter_grade = get_letter_grade(numeric_grade)
                if letter_grade == "Invalid":
                    print("Error: Could not map numerical grade to a valid letter grade. Please try again.")
                else:
                    break
            else:
                print("Grade must be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numerical value between 0 and 100.")
    
    # Record Grade
    grade_entry = f"{module_id},{selected_student_id},{numeric_grade},{letter_grade}"
    try:
        append_data(GRADES_FILE, grade_entry)
        print(f"Grade `{letter_grade}` ({numeric_grade}) recorded successfully for Student '{selected_student_name}' in Module '{module_name}'.")
    except Exception as e:
        print(f"Error recording grade: {e}")
