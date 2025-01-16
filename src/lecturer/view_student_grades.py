import os
from utils.load_data import load_data
from settings import GRADES_FILE, STUDENTS_FILE, MODULES_DIR

def view_student_grades():
    """Allows the lecturer to view student grades for a specific module."""
    print("\n--- View Student Grades ---")

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

        modules = load_data(MODULES_DIR)
        if not modules:
            print(f"No modules found in '{module_file}'.")
            return
        
        print("\nAvailable Modules:")
        for idx, module in enumerate(modules, start=1):
            mod_id, mod_name, *_ = module.strip().split(',')
            print(f"{idx}. {mod_id} - {mod_name}")

        module_id = input("Enter the Module ID to view grades for: ").strip()
        if not any (module_id == module.split(',')[0] for module in modules):
            print("Invalid category choice. Please try again.")
            return
        
        selected_category = category[int(category_choice) - 1].lower()
        module_file = os.path.join(MODULES_DIR, f"{selected_category}")

        modules = load_data(module_file)
        if not modules:
            print(f"No modules found in '{module_file}'.")
            return
        
        print("\nAvailable Modules:")
        for idx, module in enumerate(modules, start=1):
            mod_id, mod_name, *_ = module.strip().split(',')
            print(f"{idx}. {mod_id} - {mod_name}")
        
        module_id = input("Enter the Module ID to view grades for: ").strip()
        if not any(module_id == module.split(',')[0] for module in modules):
            print(f"Invalid Module ID: {module_id}. Please try again.")
            return
    except FileNotFoundError:
        print(f"Error: File '{module_file}' not found.")
        return
    
    # Retrieve Grades for the Module
    try:
        grades = load_data(GRADES_FILE)
        if not grades:
            print(f"No grades recorded for module '{module_id}'.")
            return
        
        students = load_data(STUDENTS_FILE)
        if not students:
            print("No students found. Please ensure students.txt is populated.")
            return
        
        print("\nStudent Grades:")
        print(f"{'Student ID':<15}{'Name':<20}{'Marks':<20}{'Letter Grade':<15}")
        print("=" * 70)

        grades_for_module = [grade.strip().split(',') for grade in grades if grade.split(',')[0] == module_id]
        if not grades_for_module:
            print(f"No grades found for module '{module_id}'.")
            return
        
        for grade_entry in grades_for_module:
            _, student_id, numerical_grade, letter_grade = grade_entry
            student_name = next((student.split(',')[1] for student in students if student.split(',')[0] == student_id), 'N/A')
            print(f"{student_id:<15}{student_name:<20}{numerical_grade:<20}{letter_grade:<15}")
    except FileNotFoundError:
        print(f"Error: Required file(s) not found.")
    except Exception as e:
        print(f"Error retrieving grades: {e}")
