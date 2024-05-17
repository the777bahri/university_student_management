import pandas as pd
from datetime import datetime
import math

class Admin:
    def __init__(self, filename='dataset\students_data.csv'):
        self.name = "John Smith"
        self.email = "john.smith@university.com"
        self.password = 'Admin123'
        self.filename = filename
        self.df = pd.read_csv(filename)
    
    def view_all_gui(self):
        try:
            pd.set_option('display.max_columns', None) 
            pd.set_option('display.max_rows', None)    
            df = pd.read_csv(self.filename)
            if len(df) <= 0:
                print("\nThe dataset is empty")
                return [],[],[],[]
            else:
                print("\nData read successfully.")
                student_first_name = [f"{row['First Name']}"for index, row in df.iterrows()]
                student_Last_name = [f"{row['Last Name']}"for index, row in df.iterrows()]
                student_ID = [f"{row['Student ID']}"for index, row in df.iterrows()]
                student_email = [f"{row['Email']}"for index, row in df.iterrows()]
                return student_first_name, student_Last_name, student_ID, student_email
        except FileNotFoundError:
            print("No registered students found ☠⚰💀")
            return [],[],[],[]

    def view_all(self):
        try:
            pd.set_option('display.max_columns', None) 
            pd.set_option('display.max_rows', None)  
            self.df = pd.read_csv(self.filename)
            if(len(self.df) <= 0):
                print("\nThe dataset is empty")
            else:
                print("\nData read successfully.")
            for index, row in self.df.iterrows():
                print(f"{row['First Name']} {row['Last Name']} :: ID:{row['Student ID']} --> email: {row['Email']}")
        except FileNotFoundError:
            print("No registered students found ☠⚰💀")
            return pd.DataFrame(columns=self.headers)
        
    def view_grade_gui(self):
        df = pd.read_csv(self.filename)
        grade_order = pd.CategoricalDtype(['HD', 'D', 'C', 'P', 'Z'], ordered=True)
        grade_columns = ['Course 1 Grade', 'Course 2 Grade', 'Course 3 Grade', 'Course 4 Grade']
        mark_columns = ['Course 1 Mark', 'Course 2 Mark', 'Course 3 Mark', 'Course 4 Mark']
        course_ids = ['Course 1', 'Course 2', 'Course 3', 'Course 4']

        for col in grade_columns:
            df[col] = df[col].astype(grade_order)

        df.sort_values(by=mark_columns + grade_columns, ascending=[False] * len(mark_columns) + [True] * len(grade_columns), inplace=True)
        results = []
        for course_id, grade_col, mark_col in zip(course_ids, grade_columns, mark_columns):
            for grade, group in df.groupby(grade_col, observed=True):
                for _, row in group.iterrows():
                    results.append({
                        'Course': course_id,
                        'Grade': grade_col,
                        'Student': f"{row['First Name']} {row['Last Name']}",
                        'Student ID': row['Student ID'],
                        'Course ID': row[course_id],
                        'Grade': row[grade_col],
                        'Mark': row[mark_col]
                    })
        return results
    
    def view_grade(self):
        self.df = pd.read_csv(self.filename)
        
        grade_order = pd.CategoricalDtype(['HD', 'D', 'C', 'P', 'Z'], ordered=True)
        grade_columns = ['Course 1 Grade', 'Course 2 Grade', 'Course 3 Grade', 'Course 4 Grade']
        mark_columns = ['Course 1 Mark', 'Course 2 Mark', 'Course 3 Mark', 'Course 4 Mark']
        course_ids = ['Course 1', 'Course 2', 'Course 3', 'Course 4']

        for col in grade_columns:
            self.df[col] = self.df[col].astype(grade_order)

        self.df.sort_values(by=mark_columns + grade_columns, ascending=[False] * len(mark_columns) + [True] * len(grade_columns), inplace=True)

        for course_id, grade_col, mark_col in zip(course_ids, grade_columns, mark_columns):
            print(f"\n{grade_col} -->")
            grouped = self.df.groupby(grade_col, observed=True)
            for grade, group in grouped:
                print(f"  {grade} --> [", end="")
                for _, row in group.iterrows():
                    print(f"{row['First Name']} {row['Last Name']} :: Student ID: {row['Student ID']} :: Course ID: {row[course_id]} --> grade: {row[grade_col]} -mark: {row[mark_col]}; ", end="")
                print("]")

        pd.reset_option('display.max_columns')
        pd.reset_option('display.max_rows')

    def view_pass_fail_gui(self):
        self.df = pd.read_csv(self.filename)
        grade_columns = ['Course 1 Grade', 'Course 2 Grade', 'Course 3 Grade', 'Course 4 Grade']
        mark_columns = ['Course 1 Mark', 'Course 2 Mark', 'Course 3 Mark', 'Course 4 Mark']
        course_id_columns = ['Course 1', 'Course 2', 'Course 3', 'Course 4']

        pass_list = []
        fail_list = []

        for index, row in self.df.iterrows():
            for grade_col, mark_col, course_id_col in zip(grade_columns, mark_columns, course_id_columns):
                if not math.isnan(row[mark_col]):
                    student_info = {
                                        "Name": f"{row['First Name']} {row['Last Name']}",
                                        "Student ID": row['Student ID'],
                                        "Course": row[course_id_col],
                                        "Course ID":course_id_col,
                                        "Grade": row[grade_col],
                                        "Mark": row[mark_col]
                                    }                    
                    if row[grade_col] in ['P', 'C', 'D', 'HD']: 
                        pass_list.append(student_info)
                    else:
                        fail_list.append(student_info)
        return {"Pass": pass_list, "Fail": fail_list}


    def view_pass_fail(self):
        self.df = pd.read_csv(self.filename)
        grade_columns = ['Course 1 Grade', 'Course 2 Grade', 'Course 3 Grade', 'Course 4 Grade']
        mark_columns = ['Course 1 Mark', 'Course 2 Mark', 'Course 3 Mark', 'Course 4 Mark']
        course_id_columns = ['Course 1', 'Course 2', 'Course 3', 'Course 4']

        pass_dict = {col: [] for col in grade_columns}
        fail_dict = {col: [] for col in grade_columns}

        for index, row in self.df.iterrows():
            for grade_col, mark_col, course_id_col in zip(grade_columns, mark_columns, course_id_columns):
                if not math.isnan(row[mark_col]):
                    student_info = f"{row['First Name']} {row['Last Name']} :: Student ID: {row['Student ID']} :: Course ID: {row[course_id_col]} --> grade: {row[grade_col]}, mark: {row[mark_col]}"
                    if row[grade_col] in ['P', 'C', 'D', 'HD']: 
                        pass_dict[grade_col].append(student_info)
                    else:
                        fail_dict[grade_col].append(student_info)

        for grade_col in grade_columns:
            print(f"\n{grade_col} Fail --> [", end="")
            print(", ".join(fail_dict[grade_col]), end="]\n")
            print(f"{grade_col} Pass --> [", end="")
            print(", ".join(pass_dict[grade_col]), end="]\n")

    def get_student_id(self):
        while True:
            try:
                student_id_input = int(input("\n\033[33m    Enter Student ID: \033[0m"))
                student_id = student_id_input 
                return student_id 
            except ValueError:  
                print("\033[31m    Invalid input. Please enter a valid integer for the Student ID.\033[0m")

    
    def remove_one_gui(self, student_id):
        self.df = pd.read_csv(self.filename)
        condition = (self.df['Student ID'] == student_id)
        if not self.df[condition].empty:
            self.df = self.df.drop(self.df[condition].index)
            self.df.to_csv(self.filename, index=False)
            print("\nStudent record deleted successfully💀")
            self.df = pd.read_csv(self.filename)
            self.view_all()
            return True, "Student deleted successfully."
        else:
            print("\nNo student found with the given ID 😒")
            self.df.to_csv(self.filename, index=False)
            self.df = pd.read_csv(self.filename)
            return False, "No student found with the given ID."

    def remove_one(self):
        self.df = pd.read_csv(self.filename)
        student_id = self.get_student_id()
        condition = (self.df['Student ID'] == student_id)
        if not self.df[condition].empty:
            self.df = self.df.drop(self.df[condition].index)
            self.df.to_csv(self.filename, index=False)
            self.df = pd.read_csv(self.filename)
            print("\nStudent record deleted successfully💀")
            self.df = pd.read_csv(self.filename)
            self.view_all()
        else:
            print("\nNo student found with the given ID 😒 ")
        self.df.to_csv(self.filename, index=False)
        self.df = pd.read_csv(self.filename)


    def remove_all_gui(self):
        self.df = pd.DataFrame(columns=self.df.columns) 
        self.df.to_csv(self.filename, index=False)
        self.df = pd.read_csv(self.filename)
        print("\nAll data has been deleted 😭💀")
        self.view_all()

    def remove_all(self):
        self.df = pd.read_csv(self.filename)
        print("\n✋ARE YOU REALLY SURE THAT YOU WANT TO DELETE ALL THE STUDENTS RECORD?😨😱\nY = YES\nN = NO")
        final_answer = input("\nChoose an option😰🥶: ").strip().upper()
        if final_answer == "Y":
            admin_password = input("Please enter the admin password: ")
            if admin_password == self.password:
                print("Erasing the data.....")
                self.df = pd.DataFrame(columns=self.df.columns)
                self.df.to_csv(self.filename, index=False)
                self.df = pd.read_csv(self.filename)
                print("\nAll data has been deleted 😭💀")
                self.view_all()
            else:
                print("Wrong password")
            return  
        elif final_answer == "N":
            print("OK, that's amazing 🙏")
        else:
            print("     Wrong, enter either Y or N")
            return self.remove_all()  

        
    def admin_login(self):
        print("\n\033[32m   Day and Time: " + datetime.now().strftime('%Y-%m-%d %I:%M:%S %p\033[0m'))
        print(f"\n\033[32m  {self.name}   admin menu:\033[0m")
        self.run()

    def admin_menu(self):
        choice = input("\n\033[34m   Admin System:(C)/(G)/(P)/(R)/(S)/(X)/HELP: \033[0m").strip().upper()
        return choice

    def run(self):
        while True:
            choice = self.admin_menu()
            if choice == 'X':
                print("\n\033[33m   Closing Admin menu\nGoodbye\033[0m")
                break
            elif choice == 'S':
                self.view_all()
            elif choice == 'G':
                self.view_grade()
            elif choice == 'P':
                self.view_pass_fail()
            elif choice == 'R':
                self.remove_one()
            elif choice == 'C':
                self.remove_all()
            elif choice == 'HELP':
                self.help()
            else:
                print("\n\033[31m    Invalid choice, please try again. 😒\033[0m")
                choice = self.admin_menu()
    
    def help(self):
        print("\n\033[34m       (C)Clear Database File(G)Group Students Based on Grade(P)Partition Students(R)Remove Student(S)Show All Students(X)Exit: \033[0m")


