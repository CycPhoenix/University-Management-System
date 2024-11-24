from utils.display_choices import display_choices
from settings import FOUNDATION_FILE, DIPLOMA_FILE, UNDERGRADUATE_DIR, POSTGRADUATE_DIR


def update_course():
    """Update details of an existing course."""
    print(f"\n--- Update Course ---")

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

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            courses = f.readlines()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' does not exist.")
        return
    except Exception as e:
        print(f"Error: Failed to load courses. {e}")
        return
    
    courses = [course.strip() for course in courses]
    if not courses:
        print(f"No courses found in {selected_course_type}.")

    course_options = {str(i + 1): course for i, course in enumerate(courses)}
    course_options[str(len(courses) + 1)] = 'Cancel'
    course_choice = display_choices(course_options)

    if course_choice == str(len(courses) + 1):
        print("Action canceled. Returning to admin menu.")
        return
    
    selected_course = course_options[course_choice]
    print(f"Selected course: {selected_course}")

    # Split the selected course into components (code, name, credits)
    course_details = selected_course.split(',')
    current_code = course_details[0].strip()
    current_name = course_details[1].strip()
    current_credits = course_details[2].strip()

    # Get updated details
    new_code = input(f"Enter new course code (press Enter to keep '{current_code}'): ").strip() or current_code
    new_name = input(f"Enter new course name (press Enter to keep '{current_name}'): ").strip() or current_name
    new_credits = input(f"Enter new course credits (press Enter to keep '{current_credits}'): ").strip() or current_credits

    # Combine updated details into a single line
    updated_course = f"{new_code},{new_name},{new_credits}"

    # Write updated courses back to the file
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            for course in courses:
                if course == selected_course:
                    f.write(f"{updated_course}\n")
                else:
                    f.write(f"{course.strip()}\n")
        print(f"Course '{selected_course}' updated successfully to '{updated_course}'.")
    except Exception as e:
        print(f"Error: Failed to update the course. {e}")
