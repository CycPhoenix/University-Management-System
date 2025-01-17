import os
from utils.load_data import load_data
from settings import GRADES_FILE, MODULES_DIR, STUDENTS_FILE

def view_student_grades():
    """Allows the lecturer to view grades of students in a specific module."""
    print("\n--- View Student Grades ---")

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

        module_choice = input("Enter the module number to view grades for: ").strip()
        if not module_choice.isdigit() or int(module_choice) not in range(1, len(modules) + 1):
            print(f"Invalid module number: {module_choice}. Please try again.")
            return

        selected_module = modules[int(module_choice) - 1].strip()
        module_id = selected_module.split(',')[0] # Extract Module ID
    except FileNotFoundError:
        print(f"Error: File '{module_file}' not found.")
        return

    # Retrieve Grades
    try:
        grades = load_data(GRADES_FILE)
        if not grades:
            print(f"No grades found in '{GRADES_FILE}'.")
            return

        student_grades = [grade.strip().split(',') for grade in grades if grade.split(',')[0] == module_id]
        if not student_grades:
            print(f"No grades found for module '{module_id}'.")
            return

        print("\nStudent Grades:")
        print(f"{'Student ID':<15}{'Name':<20}{'Grade':<10}")
        print("=" * 50)

        # Retrieve Student Names
        students = load_data(STUDENTS_FILE)
        for grade in student_grades:
            student_id, grade_value = grade[1], grade[2]
            student_name = next((student.split(',')[1] for student in students if student.split(',')[0] == student_id), 'Unknown')
            print(f"{student_id:<15}{student_name:<20}{grade_value:<10}")
    except FileNotFoundError:
        print(f"Error: File '{GRADES_FILE}' not found.")
    except Exception as e:
        print(f"Error retrieving grades: {e}")
