from utils.display_choices import display_choices
from utils.load_data import load_data
from utils.write_data import write_data
from settings import LECTURERS_FILE


def update_lecturer():
    """Update a lecturer's details."""
    print("\n--- Update Lecturer ---")

    # Load existing lecturers
    try:
        lecturers = load_data(LECTURERS_FILE)
        if not lecturers:
            print("No lecturers found. Please add lecturers first.")
            return
    except FileNotFoundError:
        print(f"Error: File '{LECTURERS_FILE}' not found.")
        return
    except Exception as e:
        print(f"Error: Failed to load lecturers. {e}")
        return
    
    # Display lecturers and select one to update
    lecturer_options = {str(i + 1): lecturer for i, lecturer in enumerate(lecturers)}
    lecturer_options[str(len(lecturers) + 1)] = 'Cancel'

    print("\n--- Existing Lecturers ---")
    for idx, lecturer in lecturer_options.items():
        if idx != str(len(lecturers) + 1):
            print(f"{idx}. {lecturer.strip()}")

    choice = input(f"\nSelect a lecturer to update (1-{len(lecturers)}) or type '{len(lecturers) + 1}' to cancel: ").strip()
    if choice == str(len(lecturers) + 1):
        print("Action canceled. Returning to manage lecturers menu.")
        return

    if choice not in lecturer_options:
        print("Invalid choice. Please try again.")
        return
    
    selected_lecturer = lecturer_options[choice]
    print(f"Selected lecturer: {selected_lecturer.strip()}")

    # Split the lecturer record into fields
    lecturer_fields = selected_lecturer.split(',')
    if len(lecturer_fields) != 5:
        print("Error: Selected lecturer data is corrupted or invalid.")
        print(f"Debug: Corrupted data -> {selected_lecturer}")
        return
    
    lecturer_id, lecturer_name, department, email, contact_number = [field.strip() for field in lecturer_fields]

    # Update Fields
    new_id = input(f"Enter new Lecturer ID (press Enter to keep '{lecturer_id}): ").strip() or lecturer_id
    new_name = input(f"Enter new Name (press Enter to keep '{lecturer_name}): ").strip() or lecturer_name
    new_department = input(f"Enter new Department (press Enter to keep '{department}): ").strip() or department
    new_email = input(f"Enter new Email (press Enter to keep '{email}): ").strip() or email
    new_contact_number = input(f"Enter new Contact Number (press Enter to keep '{contact_number}): ").strip() or contact_number

    # Combine updated fields
    updated_lecturer = f"{new_id.strip()},{new_name.strip()},{new_department.strip()},{new_email.strip()},{new_contact_number.strip()}"
    
    # Write updated data to the file
    try:
        with open(LECTURERS_FILE, 'w', encoding='utf-8') as f:
            for lecturer in lecturers:
                if lecturer.strip() == selected_lecturer:
                    f.write(f"{updated_lecturer}\n")
                else:
                    f.write(f"{lecturer.strip()}\n")
        print(f"Lecturer '{new_name}' updated successfully!")
    except Exception as e:
        print(f"Error: Could not write updates to '{LECTURERS_FILE}'. {e}")