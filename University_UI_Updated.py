from Admin_UI_Updated import Admin
from Student_UI_Updated import Student

class University:
    def __init__(self):    
        self.admin = Admin()
        self.student = Student()

    def main_menu(self):
        print("\n\033[34m University System: (A)/(S)/(X) or HELP: \033[0m")
        choice = input("").strip().upper()
        return choice

    def run(self):
        while True:
            choice = self.main_menu()
            if choice == 'X':
                print("\n\033[33m Exiting University System\nGoodbye\n\033[0m")
                break
            elif choice == 'A':
                self.admin.admin_login()
            elif choice == 'S':
                self.student.student_system()
            elif choice == 'HELP':
                self.help()
            else:
                print("\n\033[31m Invalid choice, please try again.\033[0m")
                self.help()
                choice = self.main_menu()
    
    def help(self):
        print("\n\033[34m\n(A) Admin, (S) Student, or (X) Exit: \033[0m")


if __name__ == '__main__':
    university = University()
    university.run()
