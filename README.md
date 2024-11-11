# University Management System (UMS)

Welcome to the **University Management System (UMS)** repository! This project is a Python application designed to manage university operations for roles such as administrators, lecturers, students, registrars, and accountants. Initially built as a command-line application, the UMS is structured to allow for future GUI enhancements, enabling a more interactive and user-friendly interface.

## 📜 Project Overview

The **UMS** is designed for a university's daily management tasks. Each user role has specific permissions and functionalities, ensuring data access is tailored to each user's needs.

Key roles:
- **Administrator**: Manages courses, students, and lecturers.
- **Lecturer**: Records grades, views enrolled students, and tracks attendance.
- **Student**: Enrolls in courses, view grades, and checks attendance.
- **Registrar**: Registers new students, updates records, and issue transcripts.
- **Accountant**: Tracks tuition payments and generates fee receipts.

## 🛠 Features

- **Role-Specific Menus**: Each roles has unique functionalities accessible through a menu system.
- **File-Based Data Management**: Data is stored in text files, making it easy to update, view and manage information without complex databases.
- **Modular Functions**: Functions are modular, allowing smooth addition of new features and easy adaptation for future GUI implementation.
- **User Input Validation**: Ensures correct data entries to maintain data integrity.

## 📂 Directory Structure

```
UMS_Project/
├── main.py                     # Main menu and role selection
├── data/                       # Folder for data files
│   ├── students.txt            # Stores student details
│   ├── courses.txt             # Stores course datails
│   ├── grades.txt              # Stores student grades
│   ├── attendance.txt          # Stores attendance records
│   └── enrollments.txt         # Stores enrollment information
└── functions/                  # Folder for role-specific functions
    ├── admin_functions.py      # Administrator role functions
    ├── lecturere_functions.py  # Lecturer fole functions
    ├── student_functions.py    # Student role functions
    ├── registrar_functions.py  # Registrar role functions
    └── accountant_functions.py # Accountant role functions
```

## 🚀 Getting Started

### Prerequisites
- Python 3.x

### Installation
1. Clone the repository:
   ``` bash
   git clone https://github.com/your-username/university-management-system.git
   cd university-management system
   ```

2. Run the main program:
   ``` bash
   python main.py
   ```

## 🎮 Usage
1. **Run the program**: Choose a role from the main menu (Administrator, Lecturers, etc.).
2. **Explore functionalities**: Each role presents a unique set of options:
   - For example, the Administrator can add courses or students, while the Registrar can issue transcripts.
3. Manage data files: All data is store in the `data/` folder as a text files.

## 🗂 Data Files

The `data` folder includes the following files:
- `students.txt`: Holds student details(`StudentID, Name, Department`)
- `courses.txt`: Lists available courses (`CoursesCode, CourseName, Credits`)
- `grades.txt`: Stores student grades (`StudentID, CourseCode, Grade`)
- `enrollments.txt`: Tracks course enrollments (`StudentID, CourseCode`)

## 📜 License

This project is licensed under the MIT license. See the [LICENSE](https://github.com/CycPhoenix/University-Management-System?tab=MIT-1-ov-file) file for more details.