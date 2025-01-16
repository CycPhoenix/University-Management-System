from settings import FEES_FILE

def record_tuition_fees():
    """Record fees paid by a student (new or existing)"""
    # Ask if the student is new or existing
    student_type = input("Are you a new student? (yes/no): ").strip().lower()

    if student_type == "yes":
        # New student: Collect details
        student_id = input("Enter student ID: ").strip()
        name = input("Enter your name: ").strip()
        course_level = input("Enter your course level (e.g., Masters, Degree, PhD, Diploma, Foundation): ").strip()

        # Define fees based on course level
        course_fees = {
            "Masters": 3000,
            "Degree": 2500,
            "PhD": 4000,
            "Diploma": 2000,
            "Foundation": 1500
        }

        if course_level not in course_fees:
            print("Invalid course level. Please try again.")
            return

        total_fees = course_fees[course_level]
        print(f"Total fees for {course_level}: ${total_fees}")

        amount_paid = float(input("Enter amount paid: "))
        fees_outstanding = total_fees - amount_paid

        # Append new student record to the file on a new line
        with open(FEES_FILE, 'a') as f:
            f.write(f"\n{student_id},{name},{course_level},{amount_paid},{fees_outstanding}")

        print("Thank you for your payment!")
        print(f"Amount paid: ${amount_paid}")
        print(f"Outstanding amount: ${fees_outstanding}")

    else:
        # Existing student: Collect ID and update record
        student_id = input("Enter student ID: ").strip()

        # Read and update fees data
        with open(FEES_FILE, 'r') as f:
            lines = f.readlines()

        found = False
        updated_lines = []

        for line in lines:
            data = line.strip().split(',')
            if data[0] == student_id:
                found = True
                name = data[1]
                course_level = data[2]
                fees_paid = float(data[3])
                fees_outstanding = float(data[4])

                if fees_outstanding == 0:
                    print(f"Hello, {name}! You have fully paid your fees. Thank you!")
                    updated_lines.append(line)  # Keep the record unchanged
                else:
                    print(f"Hello, {name}! Your outstanding amount is: ${fees_outstanding}")
                    amount = float(input("Enter amount paid: "))
                    fees_paid += amount
                    fees_outstanding -= amount

                    if fees_outstanding < 0:
                        print("Error: Payment exceeds outstanding fees.")
                        updated_lines.append(line)  # Keep original record
                    else:
                        updated_lines.append(f"{data[0]},{data[1]},{data[2]},{fees_paid},{fees_outstanding}\n")
                        print("Payment recorded successfully.")
                        print(f"Amount paid: ${amount}")
                        print(f"Outstanding amount: ${fees_outstanding}")
            else:
                updated_lines.append(line)

        if not found:
            print("Student ID not found. Please check and try again.")
            return

        # Write updated data back to the file
        with open(FEES_FILE, 'w') as f:
            f.writelines(updated_lines)
