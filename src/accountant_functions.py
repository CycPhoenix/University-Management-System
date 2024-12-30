import os
import sys

def get_resource_path(relative_path):
    """Get the absolute path to a resource file, whether running as .py or .exe"""
    base_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.join(os.path.dirname(__file__))))
    return os.path.join(base_path, relative_path)


FEES_FILE = get_resource_path('data/fees.txt')

def accountant_menu():
    """Menu for Accountant functions"""
    while True:
        print("\n--- Accountant Menu ---")
        print("1. Record Tuition Fees")
        print("2. View Outstanding Fees")
        print("3. Update Payment Records")
        print("4. Issue Fee Receipt")
        print("5. View Financial Summary")
        print("6. Back to Main Menu")
        accountant_choice = input("Select an option: ")

        if accountant_choice == '1':
            record_tuition_fees()
        elif accountant_choice == '2':
            view_outstanding_fees()
        elif accountant_choice == '3':
            update_payment_records()
        elif accountant_choice == '4':
            issue_fee_receipt()
        elif accountant_choice == '5':
            view_financial_summary()
        elif accountant_choice == '6':
            break
        else:
            print("Invalid option. Please try again.")

def record_tuition_fees():
    """Record fees paid by a student"""
    student_id = input("Enter student ID: ").strip()
    amount = float(input("Enter amount paid: "))

    
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
                    f.write(line)  
                else:
                    f.write(f"{data[0]},{data[1]},{data[2]},{fees_paid},{fees_outstanding}\n")
                    print("Payment recorded successfully.")
            else:
                f.write(line)

def view_outstanding_fees():
    """View students with outstanding fees"""
    print("\n--- Students with Outstanding Fees ---")
    print(f"{'Student ID':<12} {'Name':<20} {'Outstanding Fees':<15}")
    print("-" * 50)

    with open(FEES_FILE, 'r') as f:
        for line in f:
            data = line.strip().split(',')
            if float(data[4]) > 0:
                print(f"{data[0]:<12} {data[1]:<20} {float(data[4]):<15.2f}")

def update_payment_records():
    """Update payment records for a student"""
    student_id = input("Enter student ID: ").strip()

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

def view_financial_summary():
    """View financial summary of fees collected and outstanding"""
    total_collected = 0
    total_outstanding = 0

    with open(FEES_FILE, 'r') as f:
        for line in f:
            data = line.strip().split(',')
            total_collected += float(data[3])
            total_outstanding += float(data[4])

    print("\n--- Financial Summary ---")
    print(f"Total Fees Collected: {total_collected:.2f}")
    print(f"Total Outstanding Fees: {total_outstanding:.2f}")
