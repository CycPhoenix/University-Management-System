from utils.display_choices import display_choices
from admin.lecturers.add_lecturer import add_lecturer
from admin.lecturers.remove_lecturer import remove_lecturer
from admin.lecturers.update_lecturer import update_lecturer
from admin.lecturers.view_all_lecturer import view_all_lecturer


def manage_lecturers():
    """Manage to manage lecturers."""
    while True:
        print("\n--- Manage Lecturers ---")
        options = {
            '1': 'Add Lecturer',
            '2': 'Remove Lecturer',
            '3': 'Update Lecturer',
            '4': 'View All Lecturer',
            '5': 'Back to Admin Menu'
        }
        choice = display_choices(options)

        try:
            if choice == '1':
                add_lecturer()
            elif choice == '2':
                remove_lecturer()
            elif choice == '3':
                update_lecturer()
            elif choice == '4':
                view_all_lecturer()
            elif choice == '5':
                print("Returning to admin menu...")
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error occured: {e}")
