import os

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Data directories
DATA_DIR = os.path.join(BASE_DIR, '../data') # Assuming the `data` directory is one level up
ADMIN_DATA_DIR = os.path.join(DATA_DIR, 'admin_data')
STUDENT_DATA_DIR = os.path.join(DATA_DIR, 'student_data')

# File paths
ATTENDANCE_FILE = os.path.join(ADMIN_DATA_DIR, 'attendance.txt')
COURSES_FILE = os.path.join(ADMIN_DATA_DIR, 'courses.txt')
ENROLLMENTS_FILE = os.path.join(ADMIN_DATA_DIR, 'enrollments.txt')
FEES_FILE = os.path.join(ADMIN_DATA_DIR, 'fees.txt')
GRADES_FILE = os.path.join(ADMIN_DATA_DIR, 'grades.txt')
LECTURERS_FILE = os.path.join(ADMIN_DATA_DIR, 'lecturers.txt')
LECTURER_COURSES_FILE = os.path.join(ADMIN_DATA_DIR, 'lecturer_courses.txt')
STUDENTS_FILE = os.path.join(ADMIN_DATA_DIR, 'students.txt')

DEPARTMENTS_FILE = os.path.join(ADMIN_DATA_DIR, 'departments.txt')
FOUNDATION_FILE = os.path.join(ADMIN_DATA_DIR, 'courses', 'foundation.txt')
DIPLOMA_FILE = os.path.join(ADMIN_DATA_DIR, 'courses', 'diploma.txt')
UNDERGRADUATE_DIR = os.path.join(ADMIN_DATA_DIR, 'courses', 'undergraduate')
POSTGRADUATE_DIR = os.path.join(ADMIN_DATA_DIR, 'courses', 'postgraduate')


EXAMPLE_FILE = os.path.join(ADMIN_DATA_DIR, 'example.txt')
