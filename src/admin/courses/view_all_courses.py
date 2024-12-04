import os
from utils.load_data import load_data
from settings import FOUNDATION_FILE, DIPLOMA_FILE, UNDERGRADUATE_DIR, POSTGRADUATE_DIR

def view_all_courses():
    """View all courses available in the system."""
    vac_art = r"""
     _ _  _               ___  _  _   ___                                 
    | | |<_> ___  _ _ _  | . || || | |  _> ___  _ _  _ _  ___ ___  ___
    | ' || |/ ._>| | | | |   || || | | <__/ . \| | || '_><_-</ ._><_-<
    |__/ |_|\___.|__/_/  |_|_||_||_| `___/\___/`___||_|  /__/\___./__/
    """
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

    separator_length = max(len(line) for line in vac_art.splitlines())
    separator = "=" * separator_length

    # Select the course level
    try:
        print()
        print(separator)
        print(vac_art)
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
        elif choice == '2':
            ascii_art = diploma_art
            file_path = DIPLOMA_FILE
            selected_course_type = 'Diploma'
        elif choice == '3':
            ascii_art = undergraduate_art
            try:
                print("\n--- Undergraduate Categories ---")
                undergraduate_files = [
                    f for f in os.listdir(UNDERGRADUATE_DIR)
                    if os.path.isfile(os.path.join(UNDERGRADUATE_DIR, f)) and f.endswith('.txt')
                ]
                if not undergraduate_files:
                    print("No undergraduate categories found.")
                    
                for idx, f in enumerate(undergraduate_files, start=1):
                    print(f"{idx}. {f.replace('_', ' ').replace('.txt', '').title()}")
                category_choice = input("\nSelect a category: ").strip()
                if category_choice.isdigit() and 1 <= int(category_choice) <= len(undergraduate_files):
                    selected_file = undergraduate_files[int(category_choice) - 1]
                    file_path = os.path.join(UNDERGRADUATE_DIR, selected_file)
                    selected_course_type = f"Undergraduate - {selected_file.replace('_', ' ').replace('.txt', '').title()}"
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
                    
                for idx, f in enumerate(postgraduate_files, start=1):
                    print(f"{idx}. {f.replace('_', ' ').replace('.txt', '').title()}")
                category_choice = input("\nSelect a category: ").strip()
                if category_choice.isdigit() and 1 <= int(category_choice) <= len(postgraduate_files):
                    selected_file = postgraduate_files[int(category_choice) - 1]
                    file_path = os.path.join(POSTGRADUATE_DIR, selected_file)
                    selected_course_type = f"Postgraduate - {selected_file.replace('_', ' ').replace('.txt', '').title()}"
                else:
                    print("Invalid choice. Returning to course menu.")
                    
            except Exception as e:
                print(f"Error accessing postgraduate categories: {e}")
                
        elif choice == '5':
            print("Action canceled. Returning to admin menu...")
            return
        else:
            print("Invalid choice. Please try again.")
            

        # Display the courses from the selected file
        try:
            courses = load_data(file_path)
            if not courses:
                print(f"No courses found in {selected_course_type}.")
                return
        except FileNotFoundError:
            print(f"Error: File '{file_path}' does not exist.")
        except Exception as e:
            print(f"An error occurred while viewing courses: {e}")
    except FileNotFoundError:
            print(f"Error: File '{file_path}' does not exist.")

    # Parse view all courses into fields
    course_data = []
    for course in courses:
        course_fields = course.strip().split(',')
        if len(course_fields) == 3:
            course_data.append(course_fields)
        else:
            course_data.append(["[Corrupted Data]"])

    # Calculate column widths dynamically
    col_widths = [25, 110, 10]
    headers = ['Code', 'Name', 'Credits']

    # Add indentation
    indent = '   ' # Add 3 spaces of indentation

    header_row = "".join(f"{header:<{width}}" for header, width in zip(headers, col_widths))
    separator = "=" * len(header_row)

    print()
    print(separator)
    print(ascii_art)
    print(separator)
    print(indent + header_row)
    print(separator)

    for idx, course_fields in enumerate(course_data, start=1):
        if len(course_fields) == 3:
            row = "".join(f"{field:<{width}}" for field, width in zip(course_fields, col_widths))
            print(f"{idx:<3}{row}")
        else:
            print(f"{idx:<3}[Corrupted Data]")

    print(separator)
