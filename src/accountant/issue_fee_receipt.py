from settings import FEES_FILE

def issue_fee_receipt():
    """Generate a fee receipt for a student"""
    student_id = input("Enter student ID: ").strip()

    with open(FEES_FILE, 'r') as f:
        for line in f:
            data = line.strip().split(',')
            if data[0] == student_id:
                receipt_file = f"receipt_{student_id}.txt"
                with open(receipt_file, 'w') as receipt:
                    receipt.write("University Fee Receipt\n")
                    receipt.write("-" * 30 + "\n")
                    receipt.write(f"Student ID: {data[0]}\n")
                    receipt.write(f"Name: {data[1]}\n")
                    receipt.write(f"Program: {data[2]}\n")
                    receipt.write(f"Fees Paid: {data[3]}\n")
                    receipt.write(f"Outstanding Fees: {data[4]}\n")
                    receipt.write("-" * 30 + "\n")
                print(f"Receipt generated: {receipt_file}")
                return
        print("Student not found.")
