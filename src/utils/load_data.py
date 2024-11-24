def load_data(file_path):
    """Reads a file from the given path and returns a list of its lines."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: {file_path} not found. Please check the directory.")
        return []
    except Exception as e:
        print(f"An error occurred while reading {file_path}: {e}")
        return []
