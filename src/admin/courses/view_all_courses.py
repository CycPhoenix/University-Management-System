from utils.display_choices import display_choices
from utils.load_data import load_data
from settings import FOUNDATION_FILE, DIPLOMA_FILE, UNDERGRADUATE_DIR, POSTGRADUATE_DIR

def view_all_courses():
    """View all courses available in the system."""
    print("\n--- View All Courses ---")

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
    
    # Load and display courses
    try:
        courses = load_data(file_path)
        if not courses:
            print(f"No courses found in {selected_course_type}.")
            return
        print(f"\n--- Courses in {selected_course_type} ---")
        for course in courses:
            print(course.strip())
    except FileNotFoundError:
        print(f"Error: File '{file_path}' does not exist.")
    except Exception as e:
        print(f"Error: Failed to load courses. {e}")
