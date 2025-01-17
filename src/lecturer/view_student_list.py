import os
from utils.load_data import load_data
from settings import STUDENTS_FILE, MODULES_DIR

def view_student_list():
    """Allows the lecturer to view the list of students enrolled in a specific module."""
    print("\n--- View Student List ---")

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

        module_choice = input("Enter the module number to view student list for: ").strip()
        if not module_choice.isdigit() or int(module_choice) not in range(1, len(modules) + 1):
            print(f"Invalid module number: {module_choice}. Please try again.")
            return

        selected_module = modules[int(module_choice) - 1].strip()
        module_id = selected_module.split(',')[0] # Extract the Module ID
    except FileNotFoundError:
        print(f"Error: File '{module_file}' not found.")
        return

    # Retrieve Students Enrolled in the Module
    try:
        students = load_data(STUDENTS_FILE)
        if not students:
            print("No students found. Please ensure students.txt is populated.")
            return

        enrolled_students = [student.strip().split(',') for student in students if student.split(',')[2] == module_id]
        if not enrolled_students:
            print(f"No students are enrolled in module '{module_id}'.")
            return

        print("\nEnrolled Students:")
        print(f"{'Student ID':<15}{'Name':<20}{'Email':<30}{'Contact Number':<15}")
        print("=" * 85)

        for student in enrolled_students:
            student_id, name, _, email, contact_number = student
            print(f"{student_id:<15}{name:<20}{email:<30}{contact_number:<15}")
    except FileNotFoundError:
        print(f"Error: '{STUDENTS_FILE}' not found.")
    except Exception as e:
        print(f"Error retrieving student list: {e}")
