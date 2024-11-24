from utils.display_choices import display_choices
from utils.load_data import load_data
from utils.write_data import write_data
from settings import LECTURERS_FILE


def remove_lecturer():
    """Remove a lecturer from the system."""
    print("\n--- Remove Lecturer ---")

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
    
    # Display lecturers and select one to remove
    lecturer_options = {str(i + 1): lecturer for i, lecturer in enumerate(lecturers)}
    lecturer_options[str(len(lecturers) + 1)] = 'Cancel'

    print("\n--- Existing Lecturers ---")
    for idx, lecturer in lecturer_options.items():
        if idx != str(len(lecturers) + 1):
            print(f"{idx}. {lecturer.strip()}")

    choice = input(f"\nSelect a lecturer to remove (1-{len(lecturers)}) or type '{len(lecturers) + 1}' to cancel: ").strip()
    if choice == str(len(lecturers) + 1):
        print("Action canceled. Returning to manage lecturers menu.")
        return

    if choice not in lecturer_options:
        print("Invalid choice. Please try again.")
        return
    
    selected_lecturer = lecturer_options[choice]
    print(f"Selected lecturer: {selected_lecturer.strip()}")

    # Confirm removal
    confirmation = input(f"Are you sure you want to remove '{selected_lecturer.strip()}'? (yes/no): ").strip().lower()
    if confirmation != 'yes':
        print("Action canceled. Returning to manage lecturers menu.")
        return
        
    # Update lecturer file
    try:
        with open(LECTURERS_FILE, 'w', encoding='utf-8') as f:
            for lecturer in lecturers:
                if lecturer != selected_lecturer:
                    f.write(f"{lecturer.strip()}\n")
        print(f"Lecturer '{selected_lecturer.strip()}' removed successfully!")
    except Exception as e:
        print(f"Error: Failed to remove lecturer. {e}")
