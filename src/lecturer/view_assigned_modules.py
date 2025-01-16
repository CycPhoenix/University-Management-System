import os
from utils.load_data import load_data
from settings import MODULES_DIR, LECTURERS_FILE

def view_assigned_modules():
    """Displays the modules assigned to the current lecturer."""
    print("\n--- View Assigned MOdules ---")

    # Validate Lecturer ID
    lecturer_id = input("Enter your Lecturer ID: ").strip()
    try:
        lecturers = load_data(LECTURERS_FILE)
        if not lecturers:
            print("No lecturers found. Please ensure lecturers.txt is populated.")
            return
        
        if not any(lecturer_id == lecturer.split(',')[0] for lecturer in lecturers):
            print(f"Lecturer iD '{lecturer_id}' not found. Please try again.")
            return
    except FileNotFoundError:
        print(f"Error: '{lecturer_id}' not found.")
        return
    
    # Retrieve Modules from MODULES_DIR
    try:
        categories = ["foundation.txt", "diploma.txt", "undergraduate.txt", "postgraduate.txt"]
        assigned_modules = []

        for category in categories:
            module_file = os.path.join(MODULES_DIR, category)
            if not os.path.exists(module_file):
                continue
        
        modules = load_data(MODULES_DIR)
        for module in modules:
            mod_fields = module.strip().split(',')
            mod_id, mod_name, lecturer = mod_fields[:3]
            if lecturer.strip() == lecturer_id:
                assigned_modules.append((mod_id, mod_name, category.replace('.txt', '').capitalize()))

        if not assigned_modules:
            print(f"No modules assigned to Lecturer ID '{lecturer_id}'.")
            return
        
        # Display Assigned Modules
        print(f"\nModules Assigned to Lecutere ID `{lecturer_id}`:")
        for idx, (mod_id, mod_name, category) in enumerate(assigned_modules, start=1):
            print(f"{idx}. {mod_id} - {mod_name} (Category: {category})")
    except Exception as e:
        print(f"Error retrieving modules: {e}")
