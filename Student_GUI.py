import tkinter as tk
from tkinter import messagebox, ttk, Listbox,Label,Button,END,Text,Tk, Entry
from PIL import Image, ImageTk
import pygame
from datetime import datetime
import random
from Student_UI_Updated import Student

class StudentApp:
    def __init__(self, master, student_id):
        self.root = tk.Toplevel(master)
        self.image_paths = {
            "logo": "images\\UTS-300x300.png",
            "background": "images\\library.jpg",
            "3d" : "images\\book.jpeg"
        }
        self.student_id = student_id
        pygame.mixer.init()
        self.student = Student()


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
        self.root.withdraw()

    def show_window(self):
        self.root.deiconify()
        self.root.lift()
        self.root.focus_force()

       
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

        self.root.after(50, self.animate)
    
    def clock(self):
        time= datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
        self.canvas.itemconfig(self.time_text, text=f"Day and Time: {time}")
        self.root.after(1000, self.clock)

    def image_clicked(self, event):
        self.play_sound('sounds\office.mp3')
        text_id = self.canvas.create_text(150, 50, text="GO Study!", fill="red", font=('Times New Roman', 20, 'bold'))
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
            self.bg_width = 600
            self.bg_height = 400
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
        self.time_text = self.canvas.create_text(150, 10, text="", fill="black", font=('Helvetica', 12))
        self.create_buttons()
   


    def play_startup_sound(self):
        self.play_sound('sounds\\office.mp3')  
           

    def create_buttons(self):
        go_back_button = tk.Button(self.root, text="Go Back", command=self.go_back_button_clicked)
        go_back_button.pack()  # Adjust packing as needed
        help_button = tk.Button(self.root, text="Help", command=self.help_button_clicked)
        enrol_button = tk.Button(self.root, text="Enroll into a subject", command= self.enrol_into_subject_clicked)
        remove_subject_button = tk.Button(self.root, text="Remove a subject", command=self.remove_subject_clicked)
        current_enrollment_button = tk.Button(self.root, text="Show current enrollment", command=self.show_enrollment_clicked)
        change_password_button = tk.Button(self.root, text="Change password", command=self.change_password_clicked)

        self.canvas.create_window(self.bg_height/6, self.bg_width/5.0, anchor="nw", window=enrol_button)
        self.canvas.create_window(self.bg_height/6, self.bg_width/3.8, anchor="nw", window=remove_subject_button)
        self.canvas.create_window(self.bg_height/6, self.bg_width/3.0, anchor="nw", window=current_enrollment_button)
        self.canvas.create_window(self.bg_height/6, self.bg_width/2.5, anchor="nw", window=change_password_button)
        self.canvas.create_window(self.bg_height/7, self.bg_width/1.7, anchor="nw", window=help_button)
        self.canvas.create_window(self.bg_height/1, self.bg_width/1.7, anchor="nw", window=go_back_button)

    def enrol_into_subject(self):
        top = tk.Toplevel()
        top.geometry("300x300")  
        top.title("Enrol Into a Subject")

        self.status_label = tk.Label(top, text="", justify=tk.LEFT, anchor="nw")
        self.status_label.pack(expand=True, fill=tk.BOTH)
        self.handle_enrollment(self.student_id)

    def handle_enrollment(self, student_id):
        message = self.student.enrol_into_a_subject_gui(student_id)
        self.status_label.config(text=message)


    def remove_subject(self):
        top = tk.Toplevel()
        top.geometry("300x300")  
        top.title("Remove a Subject")
        entry_subject_id = tk.Entry(top)
        entry_subject_id.pack()
        label_subject_id = tk.Label(top, text="Subject ID:", bg='light pink')
        label_subject_id.pack()
        status_label = tk.Label(top, text="", justify=tk.LEFT, anchor="nw")
        status_label.pack(expand=True, fill=tk.BOTH)
        button_remove = tk.Button(top, text="Remove Subject", command=lambda: self.validate_student_id(entry_subject_id, status_label,top))
        button_remove.pack()
    
    def validate_student_id(self, entry_subject_id, status_label, top):
        try:
            subject_id = int(entry_subject_id.get())
            removed, message = self.student.remove_subject_from_enrolment_list_gui(self.student_id,subject_id)
            status_label.config(text=message)
            if removed:
                status_label.config(text="Student deleted successfully 💀")
                pass
            else:
                status_label.config(text="No course found with the given ID 😒")
                pass
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid integer for the Student ID.")
            entry_subject_id.delete(0, END)
            return
        finally:
            top.after(1500, top.destroy)

    def show_enrollment(self):
        top = tk.Toplevel()
        top.geometry("300x300")  
        top.title("Student Current Enrollment List")
        self.status_label = tk.Label(top, text="", justify=tk.LEFT, anchor="nw")
        self.status_label.pack(expand=True, fill=tk.BOTH)
        self.show_course(self.student_id)

    def show_course(self, student_id):
        message = self.student.show_current_enrolment_list_gui(student_id)
        self.status_label.config(text=message)

    def change_password(self):
        top = tk.Toplevel()
        top.geometry("300x300")
        top.title("Change Password")
        status_label = tk.Label(top, text="", justify=tk.LEFT, anchor="nw")
        status_label.pack(expand=True, fill=tk.BOTH)

        entry_current_password = tk.Entry(top, show="*")
        entry_current_password.pack()
        label_current_password = tk.Label(top, text="Current Password:", bg='light pink')
        label_current_password.pack()

        entry_new_password = tk.Entry(top, show="*")
        entry_new_password.pack()
        label_new_password = tk.Label(top, text="New Password:", bg='light pink')
        label_new_password.pack()

        entry_confirm_password = tk.Entry(top, show="*")
        entry_confirm_password.pack()
        label_confirm_password = tk.Label(top, text="Confirm Password:", bg='light pink')
        label_confirm_password.pack()

        update_password = tk.Button(top, text="Change Password", command=lambda: self.validate_student_password(status_label, entry_current_password, entry_new_password, entry_confirm_password, top))
        update_password.pack()

    def validate_student_password(self, status_label, entry_current_password, entry_new_password, entry_confirm_password, top):
        current_password = entry_current_password.get()
        new_password = entry_new_password.get()
        confirm_password = entry_confirm_password.get()

        update, message = self.student.change_password_gui(self.student_id, current_password, new_password, confirm_password)
        status_label.config(text=message)
        if update:
            status_label.config(text="Password Updated Successfully 💀")
        else:
            status_label.config(text=message) 

        top.after(1500, top.destroy)


    def go_back_button_clicked(self):
        self.exit_app()

    def exit_app(self):
        self.root.destroy()
        pygame.mixer.quit()       

    def help_button_clicked(self):
        self.play_sound('sounds\\huh.mp3')
        
    def enrol_into_subject_clicked(self):
        self.play_sound('sounds\\mouse_sound.mp3')
        self.enrol_into_subject()

    def change_password_clicked(self):
        self.play_sound('sounds\\nintendo-game-boy-startup.mp3')
        self.change_password()  
        
    def remove_subject_clicked(self):
        self.play_sound('sounds\\nintendo-game-boy-startup.mp3')
        self.remove_subject()

    def show_enrollment_clicked(self):
        self.play_sound('sounds\\mouse_sound.mp3')
        self.show_enrollment()
    
        

    def play_sound(self, sound_file):
        try:
            sound = pygame.mixer.Sound(sound_file)
            if not sound.get_num_channels():  
                sound.play()
        except Exception as e:
            print(f"Error playing sound: {e}")
    


    def main(self):
        self.root.title("Student Menu 📚")
        self.root.mainloop()
    

