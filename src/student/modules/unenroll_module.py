def unenroll_from_module(student_id, module_code):
    updated_lines = []
    with open('students.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith(student_id):
                data = line.strip().split(',')
                enrolled_modules = data[-1].split(';')
                if module_code in enrolled_modules:
                    enrolled_modules.remove(module_code)
                data[-1] = ';'.join(enrolled_modules)
                updated_lines.append(','.join(data) + '\n')
            else:
                updated_lines.append(line)
    with open('students.txt', 'w') as file:
        file.writelines(updated_lines)
    print(f"Unenrolled from module {module_code}.")