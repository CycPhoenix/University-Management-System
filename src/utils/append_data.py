import os

def append_data(file_path, data):
    """Appends data to a file, creating the file and directories if needed."""
    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Append data
    try:
        with open(file_path, 'a', encoding='utf-8') as f:
            f.write(data + '\n')
    except Exception as e:
        raise Exception(f"Failed to append data to file '{file_path}'. {e}")
