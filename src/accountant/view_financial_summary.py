from settings import FEES_FILE

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
