from settings import FEES_FILE

def update_payment_records():
    """Update payment records for a student"""
    student_id = input("Enter student ID: ").strip()

    # Read fees data
    with open(FEES_FILE, 'r') as f:
        lines = f.readlines()

    student_found = False

    for line in lines:
        data = line.strip().split(',')
        if data[0] == student_id:
            student_found = True
            print(f"Student Found: {data[1]}\nOutstanding Fees: {data[4]}")
            try:
                amount = float(input("Enter amount to update: "))
                if amount > float(data[4]):
                    print("Error: Payment exceeds outstanding fees.")
                else:
                    data[3] = str(float(data[3]) + amount)
                    data[4] = str(float(data[4]) - amount)
                    print("Payment updated successfully.")

                # Write updated data back to the file
                with open(FEES_FILE, 'w') as f:
                    for line in lines:
                        if line.startswith(student_id):
                            f.write(f"{','.join(data)}\n")
                        else:
                            f.write(line)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
            break

    if not student_found:
        print("Student not found.")