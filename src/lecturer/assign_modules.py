import os
from utils.load_data import load_data
from utils.append_data import append_data
from settings import MODULES_DIR, ASSIGNED_MODULES_FILE, LECTURERS_FILE

def assign_modules():
    """Assign a module to a lecturer."""
    print("\n--- Assign Module to Lecturer ---")

    # Validate Lecturer ID
    lecturer_id = input("Enter the Lecturer ID to assign a module to: ").strip().upper()
    try:
        lecturers = load_data(LECTURERS_FILE)
        if not lecturers:
            print("No lecturers found. Please ensure lecturers.txt is populated.")
            return

        # Validate lecturer entry
        valid_lecturers = [lecturer.split(',') for lecturer in lecturers if len(lecturer.split(',')) >= 3]
        if not any(lecturer_id == lecturer[0].strip() for lecturer in valid_lecturers):
            print(f"Lecturer ID '{lecturer_id}' not found. Please try again.")
            return
    except FileNotFoundError:
        print(f"Error: '{LECTURERS_FILE}' not found.")
        return
    
    # Validate Module Selection
    try:
        print("\nAvailable Module Categories:")
        categories = ["foundation.txt", "diploma.txt", "undergraduate.txt", "postgraduate.txt"]
        for idx, category in enumerate(categories, start=1):
            print(f"{idx}. {category.replace('.txt', '').capitalize()}")
        
        category_choice = input("Select a category: ").strip()
        if not category_choice.isdigit() or int(category_choice)  not in range(1, len(categories) + 1):
            print("Invalid category choice. Please try again.")
            return
        
        selected_category = categories[int(category_choice) - 1].lower()
        module_file = os.path.join(MODULES_DIR, selected_category)

        modules = load_data(module_file)
        if not modules:
            print(f"No modules found in '{module_file}'.")
            return
        
        print("\nAvailable Modules:")
        for idx, module in enumerate(modules, start=1):
            mod_id, mod_name, *_ = module.strip().split(',')
            print(f"{idx}. {mod_id} - {mod_name}")
        
        module_choice = input("Enter the module by number: ").strip()
        if not module_choice.isdigit() or int(module_choice) not in range(1, len(modules) + 1):
            print(f"Invalid module choice. Please try again.")
            return
        
        selected_module = modules[int(module_choice) - 1].strip()
        mod_id, mod_name, *_ = selected_module.split(',')
    except FileNotFoundError:
        print(f"Error: File '{module_file}' not found.")
        return
    
    # Assign Module
    try:
        assigned_entry = f"{mod_id},{mod_name},{lecturer_id}"
        append_data(ASSIGNED_MODULES_FILE, assigned_entry)
        print(f"Module '{mod_id} - {mod_name}' assigned to Lecturer ID '{lecturer_id}.")
    except Exception as e:
        print(f"Error assigning module: {e}")
