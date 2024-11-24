from utils.display_choices import display_choices
from settings import FOUNDATION_FILE, DIPLOMA_FILE, UNDERGRADUATE_DIR, POSTGRADUATE_DIR


def add_course():
    """Add a new course to the system."""
    print(f"\n--- Add New Course ---")

    # Select the course level
    while True:
        courses = {
            '1': 'Foundation',
            '2': 'Diploma',
            '3': 'Undergraduate',
            '4': 'Postgraduate',
            '5': 'Cancel'
        }
        course_choice = display_choices(courses)

        if course_choice == '1':
            file_path = FOUNDATION_FILE
            selected_course_type = 'Foundation'
            break
        elif course_choice == '2':
            file_path = DIPLOMA_FILE
            selected_course_type = 'Diploma'
            break
        elif course_choice == '3':
            categories = {
                '1': 'Accounting, Banking, Finance & Actuarial',
                '2': 'Business Management, Marketing & Tourism',
                '3': 'Computing & Technology',
                '4': 'Creative Design & Multimedia',
                '5': 'Design, Advertising, Animation & VFX',
                '6': 'Engineering',
                '7': 'Media, International Relations & Psychology',
                '8': 'Cancel'
            }
            category_choice = display_choices(categories)

            if category_choice == '8':
                print("Action canceled. Returning to admin menu.")
                return
            elif category_choice in categories:
                category = categories[category_choice]
                file_path = f"{UNDERGRADUATE_DIR}{category.lower().replace(', ', '_').replace(' ', '_')}.txt"
                selected_course_type = f"Undergraduate - {category}"
                break
        elif course_choice == '4':
            categories = {
                '1': 'Masters',
                '2': 'PhD',
                '3': 'Cancel'
            }
            category_choice = display_choices(categories)

            if category_choice == '3':
                print("Action canceled. Returning to admin menu.")
                return
            elif category_choice in categories:
                category = categories[category_choice]
                file_path = f"{POSTGRADUATE_DIR}{category.lower()}.txt"
                selected_course_type = f"Postgraduate - {category}"
                break
        elif course_choice == '5':
            print("Action canceled. Returning to admin menu.")
            return
        else:
            print("Invalid choice. Please try again.")
    
    # Add a new course
    new_course_code = input("Enter the new course code (or type 'Cancel' to exit): ").strip()
    if new_course_code.lower() == 'cancel':
        print("Action canceled. Returning to admin menu.")
        return
    
    new_course_name = input("Enter the new course name (or type 'Cancel' to exit): ").strip()
    if new_course_name.lower() == 'cancel':
        print("Action canceled. Returning to admin menu.")
        return
    
    new_course_credits = input("Enter the new course credits (or type 'Cancel' to exit): ").strip()
    if new_course_credits.lower() == 'cancel':
        print("Action canceled. Returning to admin menu.")
        return
    
    try:
        with open(file_path, 'a', encoding='utf-8') as f:
            f.write(f"{new_course_code},{new_course_name},{new_course_credits}\n")
        print(f"Course '{new_course_name}' added successfully to {selected_course_type}!")
    except Exception as e:
        print(f"Error: Failed to add course. {e}")
