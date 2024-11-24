def write_data(file_path, data, mode='w'):
    try:
        with open(file_path, mode, encoding='utf-8') as f:
            f.writelines(f"{line}\n" for line in data)
    except Exception as e:
        print(f"Error writing to file {file_path}: {e}")
