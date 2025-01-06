from settings import FEES_FILE

def record_tuition_fees():
    """Record fees paid by a student"""
    student_id = input("Enter student ID: ").strip()
    amount = float(input("Enter amount paid: "))

    # Read and update fees data
    with open(FEES_FILE, 'r') as f:
        lines = f.readlines()

    with open(FEES_FILE, 'w') as f:
        for line in lines:
            data = line.strip().split(',')
            if data[0] == student_id:
                fees_paid = float(data[3]) + amount
                fees_outstanding = float(data[4]) - amount
                if fees_outstanding < 0:
                    print("Error: Payment exceeds outstanding fees.")
                    f.write(line)  # Keep original record
                else:
                    f.write(f"{data[0]},{data[1]},{data[2]},{fees_paid},{fees_outstanding}\n")
                    print("Payment recorded successfully.")
            else:
                f.write(line)
