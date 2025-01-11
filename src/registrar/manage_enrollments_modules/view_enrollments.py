from utils.load_data import load_data
from settings import ENROLLMENTS_FILE

def view_enrollments(student_id, enrollments):
    """View current enrollments for a student."""
    # Load enrollments
    try:
        enrollments = load_data(ENROLLMENTS_FILE)
    except FileNotFoundError:
        print(f"Error: File '{ENROLLMENTS_FILE}' not found.")
        return
    
    # Filter the student's enrollments
    student_enrollments = [line.strip() for line in enrollments if line.startswith(student_id)]
    if not student_enrollments:
        print(f"No enrollments found for student {student_id}.")
        return
    
    # Display the student's current enrollments
    print("\n--- Current Enrollments ---")
    for enrollment in student_enrollments:
        module_code = enrollment.split(',')[1]
        print(f"Module Code: {module_code}")
