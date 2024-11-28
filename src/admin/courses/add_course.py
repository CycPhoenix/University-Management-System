import os
from utils.append_data import append_data
from utils.load_data import load_data
from settings import FOUNDATION_FILE, DIPLOMA_FILE, UNDERGRADUATE_DIR, POSTGRADUATE_DIR

def add_course():
    """Add a new course to the system."""
    ac_art = r"""
     ___    _    _   ___                             
    | . | _| | _| | |  _> ___  _ _  _ _  ___ ___     
    |   |/ . |/ . | | <__/ . \| | || '_><_-</ ._>
    |_|_|\___|\___| `___/\___/`___||_|  /__/\___.
    """
    # Foundation
    foundation_art = r"""
     ___                  _        _    _               
    | __>___  _ _ ._ _  _| | ___ _| |_ <_> ___ ._ _ 
    | _>/ . \| | || ' |/ . |<_> | | |  | |/ . \| ' |
    |_| \___/`___||_|_|\___|<___| |_|  |_|\___/|_|_|
    """
    diploma_art = r"""
     ___  _       _                      
    | . \<_> ___ | | ___ ._ _ _  ___ 
    | | || || . \| |/ . \| ' ' |<_> |
    |___/|_||  _/|_|\___/|_|_|_|<___|
            |_|                         
    """
    undergraduate_art = r"""
     _ _         _                             _             _           
    | | |._ _  _| | ___  _ _  ___  _ _  ___  _| | _ _  ___ _| |_ ___ 
    | ' || ' |/ . |/ ._>| '_>/ . || '_><_> |/ . || | |<_> | | | / ._>
    `___'|_|_|\___|\___.|_|  \_. ||_|  <___|\___|`___|<___| |_| \___.
                             <___'                                   
    """
    postgraduate_art = r"""
     ___             _                    _             _           
    | . \ ___  ___ _| |_ ___  _ _  ___  _| | _ _  ___ _| |_ ___ 
    |  _// . \<_-<  | | / . || '_><_> |/ . || | |<_> | | | / ._>
    |_|  \___//__/  |_| \_. ||_|  <___|\___|`___|<___| |_| \___.
                        <___'                                   
    """

    # Add indentation
    indent = '   ' # Add 3 spaces of indentation

    separator_length = max(len(line) for line in ac_art.splitlines())
    separator = "=" * separator_length

    # Select the course level
    while True:
        print()
        print(separator)
        print(ac_art)
        print(separator)
        print("\nSelect Course Type:")
        print("1. Foundation")
        print("2. Diploma")
        print("3. Undergraduate")
        print("4. Postgraduate")
        print("5. Cancel")

        choice = input("\nEnter your choice: ").strip()

        if choice == '1':
            ascii_art = foundation_art
            file_path = FOUNDATION_FILE
            selected_course_type = 'Foundation'
            break
        elif choice == '2':
            ascii_art = diploma_art
            file_path = DIPLOMA_FILE
            selected_course_type = 'Diploma'
            break
        elif choice == '3':
            ascii_art = undergraduate_art
            print("\n--- Undergraduate Categories ---")
            try:
                undergraduate_files = [
                    f for f in os.listdir(UNDERGRADUATE_DIR)
                    if os.path.isfile(os.path.join(UNDERGRADUATE_DIR, f)) and f.endswith('.txt')
                ]
                if not undergraduate_files:
                    print("No undergraduate categories found.")
                    
                for idx, file in enumerate(undergraduate_files, start=1):
                    print(f"{idx}. {file.replace('_', ' ').replace('.txt', '').title()}")
                category_choice = input("\nSelect a category: ").strip()
                if category_choice.isdigit() and 1 <= int(category_choice) <= len(undergraduate_files):
                    selected_file = undergraduate_files[int(category_choice) - 1]
                    file_path = os.path.join(UNDERGRADUATE_DIR, selected_file)
                    selected_course_type = f"Undergraduate - {selected_file.replace('_', ' ').replace('.txt', '').title()}"
                    break
                else:
                    print("Invalid choice. Returning to course menu.")
                    return
            except Exception as e:
                print(f"Error accessing undergraduate categories: {e}")
        elif choice == '4':
            ascii_art = postgraduate_art
            print("\n--- Postgraduate Categories ---")
            try:
                postgraduate_files = [
                    f for f in os.listdir(POSTGRADUATE_DIR)
                    if os.path.isfile(os.path.join(POSTGRADUATE_DIR, f)) and f.endswith('.txt')
                ]
                if not postgraduate_files:
                    print("No postgraduate categories found.")
                    
                for idx, file in enumerate(postgraduate_files, start=1):
                    print(f"{idx}. {file.replace('_', ' ').replace('.txt', '').title()}")
                category_choice = input("\nSelect a category: ").strip()
                if category_choice.isdigit() and 1 <= int(category_choice) <= len(postgraduate_files):
                    selected_file = postgraduate_files[int(category_choice) - 1]
                    file_path = os.path.join(POSTGRADUATE_DIR, selected_file)
                    selected_course_type = f"Postgraduate - {selected_file.replace('_', ' ').replace('.txt', '').title()}"
                    break
                else:
                    print("Invalid choice. Returning to course menu.")
                    return
                    
            except Exception as e:
                print(f"Error accessing postgraduate categories: {e}")
        elif choice == '5':
            print("Action canceled. Returning to admin menu...")
            return
        else:
            print("Invalid choice. Please try again.")

    separator_length = max(len(line) for line in ascii_art.splitlines())
    separator = "=" * separator_length

    # Add new course details
    while True:
        print()
        print(separator)
        print(ascii_art)
        print(separator)
        new_course_code = input("Enter the new course code (or type 'Cancel' to exit): ").strip()
        if new_course_code.lower() == 'cancel':
            print("Action canceled. Returning to admin menu.")
            return
        if not new_course_code:
            print("Course code cannot be empty. Please try again.")
            continue

        new_course_name = input("Enter the new course name (or type 'Cancel' to exit): ").strip()
        if new_course_name.lower() == 'cancel':
            print("Action canceled. Returning to admin menu.")
            return
        if not new_course_name:
            print("Course name cannot be empty. Please try again.")
            continue

        new_course_credits = input("Enter the new course credits (or type 'Cancel' to exit): ").strip()
        if new_course_credits.lower() == 'cancel':
            print("Action canceled. Returning to admin menu.")
            return
        if not new_course_credits.isdigit():
            print("Credits must be a numeric value. Please try again.")
            continue

        # Check for duplicate course codes
        existing_courses = load_data(file_path)
        if any(new_course_code.lower() == line.split(',')[0].strip().lower() for line in existing_courses):
            print(f"Course code '{new_course_code}' already exists. Please enter a new course code.")
            continue
        break

    # Append course to the file
    try:
        course_data = f"{new_course_code},{new_course_name},{new_course_credits}"
        append_data(file_path, course_data)
        print(f"Course '{new_course_name}' added successfully to {selected_course_type}!")
    except Exception as e:
        print(f"Error: Failed to add course. {e}")
