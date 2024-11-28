from admin.courses.add_course import add_course
from admin.courses.remove_course import remove_course
from admin.courses.update_course import update_course
from admin.courses.view_all_courses import view_all_courses

def manage_courses():
    """Manage courses in the system."""
    mc_art = r"""
     __ __                            ___                             
    |  \  \ ___ ._ _  ___  ___  ___  |  _> ___  _ _  _ _  ___ ___  ___    
    |     |<_> || ' |<_> |/ . |/ ._> | <__/ . \| | || '_><_-</ ._><_-<
    |_|_|_|<___||_|_|<___|\_. |\___. `___/\___/`___||_|  /__/\___./__/
                          <___'                                       
    """
    separator_length = max(len(line) for line in mc_art.splitlines())
    separator = "=" * separator_length
    
    while True:
        print()
        print(separator)
        print(mc_art)
        print(separator)
        print("\nSelect an option:")
        print("1. Add Course")
        print("2. Remove Course")
        print("3. Update Course")
        print("4. View All Courses")
        print("5. Back to Admin Menu")

        choice = input("\nEnter your choice: ").strip()

        if choice == '1':
            try:
                add_course()
            except Exception as e:
                print(f"An error occurred while adding a course: {e}")
        elif choice == '2':
            try:
                remove_course()
            except Exception as e:
                print(f"An error occurred while removing a course: {e}")
        elif choice == '3':
            try:
                update_course()
            except Exception as e:
                print(f"An error occurred while updating a course: {e}")
        elif choice == '4':
            try:
                view_all_courses()
            except Exception as e:
                print(f"An error occurred while viewing courses: {e}")
        elif choice == '5':
            print("Returning to admin menu...")
            break
        else:
            print("Invalid choice. Please try again.")
