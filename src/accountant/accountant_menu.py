from accountant.record_tuition_fees import record_tuition_fees
from accountant.view_outstanding_fees import view_outstanding_fees
from accountant.update_payment_records import update_payment_records
from accountant.issue_fee_receipt import issue_fee_receipt
from accountant.view_financial_summary import view_financial_summary

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