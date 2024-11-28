from utils.load_data import load_data
from settings import STUDENTS_FILE, LECTURERS_FILE, DEPARTMENTS_FILE

def students_and_lecturers_by_department():
    """List students and lecturers categorised by department."""
    # print("\n--- Students and Lecturers by Department ---")
    
    # Art for Students and Lecturers by Department
    sld_art = r"""
     ___  _    _     _          ___                       _                      _      
    / __>< >  | |   | |_  _ _  | . \ ___  ___  ___  _ _ _| |_ ._ _ _  ___ ._ _ _| |_
    \__ \/.\/ | |_  | . \| | | | | |/ ._>| . \<_> || '_> | |  | ' ' |/ ._>| ' | | | 
    <___/\_/\ |___| |___/`_. | |___/\___.|  _/<___||_|   |_|  |_|_|_|\___.|_|_| |_| 
                         <___'           |_|
    """

    separator_length = max(len(line) for line in sld_art.splitlines())
    separator = "=" * separator_length

    try:
        departments = load_data(DEPARTMENTS_FILE)
        students = load_data(STUDENTS_FILE)
        lecturers = load_data(LECTURERS_FILE)

        department_students = {dep.strip(): [] for dep in departments}
        department_lecturers = {dep.strip(): [] for dep in departments}

        for student in students:
            fields = student.split(',')
            if len(fields) >= 3:
                department_students[fields[2].strip()].append(fields[1].strip())

        for lecturer in lecturers:
            fields = lecturer.split(',')
            if len(fields) >= 3:
                department_lecturers[fields[2].strip()].append(fields[1].strip())

        first = True # Flag to check for the first iteration
        
        print(separator)
        print(sld_art)
        print(separator)

        for department in departments:
            if not first:
                print() # Add a newline before every department except the first
            first = False # Set the flag to False after the first iteration

            print(f"Department: {department.strip()}")
            print("  Students:")
            students_list = department_students.get(department.strip(), [])
            if students_list:
                for student in students_list:
                    print(f"    - {student}")

            print("  Lecturers:")
            lecturers_list = department_lecturers.get(department.strip(), [])
            if lecturers_list:
                for lecturer in lecturers_list:
                    print(f"    - {lecturer}")
        print(separator)
    except Exception as e:
        print(f"Error: Failed to generate report by department. {e}")
