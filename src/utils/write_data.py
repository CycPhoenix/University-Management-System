import os

def write_data(file_path, data_list):
    """Overwrites a file with a list of data."""
    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Write data
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            for line in data_list:
                # Strip any additional newlines and format correctly
                f.write(line.strip() + '\n')
    except Exception as e:
        raise Exception(f"Failed to write data to file '{file_path}'. {e}")
