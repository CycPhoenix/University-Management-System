import os
from utils.load_data import load_data
from utils.append_data import append_data
from settings import GRADES_FILE, STUDENTS_FILE, MODULES_DIR

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
    print("--- Record Grades ---")

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
            print(f"{idx}, {mod_id} - {mod_name}")
        
        module_id = input("Enter the Module ID to record grades for: ").strip()
        if not any (module_id == module.split(',')[0] for module in modules):
            print(f"Invalid Module ID: {module_id}. Please try again.")
            return
    except FileNotFoundError:
        print(f"Error: File '{module_file}' not found.")
        return
    
    # Validate Student ID
    try:
        students = load_data(STUDENTS_FILE)
        if not students:
            print("No students found. Please ensure students.txt is populated.")
            return
        
        print("\nEnrolled Students:")
        for student in students:
            student_fields = student.strip().split(',')
            student_id, name, enrolled_module = student_fields[:5]
            if enrolled_module == module_id:
                print(f"{student_id} - {name}")
        
        student_id = input("Enter the Student ID to record grades for: ").strip()
        if not any(student_id == student.split(',')[0] for student in students):
            print(f"Invalid Student ID: {student_id}. Please try again.")
            return
    except FileNotFoundError:
        print(f"Error: '{STUDENTS_FILE}' not found.")
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
    grade_entry = f"{module_id},{student_id},{numeric_grade},{letter_grade}"
    try:
        append_data(GRADES_FILE, grade_entry)
        print(f"Grade `{letter_grade}` ({numeric_grade}) recorded successfully for Student ID '{student_id}' in Module '{module_id}.")
    except Exception as e:
        print(f"Error recording grade: {e}")