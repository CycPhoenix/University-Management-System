import os
from utils.load_data import load_data
from utils.write_data import write_data
from settings import FOUNDATION_FILE, DIPLOMA_FILE, UNDERGRADUATE_DIR, POSTGRADUATE_DIR

def remove_course():
    """Remove a course from the system."""
    rc_art = r"""
     ___                              ___                         
    | . \ ___ ._ _ _  ___  _ _  ___  |  _> ___  _ _  _ _  ___ ___ 
    |   // ._>| ' ' |/ . \| | |/ ._> | <__/ . \| | || '_><_-</ ._>
    |_\_\\___.|_|_|_|\___/|__/ \___. `___/\___/`___||_|  /__/\___.
                                                              
    """
    separator_length = max(len(line) for line in rc_art.splitlines())
    separator = "=" * separator_length

    # Select the course level
    while True:
        print()
        print(separator)
        print(rc_art)
        print(separator)
        print("\nSelect Course Type:")
        print("1. Foundation")
        print("2. Diploma")
        print("3. Undergraduate")
        print("4. Postgraduate")
        print("5. Cancel")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            file_path = FOUNDATION_FILE
            selected_course_type = "Foundation"
            break
        elif choice == '2':
            file_path = DIPLOMA_FILE
            selected_course_type = "Diploma"
            break
        elif choice == '3':
            print("\n--- Undergraduate Categories ---")
            try:
                undergraduate_files = [
                    f for f in os.listdir(UNDERGRADUATE_DIR)
                    if os.path.isfile(os.path.join(UNDERGRADUATE_DIR, f)) and f.endswith('.txt')
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
                    print("Invalid choice. Returning to course menu.")
                    return
            except Exception as e:
                print(f"Error accessing undergraduate categories: {e}")
        elif choice == '4':
            print("\n--- Postgraduate Categories ---")
            try:
                postgraduate_files = [
                    f for f in os.listdir(POSTGRADUATE_DIR)
                    if os.path.isfile(os.path.join(POSTGRADUATE_DIR, f)) and f.endswith('.txt')
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
                    print("Invalid choice. Returning to course menu.")
                    return
            except Exception as e:
                print(f"Error accessing postgraduate categories: {e}")
        elif choice == '5':
            print("Action canceled. Returning to admin menu...")
            return
        else:
            print("Invalid choice. Please try again.")

    # Load courses
    try:
        courses = load_data(file_path)
        if not courses:
            print(f"No courses found in the selected file: {file_path}")
            return
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return

    # Display courses to remove
    print("\n--- Existing Courses ---")
    for idx, course in enumerate(courses, 1):
        print(f"{idx}. {course.strip()}")
    print(f"{len(courses) + 1}. Cancel")
    
    while True:
        choice = input("\nSelect a course to remove: ").strip()
        if choice.isdigit or (1 <= int(choice) < (len(courses) + 1)):
            break
        elif choice == str(len(courses) + 1):
            print("Action canceled. Returning to admin menu...")
            return
        else:
            print("Invalid choice. Please enter a valid number.")
            return

    selected_course = courses[int(choice) - 1]
    course_fields = selected_course.split(",")
    course_code = course_fields[0]
    course_name = course_fields[1]
    course_credits = course_fields[2]

    info = f"Code: {course_code} | Name: {course_name} | Credits: {course_credits}"

    print(f"Selected course - {info}")

    # Confirmation removal
    confirmation = input(f"Are you sure you want to remove '{course_name}'? (yes/no): ").strip().lower()
    if confirmation != "yes":
        print("Action canceled. Returning to Manage Courses.")
        return

    # Update the file to remove the selected course
    try:
        updated_courses = [course.strip() for course in courses if course.strip() != selected_course.strip()]
        write_data(file_path, updated_courses)
        print(f"Course '{course_name}' removed successfully.")
    except Exception as e:
        print(f"An error occurred while removing the course: {e}")
