from utils.load_data import load_data
from utils.write_data import write_data
from settings import FOUNDATION_FILE, DIPLOMA_FILE, UNDERGRADUATE_DIR, POSTGRADUATE_DIR
import os

def update_course():
    """Update a course in the system."""
    uc_art = r"""
     _ _         _        _         ___                             
    | | | ___  _| | ___ _| |_ ___  |  _> ___  _ _  _ _  ___ ___ 
    | ' || . \/ . |<_> | | | / ._> | <__/ . \| | || '_><_-</ ._>
    `___'|  _/\___|<___| |_| \___. `___/\___/`___||_|  /__/\___.
         |_|                                                    
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

    separator_length = max(len(line) for line in uc_art.splitlines())
    separator = "=" * separator_length

    print()
    print(separator)
    print(uc_art)
    print(separator)

    # Select the course level
    while True:
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
            selected_course_type = "Foundation"
            break
        elif choice == '2':
            ascii_art = diploma_art
            file_path = DIPLOMA_FILE
            selected_course_type = "Diploma"
            break
        elif choice == '3':
            ascii_art = undergraduate_art
            print("\n--- Undergraduate Categories ---")
            try:
                undergraduate_files = [
                    f for f in os.listdir(UNDERGRADUATE_DIR)
                    if f.endswith('.txt')
                ]
                if not undergraduate_files:
                    print("No undergraduate categories found.")
                    return
                for idx, file in enumerate(undergraduate_files, start=1):
                    print(f"{idx}. {file.replace('_', ' ').replace('.txt', '').title()}")
                category_choice = input("\nSelect a category: ").strip()
                if category_choice.isdigit() and 1 <= int(category_choice) <= len(undergraduate_files):
                    selected_file = undergraduate_files[int(category_choice) - 1]
                    file_path = os.path.join(UNDERGRADUATE_DIR, selected_file)
                    selected_course_type = f"Undergraduate - {selected_file.replace('_', ' ').replace('.txt', '').title()}"
                    break
                else:
                    print("Invalid choice. Returning to menu.")
                    return
            except Exception as e:
                print(f"Error accessing undergraduate categories: {e}")
        elif choice == '4':
            ascii_art = postgraduate_art
            print("\n--- Postgraduate Categories ---")
            try:
                postgraduate_files = [
                    f for f in os.listdir(POSTGRADUATE_DIR)
                    if f.endswith('.txt')
                ]
                if not postgraduate_files:
                    print("No postgraduate categories found.")
                    return
                for idx, file in enumerate(postgraduate_files, start=1):
                    print(f"{idx}. {file.replace('_', ' ').replace('.txt', '').title()}")
                category_choice = input("\nSelect a category: ").strip()
                if category_choice.isdigit() and 1 <= int(category_choice) <= len(postgraduate_files):
                    selected_file = postgraduate_files[int(category_choice) - 1]
                    file_path = os.path.join(POSTGRADUATE_DIR, selected_file)
                    selected_course_type = f"Postgraduate - {selected_file.replace('_', ' ').replace('.txt', '').title()}"
                    break
                else:
                    print("Invalid choice. Returning to menu.")
                    return
            except Exception as e:
                print(f"Error accessing postgraduate categories: {e}")
        elif choice == '5':
            print("Action canceled. Returning to admin menu...")
            return
        else:
            print("Invalid choice. Please try again.")

    # Load and display courses
    try:
        courses = load_data(file_path)
        if not courses:
            print(f"No courses found in {selected_course_type}.")
            return
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return

    print("\n--- Courses ---")
    for idx, course in enumerate(courses, start=1):
        print(f"{idx}. {course.strip()}")
    print(f"{len(courses) + 1}. Cancel")

    # Select a course to update
    choice = input("\nSelect a course to update: ").strip()
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(courses):
        print("Invalid choice. Returning to admin menu...")
        return

    selected_course = courses[int(choice) - 1]
    course_fields = selected_course.split(',')

    if len(course_fields) != 3:
        print("Error: Selected course data is corrupted.")
        return

    # Update course fields
    new_code = input(f"Enter new Course Code (press Enter to keep '{course_fields[0]}'): ").strip().upper() or course_fields[0]
    new_name = input(f"Enter new Course Name (press Enter to keep '{course_fields[1]}'): ").strip() or course_fields[1]
    new_credits = input(f"Enter new Course Credits (press Enter to keep '{course_fields[2]}'): ").strip() or course_fields[2]

    updated_course = f"{new_code},{new_name},{new_credits}"

    # Update courses and save
    try:
        updated_courses = [updated_course if course == selected_course else course for course in courses]
        write_data(file_path, updated_courses)
        print(f"Course updated successfully: {updated_course}")
    except Exception as e:
        print(f"An error occurred while updating the course: {e}")
