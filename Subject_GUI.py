import tkinter as tk
from tkinter import messagebox, ttk, Listbox,Label,Button,END,Text,Tk, Entry
from PIL import Image, ImageTk
import pygame
from datetime import datetime
import random
from Admin_UI_Updated import Admin

class AdminApp:
    def __init__(self, master):
        self.root = tk.Toplevel(master)
        self.root.title("Admin Menu")
        self.image_paths = {
            "logo": "images\\UTS-300x300.png",
            "background": "images\\admin.jpg",
            "kitty" : "images\\kitty.png"
        }
        self.admin = Admin()

        self.initialize_ui()  
    
    def initialize_ui(self):
        self.load_images()
        self.setup_ui()
        self.check_if_png()
        self.play_startup_sound()
        self.setup_moving_image()
        self.animate()
        self.clock()
        self.main()

    def hide_window(self):
        self.root.withdraw()

    def show_window(self):
        self.root.deiconify()
        self.root.lift()
        self.root.focus_force()

       
    def setup_moving_image(self):
        self.image = Image.open(self.image_paths["kitty"])
        self.image = self.image.resize((100, 100), Image.Resampling.LANCZOS)
        self.tk_image = ImageTk.PhotoImage(self.image)
        
        self.pos_x = random.randint(0, self.bg_width - 100)
        self.pos_y = random.randint(0, self.bg_height - 100)
        self.move_x = random.choice([-4, 4])
        self.move_y = random.choice([-4, 4])

        self.image_id = self.canvas.create_image(self.pos_x, self.pos_y, image=self.tk_image, anchor="nw", tags="clickable_image")
        self.canvas.tag_bind("clickable_image", "<Button-1>", self.image_clicked)

        self.animate()  


    def animate(self):
        self.pos_x += self.move_x
        self.pos_y += self.move_y


        if self.pos_x <= 0 or self.pos_x >= (self.bg_width - 100):
            self.move_x = -self.move_x
        if self.pos_y <= 0 or self.pos_y >= (self.bg_height - 100):
            self.move_y = -self.move_y

        self.canvas.move(self.image_id, self.move_x, self.move_y)

        if random.randint(1, 100) > 98:
            self.move_x = random.choice([-4, 4])
            self.move_y = random.choice([-4, 4])

        self.root.after(50, self.animate)
    
    def clock(self):
        time= datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
        self.time_text = self.canvas.create_text(150, 10, text="", fill="white", font=('Helvetica', 12))
        self.canvas.itemconfig(self.time_text, text=f"Day and Time: {time}")
        self.root.after(1000, self.clock)

    def image_clicked(self, event):
        self.play_sound('sounds\error_CDOxCYm.mp3')
        text_id = self.canvas.create_text(150, 50, text="leave me alone 🥺😽!", fill="pink", font=('Helvetica', 12))
        self.play_sound('sounds\kitty1.mp3')
        self.root.after(3000, lambda: self.remove_text(text_id))

    def remove_text(self, text):
        self.canvas.delete(text)

    def convert_jpg_to_png(self, jpg_file_path, png_file_path):
        img = Image.open(jpg_file_path)
        img.save(png_file_path, 'PNG')
        print(f"Open {jpg_file_path}, Saved {png_file_path}")

    def check_if_png(self):
        for key, path in self.image_paths.items():
            if not path.lower().endswith('.png'):
                png_path = path.rsplit('.', 1)[0] + '.png'
                self.convert_jpg_to_png(path, png_path)
                self.image_paths[key] = png_path  
                print(f"Converted {path} to {png_path}")
            else:
                print(f"{path} is already in PNG format.")

    def load_images(self):
        try:
            background_image = Image.open(self.image_paths["background"])
            self.bg_width, self.bg_height = background_image.size
            self.root.geometry(f"{self.bg_width}x{self.bg_height}")
            print(f"{self.bg_width}x{self.bg_height}")
            background_image = background_image.resize((self.bg_width, self.bg_height), Image.Resampling.LANCZOS)
            self.background_image = ImageTk.PhotoImage(background_image)

            logo_image = Image.open(self.image_paths["logo"])
            logo_image = logo_image.resize((100, 100), Image.Resampling.LANCZOS)
            self.logo_image = ImageTk.PhotoImage(logo_image)
        except IOError as e:
            print(f"Error opening image files: {e}")

    def setup_ui(self):
        self.canvas = tk.Canvas(self.root, width=self.bg_width, height=self.bg_height)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.background_image, anchor="nw")
        self.canvas.create_image(self.bg_width/1.1, self.bg_height/10, image=self.logo_image, anchor="center")
        self.clock()
        self.create_buttons()
        self.button_open = Button(self.master, text="Remove Student", command=self.remove_student)
        self.button_open.pack()


    def play_startup_sound(self):
        self.play_sound('sounds\\office.mp3')  
           

    def create_buttons(self):
        go_back_button = tk.Button(self.root, text="Go Back", command=self.go_back_button_clicked)
        go_back_button.pack()  # Adjust packing as needed
        help_button = tk.Button(self.root, text="Help", command=self.help_button_clicked)
        clear_button = tk.Button(self.root, text="Cear Database", command= self.clears_button_clicked)
        group_button = tk.Button(self.root, text="Group Students Based on Grade", command=self.group_button_clicked)
        partition_button = tk.Button(self.root, text="Partition Students by Pass/Fail", command=self.partition_button_clicked)
        remove_button = tk.Button(self.root, text="Remove a Student", command=self.remove_button_clicked)
        show_button = tk.Button(self.root, text="Show all Students", command=self.show_button_clicked )
        show_button.pack(pady=20)

        self.canvas.create_window(self.bg_height/6, self.bg_width/5.0, anchor="nw", window=clear_button)
        self.canvas.create_window(self.bg_height/6, self.bg_width/3.8, anchor="nw", window=group_button)
        self.canvas.create_window(self.bg_height/6, self.bg_width/3.0, anchor="nw", window=partition_button)
        self.canvas.create_window(self.bg_height/6, self.bg_width/2.5, anchor="nw", window=remove_button)
        self.canvas.create_window(self.bg_height/6, self.bg_width/2.0, anchor="nw", window=show_button)
        self.canvas.create_window(self.bg_height/7, self.bg_width/1.7, anchor="nw", window=help_button)
        self.canvas.create_window(self.bg_height/1, self.bg_width/1.7, anchor="nw", window=go_back_button)

    def list_all(self):
        top = tk.Toplevel()
        top.geometry("600x600")  
        top.title("Students List") 
        style = ttk.Style(top)
        style.configure("Treeview", font=('Times New Roman', 12))
        columns = ('First Name', 'Last Name', 'Student ID', 'Email')
        tree = ttk.Treeview(top, columns=columns, show='headings')
        for col in columns:
            tree.heading(col, text=col)

        first_names, last_names, ids, emails = self.admin.view_all_gui()
        for f, l, i, e in zip(first_names, last_names, ids, emails):
            tree.insert('', tk.END, values=(f, l, i, e))

        tree.pack(expand=True, fill='both')
        top.update_idletasks()  
        top.geometry(f"{tree.winfo_reqwidth()}x{tree.winfo_reqheight()}")  

        top.minsize(tree.winfo_width(), tree.winfo_height())

    def list_grade(self):
        top = tk.Toplevel()
        top.geometry("600x600")  
        top.title("Student Grades List")
        grades = self.admin.view_grade_gui()


        tree = ttk.Treeview(top, columns=('Course', 'Course ID', 'Student', 'Student ID', 'Grade', 'Mark'), show='headings')
        for col in ('Course', 'Grade', 'Student', 'Student ID', 'Course ID', 'Mark'):
            tree.heading(col, text=col)
            tree.column(col, anchor="w")

        for grade in grades:
            tree.insert('', 'end', values=(grade['Course'], grade['Course ID'], grade['Student'], grade['Student ID'], grade['Grade'], grade['Mark']))

        tree.pack(expand=True, fill='both')
        top.update_idletasks() 
        top.geometry(f"{tree.winfo_reqwidth()}x{tree.winfo_reqheight()}")  
        top.minsize(tree.winfo_width(), tree.winfo_height())

    def list_pass_fail(self):
        top = tk.Toplevel()
        top.geometry("600x600")  
        top.title("Student Pass/Fail List")
        results = self.admin.view_pass_fail_gui()
        pass_list = results["Pass"]
        fail_list = results["Fail"]

        tree = ttk.Treeview(top, columns=('Course', 'Course ID',  'Student', 'Student ID','Grade', 'Mark'), show='headings')
        for col in ('Course', 'Course ID',  'Student', 'Student ID','Grade', 'Mark'):
            tree.heading(col, text=col)
            tree.column(col, anchor="w")

        for student in pass_list:
            values = (student["Course"],student["Course ID"], student["Name"], student["Student ID"], student["Grade"], student["Mark"])
            tree.insert('', 'end', values=values)
        
        for student in fail_list:
            values = (student["Course"],student["Course ID"], student["Name"], student["Student ID"], student["Grade"], student["Mark"])
            tree.insert('', 'end', values=values)

        tree.pack(expand=True, fill='both')
        top.update_idletasks() 
        top.geometry(f"{tree.winfo_reqwidth()}x{tree.winfo_reqheight()}")  
        top.minsize(tree.winfo_width(), tree.winfo_height())

    def remove_student(self):
        self.top = tk.Toplevel()
        self.top.geometry("200x200")
        self.top.title("Remove a Student")

        self.entry_student_id = Entry(self.top, width=20)
        self.entry_student_id.pack(pady=10)
        Label(self.top, text="Enter Student ID:", font=('Calibri', 12)).pack()

        self.label = Label(self.top, text="", font=('Calibri', 15))
        self.label.pack()

        button_submit_id = Button(self.top, text="Submit ID", command=self.validate_student_id)
        button_submit_id.pack(pady=10)
        
    def validate_student_id(self):
        try:
            student_id = int(self.entry_student_id.get())  # Validate and convert input
            # Attempt to remove the student using the admin method
            removed, message = self.admin.remove_one_gui(student_id)
            if removed:
                self.label.config(text="Student deleted successfully 💀")
                self.list_all()
                pass
            else:
                self.label.config(text="No student found with the given ID 😒")
                pass
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid integer for the Student ID.")
            self.entry_student_id.delete(0, END)
            return
        finally:
            self.top.after(1500, self.top.destroy)

    def clear_all(self):
        self.top = tk.Toplevel()
        self.top.geometry("300x300")
        self.top.title("Remove All Students")

        Label(self.top, text="Delete All Students😰🥶?", font=('Calibri', 12)).pack()

        self.label = Label(self.top, text="", font=('Calibri', 10))
        self.label.pack()

        yes_button = Button(self.top, text="Yes", command=self.delete_all)
        no_button = Button(self.top, text="No", command=self.top.destroy)
        yes_button.pack(padx =5 ,pady=5)
        no_button.pack(padx = 15,pady=5)

    def delete_all(self):
        self.admin.remove_all_gui()


    def go_back_button_clicked(self):
        self.exit_app()

    def exit_app(self):
        self.root.after(500,lambda:self.quit())
    
    def quit(self):
        pygame.mixer.quit()
        self.root.destroy()


    def help_button_clicked(self):
        self.play_sound('sounds\\huh.mp3')
        self.admin.help()
        
    def clears_button_clicked(self):
        self.play_sound('sounds\\mouse_sound.mp3')
        self.clear_all()

    def group_button_clicked(self):
        self.play_sound('sounds\\nintendo-game-boy-startup.mp3')
        self.list_grade()

    def partition_button_clicked(self):
        self.play_sound('sounds\\mouse_sound.mp3')
        self.list_pass_fail()

    def remove_button_clicked(self):
        self.play_sound('sounds\\nintendo-game-boy-startup.mp3')
        self.remove_student()

    def show_button_clicked(self):
        self.play_sound('sounds\\mouse_sound.mp3')
        self.list_all()

    def play_sound(self, sound_file):
        if not pygame.mixer.get_init():
            pygame.mixer.init()
        try:
            sound = pygame.mixer.Sound(sound_file)
            if not sound.get_num_channels():  # Check if the sound is already playing
                sound.play()
        except Exception as e:
            print(f"Error playing sound: {e}")


    def main(self):
        self.root.title("Admin Menu 👨‍💻")
        self.root.mainloop()
    

