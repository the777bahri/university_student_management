# university_student_management
### Project Summary

Welcome to the CLIUniApp (University_UI_Updated.py) and GUIUniApp (University_GUI.py) Project!

CLIUniApp is an interactive system designed for a local university to manage student and admin operations through both Command Line Interface (CLI) and Graphical User Interface (GUI). The system is divided into two main sub-systems: one for students and one for admins, each with specific functionalities.

#### Key Features:
- **Student System**:
  - **Registration**: Students can register with verified email and password. Emails must include the student's first name followed by a dot (.) and the student's last name, an at symbol (@), and the domain `university.com`. Passwords must start with an uppercase letter, contain at least six letters, and include a minimum of three digits.
    
  - **Login**: Registered students can log in. Credentials are checked against the stored data in `students.data`.
  
  - **Enrolment**: Students can enrol in up to 4 subjects. Each subject enrolled generates a random mark between 25 and 100 and calculates the corresponding grade. Students can also view enrolled subjects, remove subjects, and change their passwords.

- **Admin System**:
  - **Data Management**: Admins can view, group, and partition students by grades, remove students, and clear the entire student data file. Admins do not require login to access these functionalities.
  - ##DataFile##: the datafile is an CSV format

#### Technical Details:
- **Languages**: Developed in Python.
- **Data Storage**: Student data is stored in a local file (`students.data`), ensuring all CRUD operations are maintained with this file.
- **Controllers**: Controllers manage data exchange between the model classes (Student, Subject, Admin) and the system menus.
- **Model Classes**:
  - **Student**: Handles student details and subject enrolments. Each student has a unique ID formatted as a six-digit number.
  - **Subject**: Manages subject information and grades. Each subject has a unique ID formatted as a three-digit number. Marks are randomly generated within the range of 25 to 100, and grades are calculated based on these marks.
  - **Admin**: Admins can view, group, and partition students by grades, remove students, and clear the entire student data file. Admins do not require login to access these functionalities.

#### GUI App:
Additionally, a GUI version called GUIUniApp is developed as a standalone application for student use. It includes all the functionalities of the CLI but in an interactive GUI.

#### System Menus:
- **University System Menu**:
  - (A) Admin
  - (S) Student
  - (X) Exit

- **Student System Menu**:
  - (L) Login
  - (R) Register
  - (X) Exit

- **Student Course System Menu**:
  - (C) Change Password
  - (E) Enrol in Subject
  - (R) Remove Subject
  - (S) Show Enrolled Subjects
  - (X) Exit

- **Admin System Menu**:
  - (C) Clear Database File
  - (G) Group Students by Grade
  - (P) Partition Students (Pass/Fail)
  - (R) Remove Student by ID
  - (S) Show All Students
  - (X) Exit

#### Libraries Installed:
I have installed 4 libraries in addition to the default Python libraries:

1. Pandas
   ```
   pip install pandas
   ```

2. Pygame
   ```
   pip install pygame
   ```

3. Pillow
   ```
   pip install pillow
   ```

4. Tkinter
   ```
   pip install tk
   ```

Functionalities and features of each component in the system:
### University GUI (University_GUI.py)
The University GUI application provides a graphical interface for accessing both student and admin functionalities. It features:
- **Main Menu**: Allow users to choose between student and admin systems or exit the application.
- **Student System Access**: Grant access to student functionalities such as enrolment and viewing subjects.
- **Admin System Access**: Grant access to admin functionalities such as viewing and managing student data.
This interface uses Tkinter to create a user-friendly environment for both students and admins to access their respective functionalities.

  ## UNIVERSITY GUI MAIN WINDOW
