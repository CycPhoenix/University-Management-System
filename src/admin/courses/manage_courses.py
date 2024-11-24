from utils.display_choices import display_choices
from admin.courses.add_course import add_course
from admin.courses.remove_course import remove_course
from admin.courses.update_course import update_course
from admin.courses.view_all_courses import view_all_courses


def manage_courses():
    """Manage courses in the system."""
    while True:
        print("\n--- Manage Courses ---")
        options = {
            '1': 'Add Course',
            '2': 'Remove Course',
            '3': 'Update Course',
            '4': 'View All Courses',
            '5': 'Back to Admin Menu'
        }
        choice = display_choices(options)

        try:
            if choice == '1':
                add_course()
            elif choice == '2':
                remove_course()
            elif choice == '3':
                update_course()
            elif choice == '4':
                view_all_courses()
            elif choice == '5':
                print("Returning to admin menu...")
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error occured: {e}")
