from settings import FEES_FILE

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
