import pandas as pd
import os
import re
import random
from Subjects_UI_Updated import Subject

class Student:
    def __init__(self, filename='dataset\students_data.csv'):
        self.filename = filename
        self.df = pd.read_csv(filename)
        self.headers = ['Student ID', 'First Name', 'Last Name', 'Email', 'Password',
                        'Course 1', 'Course 1 Mark', 'Course 1 Grade', 'Course 2',
                        'Course 2 Mark', 'Course 2 Grade', 'Course 3', 'Course 3 Mark',
                        'Course 3 Grade', 'Course 4', 'Course 4 Mark', 'Course 4 Grade']
        
        self.subject = Subject()
        self.student_id = ''

    def registration_gui(self, first_name, last_name, email, password):
        self.df = pd.read_csv(self.filename)
        if self.student_exists(first_name, last_name):
            return False, "A student with this name is already registered."

        expected_email = f"{first_name.lower()}.{last_name.lower()}@university.com"
        if email.lower() != expected_email:
            return False, "The email address does not match the required format: firstname.lastname@university.com."

        if not self.is_valid_password(password):
            return False, "Invalid password. It must start with an uppercase letter, followed by at least four more letters, and end with three or more digits."

        student_id = self.sixdig_id()
        data = [student_id, first_name, last_name, email, password] + [''] * 12
        self.write_data(data)
        self.df = pd.read_csv(self.filename)
        return True, f"Student {first_name} {last_name} created with ID {student_id}."
    
    
    def registration(self):
        print("\n\033[34m   Students Registration Form\033[0m")
        self.df = pd.read_csv(self.filename)

        first_name = input("\n  Please enter your first name: ")
        last_name = input("\n   Please enter your last name: ")

        if self.student_exists(first_name, last_name):
            print(f"\n\033[31m  A student named {first_name} {last_name} is already registered.\033[0m")
            return
        
        while True:
            email = input("\n   Please enter your email address in the form of firstname.lastname@university.com only\n").lower()
            expected_email = f"{first_name.lower()}.{last_name.lower()}@university.com"
            if email.lower() == expected_email:
                print("\n\033[32m   The email address is correctly formatted 👍\033[0m")
                break
            else:
                print("\n\033[31m   The email address does not match the required format 😭\n required fromat is firstname.lastname@university.com.\033[0m")
        while True:
            password = input("\n    Enter your password: ")
            if self.is_valid_password(password):
                print("\n\033[32m   Password is valid 👍\033[0m")
                print("\n")
                break
            else:
                print("\n\033[31m   Password is invalid😒. It must start with an uppercase letter\nand followed by at least four more letters, and end with three or more digits.\033[0m")

        student_id = self.sixdig_id()
        data = [student_id, first_name, last_name, email, password, '','','','','','','','','','','','']
        self.write_data(data)
        self.df = pd.read_csv(self.filename)

        print(f"\n\033[33m   Student {first_name} {last_name} Created with ID {student_id} ✌\033[0m")    

    def student_exists(self, first_name, last_name):
        exists = self.df[(self.df['First Name'].str.lower() == first_name.lower()) & 
                     (self.df['Last Name'].str.lower() == last_name.lower())]
        return not exists.empty
    
    def sixdig_id(self):
        return f"{random.randint(1, 999999):06d}"

    @staticmethod
    def is_valid_password(password):
        pattern = r'^[A-Z][a-zA-Z]{4,}[0-9]{3,}$'
        return bool(re.search(pattern, password))

    def write_data(self, data):
      new_row = pd.DataFrame([data], columns=self.df.columns)
      self.df = pd.concat([self.df, new_row], ignore_index=True)
      self.df.to_csv(self.filename, index=False) 

    def enrol_into_a_subject_gui(self, student_id):
        try:
            self.df = pd.read_csv(self.filename)
            if 'Student ID' not in self.df.columns:
                return "The DataFrame is missing the 'Student ID' column."
            self.df['Student ID'] = self.df['Student ID'].astype(int)

            if self.df.empty:
                return "The student records are empty. No enrollments can be processed."

            user_data = self.df.loc[self.df['Student ID'] == student_id]
            if user_data.empty:
                return "No student found with the provided ID."

            courses = ['Course 1', 'Course 2', 'Course 3', 'Course 4']
            marks = ['Course 1 Mark', 'Course 2 Mark', 'Course 3 Mark', 'Course 4 Mark']
            grades = ['Course 1 Grade', 'Course 2 Grade', 'Course 3 Grade', 'Course 4 Grade']

            for col in courses + marks + grades:
                if col not in self.df.columns:
                    self.df[col] = pd.NA

            self.df[grades] = self.df[grades].astype(str)
            self.df[marks] = self.df[marks].replace('', pd.NA).astype(float)

            for i, course in enumerate(courses):
                if pd.isna(user_data.iloc[0][course]) or user_data.iloc[0][course] == '':
                    subject_id, subject_mark, subject_grade = self.subject.create_subject()
                    
                    self.df.loc[self.df['Student ID'] == student_id, course] = int(subject_id)
                    self.df.loc[self.df['Student ID'] == student_id, marks[i]] = float(subject_mark)
                    self.df.loc[self.df['Student ID'] == student_id, grades[i]] = str(subject_grade)

                    self.df.to_csv(self.filename, index=False)
                    self.df = pd.read_csv(self.filename)

                    return f"Enrolled in {course} with ID {subject_id}, Mark: {subject_mark}, Grade: {subject_grade}"

            return "You are already enrolled in 4 subjects."
        except Exception as e:
            return f"An unexpected error occurred: {e}"
    
    def enrol_into_a_subject(self):
        try:
            self.df = pd.read_csv(self.filename)
            if self.df.empty:
                print("The student records are empty. No enrollments can be processed.")
                return
            
            user_data = self.df.loc[self.df['Student ID'] == self.student_id]
            if user_data.empty:
                print("No student found with the given ID.")
                return

            courses = ['Course 1', 'Course 2', 'Course 3', 'Course 4']
            marks = ['Course 1 Mark', 'Course 2 Mark', 'Course 3 Mark', 'Course 4 Mark']
            grades = ['Course 1 Grade', 'Course 2 Grade', 'Course 3 Grade', 'Course 4 Grade']

            for col in courses:
                if col not in self.df.columns:
                    self.df[col] = pd.NA  

            for mark in marks:
                if mark not in self.df.columns:
                    self.df[mark] = pd.NA  

            for grade in grades:
                if grade not in self.df.columns:
                    self.df[grade] = pd.NA

            enrolled = False
            self.df[grades] = self.df[grades].astype(object)

            for i, course in enumerate(courses):
                if pd.isna(user_data.iloc[0][course]) or user_data.iloc[0][course]=='':
                    print(f"\n\033[33m Enrolling in Course {i+1}...\033[0m")
                    subject_id, subject_mark, subject_grade = self.subject.create_subject()

                    self.df.loc[self.df['Student ID'] == self.student_id, course] = int(subject_id)
                    self.df.loc[self.df['Student ID'] == self.student_id, marks[i]] = float(subject_mark)
                    self.df.loc[self.df['Student ID'] == self.student_id, grades[i]] = subject_grade

                    self.df.to_csv(self.filename, index=False)
                    self.df = pd.read_csv(self.filename)

                    print(f"\n Enrolled in {course} with ID {subject_id}, Mark: {subject_mark}, Grade: {subject_grade}")
                    enrolled = True
                    break
            
            if not enrolled:
                print("\n\033[31m You are already enrolled in 4 subjects.\033[0m")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def get_course_id(self):
        while True:
            try:
                course_id_to_remove = int(input("\n\033[33m    Enter Subject ID: \033[0m"))
                return course_id_to_remove 
            except ValueError:  
                print("\033[31m    Invalid input. Please enter a valid integer for the Student ID.\033[0m")

    def remove_subject_from_enrolment_list_gui(self,student_id,entyntry_subject_id):
        try:
            self.df = pd.read_csv(self.filename)
            course_id = entyntry_subject_id
        except ValueError:
            return "Invalid subject ID format. Please enter a numeric ID."

        if self.show_current_enrolment_list_gui(student_id):
            courses = ['Course 1', 'Course 2', 'Course 3', 'Course 4']
            marks = ['Course 1 Mark', 'Course 2 Mark', 'Course 3 Mark', 'Course 4 Mark']
            grades = ['Course 1 Grade', 'Course 2 Grade', 'Course 3 Grade', 'Course 4 Grade']
            for course, mark, grade in zip(courses, marks, grades):
                current_course_id = self.df.loc[self.df['Student ID'] == student_id, course].iloc[0]
                if pd.notna(current_course_id) and int(current_course_id) == course_id:
                    self.df.loc[self.df['Student ID'] == student_id, [course, mark, grade]] = [None, None, None]
                    self.df.to_csv(self.filename, index=False)
                    self.df = pd.read_csv(self.filename)
                    return True, f"Course information for {course_id} has been removed."
            return False, "No such course found to remove."
        else:
            return False, "No subjects are enrolled to remove."

    def remove_subject_from_enrolment_list(self):
        self.df = pd.read_csv(self.filename)
        if self.show_current_enrolment_list():
            course_id = self.get_course_id()
            courses = ['Course 1', 'Course 2', 'Course 3', 'Course 4']
            marks = ['Course 1 Mark', 'Course 2 Mark', 'Course 3 Mark', 'Course 4 Mark']
            grades = ['Course 1 Grade', 'Course 2 Grade', 'Course 3 Grade', 'Course 4 Grade']
            for course, mark, grade in zip(courses, marks, grades):
                if self.df.loc[self.df['Student ID'] == self.student_id, course].iloc[0] == course_id:
                    self.df.loc[self.df['Student ID'] == self.student_id, [course, mark, grade]] = [None, None, None]
                    print(f"\n\033[33m Course information for {course_id} has been removed.\033[0m")
                    self.df.to_csv(self.filename, index=False)
                    self.df = pd.read_csv(self.filename)
                    break
            else:
                print("No such course found to remove.")
        else:
            print("No subjects are enrolled to remove.")

    def show_current_enrolment_list_gui(self,student_id):
        try:
            self.df = pd.read_csv(self.filename)
            student_data = self.df[self.df['Student ID'] == student_id]
            if student_data.empty:
                
                return "You are not enrolled in any subjects." 
            else:
                st_id = int(student_data["Student ID"].iloc[0])
                st_fn = student_data["First Name"].iloc[0]
                st_ln = student_data["Last Name"].iloc[0]
                st_list= f"Student ID {st_id}  First Name  {st_fn}  Last Name {st_ln}"
                enrollment_list = []
                num_courses = 4  
                for i in range(1, num_courses + 1):
                    course_col = f'Course {i}'  
                    mark_col = f'Course {i} Mark'
                    grade_col = f'Course {i} Grade'
                    if pd.notna(student_data.iloc[0][course_col]):
                        course_id = int(student_data.iloc[0][course_col])
                        mark = student_data.iloc[0][mark_col]
                        grade = student_data.iloc[0][grade_col]
                        enrollment_list.append(f"subject:: {course_id} -- mark = {mark} -- grade = {grade}")
                if enrollment_list:
                    return st_list+"\n"+"\n\n".join(enrollment_list)
                else:
                    return st_list+"You are currently not enrolled in any subjects with complete data."
        except KeyError as e:
            return f"An error occurred: {e}. Please check the data format."


    def show_current_enrolment_list(self):
        self.df = pd.read_csv(self.filename)
        print("Student ID:", self.student_id)  
        try:
            student_data = self.df[self.df['Student ID'] == self.student_id]
            if student_data.empty:
                print("You are not enrolled in any subjects.")
                return False
            else:
                enrollment_list = []
                num_courses = 4  
                for i in range(1, num_courses + 1):
                    course_col = f'Course {i}'  
                    mark_col = f'Course {i} Mark'
                    grade_col = f'Course {i} Grade'
                    if pd.notna(student_data.iloc[0][course_col]):
                        course_id = int(student_data.iloc[0][course_col])
                        mark = student_data.iloc[0][mark_col]
                        grade = student_data.iloc[0][grade_col]
                        enrollment_list.append(f"[subject:: {course_id} -- mark = {mark} -- grade = {grade}]")

                if enrollment_list:
                    print(", ".join(enrollment_list))
                    return True
                else:
                    print("You are currently not enrolled in any subjects with complete data.")
                    return False
        except KeyError as e:
            print(f"An error occurred: {e}. Please check the data format.")
            return False

    def change_password_gui(self, student_id, current_password, new_password, confirm_password):
        self.df = pd.read_csv(self.filename)
        if self.df.loc[self.df['Student ID'] == student_id, 'Password'].iloc[0] != current_password:
            return False, "Wrong current password 🤦‍♂️"

        if new_password == current_password:
            return False, "New password cannot be the same as the current password 😒"

        if new_password != confirm_password:
            return False, "New password does not match confirmation"

        if not self.is_valid_password(new_password):
            return False, "Password is invalid. It must start with an uppercase letter followed by at least four more letters and end with three or more digits."

        self.df.loc[self.df['Student ID'] == student_id, 'Password'] = new_password
        self.df.to_csv(self.filename, index=False)
        self.df = pd.read_csv(self.filename)

        return True, "Password updated successfully 🎉✨🎊."

    def change_password(self):
        while True:
            self.df = pd.read_csv(self.filename)
            current_password = input("\nEnter your current password: ").strip()
            if self.df.loc[self.df['Student ID'] == self.student_id, 'Password'].iloc[0] == current_password:
                new_password = input("\nEnter new password: ").strip()
                confirm_password = input("\Confirm new password: ").strip()
                if new_password != current_password:
                    if new_password != confirm_password:
                        print("new password does not match")
                    elif self.is_valid_password(new_password):
                        self.df.loc[self.df['Student ID'] == self.student_id, 'Password'] = new_password
                        self.df.to_csv(self.filename, index=False) 
                        self.df = pd.read_csv(self.filename)
                        print("Password updated successfully 🎉✨🎊.")
                        break
                    else:
                        print("\nPassword is invalid. It must start with an uppercase letter, followed by at least four more letters, and end with three or more digits.")
                else:
                    print("\nNew Password Cannot Equal Current Password 😒")
            else:
                print("Wrong password 🤦‍♂️")
                break

    @staticmethod
    def is_valid_password(password):
        pattern = r'^[A-Z][a-zA-Z]{4,}[0-9]{3,}$'
        return bool(re.search(pattern, password))

    def main_menu0(self):
        print("\n\033[34m   Student Menu: (I)/(R)/(X) or HELP: \033[0m")
        choice = input("").strip().upper()
        return choice

    def student_system(self):
        while True:
            choice = self.main_menu0()
            if choice == 'X':
                break
            elif choice == 'I':
                self.student_login()
            elif choice == 'R':
                self.registration()
            elif choice == 'HELP':
                self.helpss()
            else:
                print("\n\033[31m   Invalid choice, please try again.\033[0m")

    def helpss(self):
        print("\n\033[34m   (I) Login (R)Student Registration Form (X)Exit: \033[0m")

    def student_login_gui(self, username, password):
        student_email = username
        student_password = password
        userpass = self.df.loc[self.df['Email'] == student_email, 'Password'].values
        userID = self.df.loc[self.df['Email'] == student_email, 'Student ID'].values

        if userpass.size > 0 and userID.size > 0:
            if student_password == str(userpass[0]):
                student_id = userID[0]  
                print(f"Student_id = {student_id} with type {type(student_id)}")
                return True, "Correct Student email and password 😉", student_id
            else:
                return False, "Wrong Email or Password 😢"
        else:
            return False, "No record of that student, you need to sign up 😒"

        

    def student_login(self):
        while True:
            student_email = input("\n   Enter your student email: ").strip().lower()
            student_password = input("\n   Enter your password: ").strip()
            userpass = self.df.loc[self.df['Email'] == student_email, 'Password'].values
            userID = self.df.loc[self.df['Email'] == student_email, 'Student ID'].values
            if userpass.size > 0 and userID.size > 0:
                self.student_id = userID[0]
                if student_password == str(userpass[0]):
                    print("\n\033[32m   Correct Student email and password 😉\033[0m")
                    self.run()
                    break  
                else:
                    print("\n\033[31m   Wrong Email or Password 😢\033[0m")
                    break
            else:
                print("\n\033[33m   No record of that student, you need to sign up😒\033[0m")
                break

    def student_menu(self):
        print("\n\033[34m   (E)/(R)/(S)/(C)/(X) or HELP: \033[0m")
        choice = input().strip().upper()
        return choice

    def run(self):
        while True:
            choice = self.student_menu()
            if choice == 'X':
                print("\n\033[33m     Exiting Student menu\nGoodbyen\033[0m")
                break
            elif choice == 'E':
                self.enrol_into_a_subject()
            elif choice == 'R':
                self.remove_subject_from_enrolment_list()
            elif choice == 'S':
                self.show_current_enrolment_list()
            elif choice == 'C':
                self.change_password()
            elif choice == 'HELP':
                self.helpsm()
            else:
                print("     Invalid choice, please try again.")
                choice = self.student_menu()
    
    def helpsm(self):
        print("\n\033[34m   (E)Enroll into a subject/(R)Remove a subject/(S)Show current enrollment/(C)Change password/(X) Exit: \033[0m")


