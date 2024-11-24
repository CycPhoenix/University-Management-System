from utils.display_choices import display_choices
from admin.students.add_student import add_student
from admin.students.remove_student import remove_student
from admin.students.update_student import update_student
from admin.students.view_all_students import view_all_students


def manage_students():
    """Menu to manage students."""
    while True:
        print("\n--- Manage Students ---")
        options = {
            '1': 'Add Student',
            '2': 'Remove Student',
            '3': 'Update Student',
            '4': 'View All Students',
            '5': 'Back to Admin Menu'
        }
        choice = display_choices(options)

        try:
            if choice == '1':
                add_student()
            elif choice == '2':
                remove_student()
            elif choice == '3':
                update_student()
            elif choice == '4':
                view_all_students()
            elif choice == '5':
                print("Returning to admin menu...")
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")