![uni gui](https://github.com/the777bahri/university_student_management/assets/159003597/96ee48e9-d35a-4cf8-b21a-93edeedb7432)


### University CLI (University_UI_Updated.py)
The University CLI application serves as the main entry point for the system, providing a command-line interface for accessing both student and admin functionalities. It includes:
- **Main Menu**: Allow users to choose between student and admin systems or exit the application.
- **Student System Access**: Enable access to student functionalities such as enrolment and viewing subjects.
- **Admin System Access**: Enable access to admin functionalities such as viewing and managing student data.
This module ensures that users can navigate between student and admin systems efficiently through a straightforward CLI.

### Admin GUI (Admin_GUI.py)
The Admin GUI application provides an interactive graphical interface for admins to manage student data. It allows admins to:
- **View All Students**: Display a list of all registered students, their enrolled subjects, and corresponding grades.
- **Group Students by Grade**: Organize students into groups based on their grades, providing a clear overview of student performance.
- **Partition Students by Pass/Fail**: Separate students into pass and fail categories, simplifying performance evaluation.
- **Remove Student by ID**: Remove a student from the database by specifying their unique ID.
- **Clear Database**: Erase all student data from the system, providing a fresh start for new academic terms.
This interface is built using Tkinter, providing a user-friendly experience for admin operations.

  ### ADMIN GUI WINDOW
![admin gui](https://github.com/the777bahri/university_student_management/assets/159003597/63aac3c6-3eaa-4a2c-95cb-eb219b457e8d)


  ### ADMIN SHOW ALL STUDENTS FUCNTION
![adminshow all students](https://github.com/the777bahri/university_student_management/assets/159003597/2b376eae-04cd-48d6-8705-ea243b8acbd5)


### Admin CLI (Admin_UI_Updated.py)
The Admin CLI application offers a command-line interface for admins to perform various data management tasks. Key functionalities include:
- **View All Students**: Display a comprehensive list of all students and their details.
- **Group Students by Grade**: Categorize students based on their grades to facilitate performance assessment.
- **Partition Students by Pass/Fail**: Divide students into pass and fail groups for quick evaluation.
- **Remove Student by ID**: Enable admins to delete a student's record by entering their unique ID.
- **Clear Database**: Allow admins to clear all records from the student data file.
This module ensures that admins can efficiently manage student data through a straightforward CLI, ensuring data integrity and easy access to crucial functions.

### Student GUI (Student_GUI.py)
The Student GUI application provides students with an interactive graphical interface for managing their academic activities. Features include:
- **Login and Registration**: Students can log in if they are registered or register a new account if they are not.
- **View Enrolled Subjects**: Display the list of subjects a student is enrolled in, including marks and grades.
- **Enrol in Subjects**: Allow students to enrol in up to four subjects, with each enrolment generating a random mark and corresponding grade.
- **Remove Subjects**: Enable students to remove subjects from their enrolment list.
- **Change Password**: Allow students to update their password securely.
This interface uses Tkinter to create a user-friendly environment for students to manage their academic records.

    ### STUDENT GUI WINDOW
![student login gui](https://github.com/the777bahri/university_student_management/assets/159003597/8aeaf917-9078-4c75-8b5c-d3e962c0372e)

  ### STUDENT REGISTRATION FORM
![SRF](https://github.com/the777bahri/university_student_management/assets/159003597/c8b2621e-cdae-4fba-8e01-aeea2a8976bc)

  ### STUDENT MAIN GUI WINDOW
![student gui](https://github.com/the777bahri/university_student_management/assets/159003597/7f4c1366-0ea5-453e-8e1a-06c94e90f041)


  ### STUDENT SHOW CURRENT ENROLLMENT FUNCTION
![student show current enrollment](https://github.com/the777bahri/university_student_management/assets/159003597/6af91632-4380-4bb6-8aff-e315e5333c10)

### Student CLI (Student_UI_Updated.py)
The Student CLI application offers a command-line interface for students to manage their enrolment and academic records. Key functionalities include:
- **Login and Registration**: Students can log in using their registered credentials or register a new account.
- **View Enrolled Subjects**: List all subjects a student is enrolled in, along with marks and grades.
- **Enrol in Subjects**: Enable students to enrol in up to four subjects, with each subject generating a random mark and grade.
- **Remove Subjects**: Allow students to remove subjects from their enrolment list.
- **Change Password**: Provide a secure way for students to update their password.
This module ensures that students can manage their academic activities efficiently through a straightforward CLI.


### Student Login GUI (Student_Login_GUI.py)
The Student Login GUI focuses on providing a secure and user-friendly login interface for students. It features:
- **Login**: Validate student credentials against the stored data to grant access to the system.
- **Registration**: Allow new students to register by providing their details, which are then stored in the system.
This module ensures that only authorized students can access their academic information and perform enrolment activities.

  ### STUDENT LOGIN GUI WINDOW
![student login](https://github.com/the777bahri/university_student_management/assets/159003597/cb2d4462-320c-44da-962b-d23e2b75f65f)


### Subjects CLI (Subjects_UI_Updated.py)
The Subjects CLI application handles the functionalities related to subjects, including:
- **Enrol in Subjects**: Students can enrol in subjects by providing the subject ID.
- **Remove Subjects**: Enable students to remove subjects from their enrolment list by specifying the subject ID.
- **View Enrolled Subjects**: Display a list of all subjects a student is enrolled in, including marks and grades.
This module focuses on managing subject-related operations, ensuring that students can efficiently enrol in and manage their subjects.


