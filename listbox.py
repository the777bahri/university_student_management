import tkinter as tk
from tkinter import messagebox, ttk, Listbox,Label,Button,END,Text,Tk, Entry

def log():
    root = tk.Tk()
    root.geometry("300x300")  
    root.title("Students LogIn")    
    root.configure(background='light blue')  

    entry_username = tk.Entry(root)
    entry_username.pack()
    label_username = tk.Label(root, text="Username:", bg='light black')
    label_username.pack()

    entry_password = tk.Entry(root, show="*")
    entry_password.pack()
    label_password = tk.Label(root, text="Password:", bg='light black')
    label_password.pack()

    button_login_student = tk.Button(root, text="Login as Student", command=lambda:login_as_student(entry_username, entry_password))
    button_login_student.pack()


def login_as_student(entry_username, entry_password):
    username = entry_username.get()
    password = entry_password.get()
    # Add your authentication logic here
    messagebox.showinfo("Login Attempt", f"Logging in as Staff with Username: {username} and pasword {password}")
    
