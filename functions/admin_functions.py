import os

DATA_PATH = "data"

def admin_menu():
    """
    Menu for Administrator functions.
    Provides access to various management options for students, lecturers, and courses, as well as options to generate reports and view all data.
    """
    while True:
        print("\n--- Administrator Menu ---")
        print("1. Add New Course")
        print("2. Add/Remove Student")
        print("3. Manage Lecturers")
        print("4. Generate Reports")
        print("5. View All Data")
        print("6. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            manage_course()
        elif choice == '2':
            manage_students()
        elif choice == '3':
            manage_lecturers()
        elif choice == '4':
            generate_reports()
        elif choice == '5':
            view_all_data()
        elif choice == '6':
            break
        else:
            print("Invalid option. Please try again.")

def manage_course():
    """
    Add, remoev, or update course information.
    """
    print("\n--- Manage Courses ---")
    print("1. Add Course")
    print("2. Remove Course")
    print("3. Update Course Information")
    choice = input("Select an option: ").strip()

    courses_file = os.path.join(DATA_PATH, "courses.txt")

    if choice == "1":
        # Add a new course
        course_code = input("Enter Course Code: ").strip()
        course_name = input("Enter Course Name: ").strip()
        credits = input("Enter Credits: ").strip()

        # Add new course to courses.txt
        with open(courses_file, "a") as f:
            f.write(f"{course_code}, {course_name}, {credits}\n")

        print("Courses added successfully.")

    elif choice == "2":
        # Remove an existing course
        course_code = input("Enter Course Code to remove: ").strip()

        # Remove course from courses.txt
        with open(courses_file, "r") as f:
            lines = f.readlines()
        with open(courses_file, "w") as f:
            for line in lines:
                if not line.startswith(course_code):
                    f.write(line)

        print("Course removed successfully.")

    elif choice == "3":
        # Update course information
        course_code = input("Enter Course Code to update: ").strip()
        new_name = input("Enter new Course Name: ").strip()
        new_credits = input("Enter new Credits: ").strip()

        # Update course details in courses.txt
        with open(courses_file, "r") as f:
            lines = f.readlines()
        with open(courses_file, "w") as f:
            for line in lines:
                if line.startswith(course_code):
                    f.write(f"{course_code}, {new_name}, {new_credits}")
                else:
                    f.write(line)
        
        print("Courses infromation updated successfully")
        
    else:
        print("invalid choice.")

def manage_students():
    """
    Add, remove, or update student information.
    """
    print("\n--- Manage Students ---")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Update Student Information")
    choice = input("Select an option: ").strip()

    students_file = os.path.join(DATA_PATH, "students.txt")

    if choice == "1":
        # Add a new student
        student_id = input("Enter student ID: ").strip()
        name = input("Enter student name: ").strip()
        department = input("Enter student department: ").strip()

        # Add new student to studnets.txt
        with open(students_file, "a") as f:
            f.write(f"{student_id}, {name}, {department}")
        print("Student added successfully.")
    
    elif choice == "2":
        # Remove an existing student
        student_id = input("Enter student ID to remove: ").strip()

        # Remove student from studnets.txt
        with open(students_file, "r") as f:
            lines = f.readlines()
        with open(students_file, "w") as f:
            for line in lines:
                if not line.startswith(student_id):
                    f.write(line)

        print("Student removed successfully.")

    elif choice == "3":
        # Update student information
        student_id = input("Enter Student ID to update: ").strip()
        new_name = input("Enter new Name: ").strip()
        new_department = input("Enter new Department: ").strip()
        
        # Update studnet details in students.txt
        with open(students_file, "r") as f:
            lines = f.readlines()
        with open(students_file, "w") as f:
            for line in lines:
                if line.startswith(student_id):
                    f.write(f"{student_id}, {new_name}, {new_department}")
                else:
                    f.write(line)
        print("Student information updated successfully.")

    else:
        print("Invalid choice.")

def manage_lecturers():
    """Add, remove or update lecturer information"""
    print("1. Add Lecturer")
    print("2. Remove Lecturer")
    print("3. Update Lecturer Information")
    print("4. Assign Course to Lecturer")
    choice = input("Select an option: ")

    if choice == '1':
        # Add a new lecturer
        lecturer_id = input("Enter lecturer ID: ").strip()
        name = input("Enter lecturer name: ").strip()
        department = input("Enter lecturer department: ").strip()
        with open(os.path.join(DATA_PATH, "lectureres.txt"), "a") as f:
            f.write(f"{lecturer_id}, {name}, {department}")
        print('Lecturer added successfully.')

    elif choice == '2':
        # Remove an existing lecturer
        lecturer_id = input("Enter lecturer ID to remove: ").strip()
        lecturers_file = os.path.join(DATA_PATH, "lectureres.txt")
        with open(lecturers_file, 'r') as f:
            lines = f.readlines()
        with open(lecturers_file, "w") as f:
            for line in lines:
                if not line.startswith(lecturer_id):
                    f.write(line)
        
        # Also remove any course assignments
        lecturers_courses_file = os.path.join(DATA_PATH, "lecturer_courses.txt")
        if os.path.exists(lecturers_courses_file):
            with open(lecturers_courses_file, "r") as f:
                lines = f.readlines()
            with open(lecturers_courses_file, "w") as f:
                for line in lines:
                    if not line.startswith(lecturer_id):
                        f.write(line)
        print("Lecturer removed successfully.")
    elif choice == '3':
        # Update lecturer information
        lecturer_id = input("Enter lecturer ID: ").strip()
        update_name = input("Enter new name: ").strip()
        update_department = input("Enter new department: ").strip()
        lecturers_file = os.path.join(DATA_PATH, "lecturers.txt")
        with open(lecturers_file, 'r') as f:
            lines = f.readlines()
        with open(lecturers_file, 'w') as f:
            for line in lines:
                if line.startswith(lecturer_id):
                    f.write(f"{lecturer_id}, {update_name}, {update_department}\n")
                else:
                    f.write(line)
        print("Lecturer information updated successfully.")

    elif choice == "4":
        # Assign course to lecturer
        lecturer_id = input("Enter lecturer ID: ").strip()
        course_code = input("Enter course code to assign: ").strip()

        # Verify lecturer exists
        if not lecturer_exists(lecturer_id):
            print("Lecturer ID not found. Please add the lecturer first.")
            return
        
        # Verify course exitsts
        courses_file = os.path.join(DATA_PATH, "courses.txt")
        course_exists = False
        with open(courses_file, "r") as f:
            for line in f:
                existing_course_code = line.strip().split(",")[0]
                if existing_course_code == course_code:
                    course_exists = True
                    break
        if not course_exists:
            print("Course code not found. Please add the course first.")
        
        # Assign course
        with open(os.path.join(DATA_PATH, "lecturer.courses.txt"), "a") as f:
            f.write(f"{lecturer_id}, {course_code}\n")
            print(f"Course {course_code} assigned to lecturer {lecturer_id} successfully")

    else:
        print("Invalid choice.")

def lecturer_exists(lecturer_id):
    """
    Checks if a lecturer exists in lecturers.txt.
    
    Parameters:
    - lecturer_id (str): ID of the lecturer.
    
    Returns:
    bool: True if lecturer exists, False otherwise.
    """
    lecturers_file = os.path.join(DATA_PATH, "lecturers.txt")
    if not os.path.exists(lecturers_file):
        return False
    
    with open(lecturers_file, "r") as f:
        for line in f:
            existing_id = line.strip().split(",")[0]
            if existing_id == lecturer_id:
                return True
    return False
    

def generate_reports():
    """
    Generate various reports (e.g., list of students, lecturers, courses).
    """
    print("\n--- Generate Reports ---")
    print("1. List of Students")
    print("2. List of Lecturers")
    print("3. List of Courses")
    choice = input("Select a report to generate: ").strip()

    if choice == "1":
        print("\n--- List of Students ---")
        with open(os.path.join(DATA_PATH, "students.txt"), "r") as f:
            for line in f:
                print(line.strip())

    elif choice == "2":
        print("\n--- List of Lecturers ---")
        with open(os.path.join(DATA_PATH, "lecturers.txt"), "r") as f:
            for line in f:
                print(line.strip())
    
    elif choice == "3":
        print("\n--- List of Courses ---")
        with open(os.path.join(DATA_PATH, "courses.txt"), "r") as f:
            for line in f:
                print(line.strip())
    
    else:
        print("Invalid choice")

def view_all_data():
    """
    View all data for students, lecturers, courses, and lecturer course assignments.
    """
    print("\n--- View All Data ---")
    print("\n--- Students ---")
    with open(os.path.join(DATA_PATH, "students.txt"), "r") as f:
        for line in f:
            print(line.strip())

    print("\n--- Lecturers ---")
    with open(os.path.join(DATA_PATH, "lecturers.txt"), "r") as f:
        for line in f:
            print(line.strip())

    print("\n--- Courses ---")
    with open(os.path.join(DATA_PATH, "courses.txt"), "r") as f:
        for line in f:
            print(line.strip())

    print("\n--- Lecturer Course Assigns ---")
    lecturer_courses_file = os.path.join(DATA_PATH, "lecturer_courses.txt")
    if os.path.exists(lecturer_courses_file):
        with open(lecturer_courses_file, "r") as f:
            for line in f:
                print(line.strip())
    else:
        print("No lecturer-course assignments found.")
