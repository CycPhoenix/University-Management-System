from admin.lecturers.add_lecturer import add_lecturer
from admin.lecturers.remove_lecturer import remove_lecturer
from admin.lecturers.update_lecturer import update_lecturer
from admin.lecturers.view_all_lecturers import view_all_lecturers

def manage_lecturers():
    """Menu to manage lecturers."""
    while True:
        print("\n--- Manage Lecturers ---")
        options = {
            '1': 'Add Lecturer',
            '2': 'Remove Lecturer',
            '3': 'Update Lecturer',
            '4': 'View All Lecturers',
            '5': 'Back to Admin Menu'
        }
        choice = display_choices(options)

        if choice == '1':
            try:
                add_lecturer()
            except Exception as e:
                print(f"An error occurred while adding a lecturer: {e}")
        elif choice == '2':
            try:
                remove_lecturer()
            except Exception as e:
                print(f"An error occurred while removing a lecturer: {e}")
        elif choice == '3':
            try:
                update_lecturer()
            except Exception as e:
                print(f"An error occurred while updating a lecturer: {e}")
        elif choice == '4':
            try:
                view_all_lecturers()
            except Exception as e:
                print(f"An error occurred while viewing lecturers: {e}")
        elif choice == '5':
            print("Returning to admin menu...")
            break
        else:
            print("Invalid choice. Please try again.")
