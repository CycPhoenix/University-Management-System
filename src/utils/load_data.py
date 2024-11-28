def load_data(file_path):
    """Loads data from a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.readlines()
    except FileNotFoundError:
        return []
    except Exception as e:
        raise Exception(f"Failed to load data from file '{file_path}'. {e}")
