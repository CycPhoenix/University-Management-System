from admin.lecturers.add_lecturer import add_lecturer
from admin.lecturers.remove_lecturer import remove_lecturer
from admin.lecturers.update_lecturer import update_lecturer
from admin.lecturers.view_all_lecturers import view_all_lecturers

def manage_lecturers():
    """Menu to manage lecturers."""
    ml_art = r"""
     __ __                            _               _                              
    |  \  \ ___ ._ _  ___  ___  ___  | |   ___  ___ _| |_ _ _  _ _  ___  _ _  ___
    |     |<_> || ' |<_> |/ . |/ ._> | |_ / ._>/ | ' | | | | || '_>/ ._>| '_><_-<
    |_|_|_|<___||_|_|<___|\_. |\___. |___|\___.\_|_. |_| `___||_|  \___.|_|  /__/
                      <___'                                                  
    """
    separator_length = max(len(line) for line in ml_art.splitlines())
    separator = "=" * separator_length

    while True:
        print()
        print(separator)
        print(ml_art)
        print(separator)
        print("\nSelect an option:")
        print("1. Add Lecturer")
        print("2. Remove Lecturer")
        print("3. Update Lecturer")
        print("4. View All Lecturers")
        print("5. Back to Admin Menu")

        choice = input("\nEnter your choice: ").strip()

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
