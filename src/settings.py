import os

# Base directory
BASE_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

# File paths
ATTENDANCE_FILE = os.path.join(BASE_DIR, 'attendance.txt')
COURSES_FILE = os.path.join(BASE_DIR, 'courses.txt')
ENROLLMENTS_FILE = os.path.join(BASE_DIR, 'enrollments.txt')
FEES_FILE = os.path.join(BASE_DIR, 'fees.txt')
GRADES_FILE = os.path.join(BASE_DIR, 'grades.txt')
LECTURERS_FILE = os.path.join(BASE_DIR, 'lecturers.txt')
LECTURER_COURSES_FILE = os.path.join(BASE_DIR, 'lecturer_courses.txt')
STUDENTS_FILE = os.path.join(BASE_DIR, 'students.txt')

DEPARTMENTS_FILE = os.path.join(BASE_DIR, 'departments.txt')
FOUNDATION_FILE = os.path.join(BASE_DIR, 'courses', 'foundation.txt')
DIPLOMA_FILE = os.path.join(BASE_DIR, 'courses', 'diploma.txt')
UNDERGRADUATE_DIR = os.path.join(BASE_DIR, 'courses', 'undergraduate')
POSTGRADUATE_DIR = os.path.join(BASE_DIR, 'courses', 'postgraduate')
EXAMPLE_FILE = os.path.join(BASE_DIR, 'example.txt')