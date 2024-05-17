import tkinter as tk
from tkinter import messagebox, ttk, Listbox,Label,Button,END,Text,Tk, Entry
from PIL import Image, ImageTk
import pygame
from datetime import datetime
import random
from Student_UI_Updated import Student
from Student_GUI import StudentApp

class Student_LoginApp:
    def __init__(self, master):
        self.master = master
        self.top = tk.Toplevel(master)
        self.image_paths = {
            "logo": "images\\UTS-300x300.png",
            "background": "images\\library.jpg",
            "3d" : "images\\book.jpeg"
        }
        pygame.mixer.init()
        self.student = Student()
        self.student_app = None
        self.initialize_ui()  
    
    def initialize_ui(self):
        self.check_if_png()
        self.load_images()
        self.setup_ui()
        self.play_startup_sound()
        self.setup_moving_image()
        self.animate()
        self.clock()
        self.main()


    def hide_window(self):
        self.top.withdraw()

    def show_window(self):
        self.top.deiconify()
        self.top.lift()
        self.top.focus_force()

    def close_login_window(self):
        self.top.destroy()
        self.launch_student_app()

       
    def setup_moving_image(self):
        self.image = Image.open(self.image_paths["3d"])
        self.image = self.image.resize((50, 50), Image.Resampling.LANCZOS)
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

        self.top.after(50, self.animate)
    
    def clock(self):
        time= datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
        self.canvas.itemconfig(self.time_text, text=f"Day and Time: {time}")
        self.top.after(1000, self.clock)

    def image_clicked(self, event):
        self.play_sound('sounds\office.mp3')
        text_id = self.canvas.create_text(150, 50, text="Dont You Have Better Things To Do 🥺!", fill="black", font=('Times New Roman', 12, 'bold'))
        self.top.after(3000, lambda: self.remove_text(text_id))

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
            self.bg_width = 600
            self.bg_height = 400
            self.top.geometry(f"{self.bg_width}x{self.bg_height}")
            print(f"{self.bg_width}x{self.bg_height}")
            background_image = background_image.resize((self.bg_width, self.bg_height), Image.Resampling.LANCZOS)
            self.background_image = ImageTk.PhotoImage(background_image)

            logo_image = Image.open(self.image_paths["logo"])
            logo_image = logo_image.resize((100, 100), Image.Resampling.LANCZOS)
            self.logo_image = ImageTk.PhotoImage(logo_image)
        except IOError as e:
            print(f"Error opening image files: {e}")

    def setup_ui(self):
        self.canvas = tk.Canvas(self.top, width=self.bg_width, height=self.bg_height)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.background_image, anchor="nw")
        self.canvas.create_image(self.bg_width/1.1, self.bg_height/10, image=self.logo_image, anchor="center")
        self.time_text = self.canvas.create_text(150, 10, text="", fill="black", font=('Helvetica', 12))
        self.create_buttons()



    def play_startup_sound(self):
        self.play_sound('sounds\\office.mp3')  
           

    def create_buttons(self):
        go_back_button = tk.Button(self.top, text="Go Back", command=self.go_back_button_clicked)
        go_back_button.pack()  # Adjust packing as needed
        log_in_button = tk.Button(self.top, text="Student LOGIN", command= self.login)
        Registration_button = tk.Button(self.top, text="Student Registration Foarm", command=self.registration)
        
        self.canvas.create_window(self.bg_height/6, self.bg_width/5.0, anchor="nw", window=log_in_button)
        self.canvas.create_window(self.bg_height/6, self.bg_width/3.8, anchor="nw", window=Registration_button)
        self.canvas.create_window(self.bg_height/1, self.bg_width/1.7, anchor="nw", window=go_back_button)

    def reg(self):
        self.root = tk.Toplevel()
        self.root.geometry("400x400")  
        self.root.title("Students Registration Foarm")
        fields = 'First Name', 'Last Name', 'Email', 'Password'
        entries = {}
        for index, field in enumerate(fields):
            lab = tk.Label(self.root, width=10, text=field, anchor='w')
            lab.grid(row=index, column=0, padx=5, pady=5)
            ent = tk.Entry(self.root,width=30)
            ent.grid(row=index, column=1, padx=5, pady=5, sticky='ew')
            entries[field] = ent
        
        b1 = tk.Button(self.root, text='Register',command=lambda:self.register_button_clicked(entries))
        b1.grid(row=len(fields), column=0, padx=5, pady=1, sticky='ew')
        b2 = tk.Button(self.root, text='Quit', command=self.quit_button_clicked)
        b2.grid(row=len(fields), column=1, padx=5, pady=1, sticky='ew')

    def register_button_clicked(self, entries):
        self.play_sound('sounds\\mouse_sound.mp3')
        self.register_student(entries)
    
    def quit_button_clicked(self):
        self.play_sound('sounds\\nintendo-game-boy-startup.mp3')
        self.root.after(1000, self.root.destroy)


    
    def register_student(self,entries):
        try:
            # Gather data from entries
            first_name = entries['First Name'].get()
            last_name = entries['Last Name'].get()
            email = entries['Email'].get()
            password = entries['Password'].get()
            
            success, message = self.student.registration_gui(first_name, last_name, email, password)
            if success:
                messagebox.showinfo("Registration Successful", message)
                pass
            else:
                messagebox.showerror("Registration Failed", message)
                pass
        except ValueError:
            messagebox.showerror("Error")
            return
        finally:
            self.root.after(1500, self.root.destroy)

    def log(self):
        self.root = tk.Toplevel()
        self.root.geometry("400x400")  
        self.root.title("Students LogIn")    
        self.root.configure(background='light blue')  

        entry_username = tk.Entry(self.root)
        entry_username.pack()
        label_username = tk.Label(self.root, text="Username:", bg='light pink')
        label_username.pack()

        entry_password = tk.Entry(self.root, show="*")
        entry_password.pack()
        label_password = tk.Label(self.root, text="Password:", bg='light pink')
        label_password.pack()

        button_login_student = tk.Button(self.root, text="Login as Student", command=lambda: self.login_as_student(entry_username, entry_password))
        button_login_student.pack()

        self.status_label = tk.Label(self.root, text="", bg='light blue')
        self.status_label.pack()



    def login_as_student(self, entry_username, entry_password):
        try:
            username = entry_username.get()
            password = entry_password.get()
            success, message, student_id = self.student.student_login_gui(username, password)
            print(f"Student_id = {student_id} with type {type(student_id)}")
            if success:
                self.status_label.config(text="Login successful!")
                self.root.after(1000, lambda: self.close_login_window(student_id))
            else:
                self.status_label.config(text="Login failed: " + message)
        except ValueError:
            messagebox.showerror("Error", "Invalid input or error during login.")
        finally:
            self.root.after(1500, self.root.destroy)


    def close_login_window(self,student_id):
        print("closing")
        self.root.destroy()
        print("closed")
        self.lunch_studentapp(student_id)
        self.go_back_button_clicked()


    def lunch_studentapp(self,student_id):
        if self.student_app is None or not self.student_app.root.winfo_exists():
            self.student_app = StudentApp(self.master,student_id)
        else:
            self.student_app.show_window()


    def go_back_button_clicked(self):
        print("Go Back button clicked.")
        self.master.deiconify()
        self.exit_app()


    def exit_app(self):
        print("Preparing to exit app...")
        pygame.mixer.quit()
        self.top.destroy()
        
    def login(self):
        self.play_sound('sounds\\nintendo-game-boy-startup.mp3')
        self.log()

    def registration(self):
        self.play_sound('sounds\\mouse_sound.mp3')
        self.reg()
        
    
        

    def play_sound(self, sound_file):
        try:
            sound = pygame.mixer.Sound(sound_file)
            if not sound.get_num_channels():  
                sound.play()
        except Exception as e:
            print(f"Error playing sound: {e}")
    


    def main(self):
        self.top.title("Student Log IN and Registration")
        self.top.mainloop()
    

