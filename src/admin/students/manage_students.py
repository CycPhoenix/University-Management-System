from admin.students.add_student import add_student
from admin.students.remove_student import remove_student
from admin.students.update_student import update_student
from admin.students.view_all_students import view_all_students

def manage_students():
    """Menu to manage students."""
    ms_art = r"""
     __ __                            ___    _          _             _          
    |  \  \ ___ ._ _  ___  ___  ___  / __> _| |_ _ _  _| | ___ ._ _ _| |_ ___
    |     |<_> || ' |<_> |/ . |/ ._> \__ \  | | | | |/ . |/ ._>| ' | | | <_-<
    |_|_|_|<___||_|_|<___|\_. |\___. <___/  |_| `___|\___|\___.|_|_| |_| /__/
                          <___'                                              
    """
    separator_length = max(len(line) for line in ms_art.splitlines())
    separator = "=" * separator_length

    while True:
        print()
        print(separator)
        print(ms_art)
        print(separator)
        print("\n--- Select an option ---")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Update Student")
        print("4. View All Students")
        print("5. Back to Admin Menu")

        choice = input("\nEnter your choice: ").strip()

        if choice == '1':
            try:
                add_student()
            except Exception as e:
                print(f"An error occurred while adding a student: {e}")
        elif choice == '2':
            try:
                remove_student()
            except Exception as e:
                print(f"An error occurred while removing a student: {e}")
        elif choice == '3':
            try:
                update_student()
            except Exception as e:
                print(f"An error occurred while updating a student: {e}")
        elif choice == '4':
            try:
                view_all_students()
            except Exception as e:
                print(f"An error occurred while viewing students: {e}")
        elif choice == '5':
            print("Returning to admin menu...")
            break
        else:
            print("Invalid choice. Please try again.")
