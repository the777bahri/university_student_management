import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pygame
from datetime import datetime
import random
from University_UI_Updated import University
from Admin_GUI import AdminApp
from Student_Login_GUI import Student_LoginApp

class UniApp:
    def __init__(self, root):
        self.root = root
        self.university = University()
        self.root.title("University APP GUI")
        self.image_paths = {
            "logo": "images\\UTS-300x300.png",
            "background": "images\\UTS building 11.jpg",
            "3d" : "images\\kitty.png"
        }
        pygame.mixer.init()
        self.initialize_ui()

    def initialize_ui(self):
        self.check_if_png()
        self.load_images()
        self.setup_ui()
        self.play_startup_sound()
        self.setup_moving_image()
        self.animate()
        self.clock()
        self.admin_app = None  
        self.student_login_app = None


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


    def clock(self):
        time= datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
        self.canvas.itemconfig(self.time_text, text=f"Day and Time: {time}")
        self.root.after(1000, self.clock)


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

    def image_clicked(self, event):
        self.play_sound('sounds\kitty1.mp3')
        text_id = self.canvas.create_text(400, 50, text="leave me alone 🥺😽!", fill="pink", font=('Times New Roman', 22, 'bold'))
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
            background_image = background_image.resize((self.bg_width, self.bg_height), Image.Resampling.LANCZOS)
            self.background_image = ImageTk.PhotoImage(background_image)

            logo_image = Image.open(self.image_paths["logo"])
            logo_image = logo_image.resize((100, 100), Image.Resampling.LANCZOS)
            self.logo_image = ImageTk.PhotoImage(logo_image)
        except Exception as e:
            print(f"Error loading or processing image files: {e}")

    def setup_ui(self):
        self.canvas = tk.Canvas(self.root, width=self.bg_width, height=self.bg_height)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.background_image, anchor="nw")
        self.canvas.create_image(self.bg_width/10, self.bg_height/10, image=self.logo_image, anchor="center")
        self.time_text = self.canvas.create_text(150, 10, text="", fill="white", font=('Helvetica', 12))
        self.create_buttons()

    def play_startup_sound(self):
        self.play_sound('sounds\mong us.mp3') 
            

    def create_buttons(self):
        exit_button = tk.Button(self.root, text="Exit", command=self.exit_button_clicked)
        help_button = tk.Button(self.root, text="Help", command= self.help_button_clicked)
        student_button = tk.Button(self.root, text="Student", command=self.student_button_clicked)
        admin_button = tk.Button(self.root, text="Admin", command= self.admin_button_clicked)

        self.canvas.create_window(self.bg_height/2, self.bg_width/1.7, anchor="nw", window=exit_button)
        self.canvas.create_window(self.bg_height/4, self.bg_width/5, anchor="nw", window=student_button)
        self.canvas.create_window(self.bg_height/10, self.bg_width/5, anchor="nw", window=admin_button)
        self.canvas.create_window(self.bg_height/6, self.bg_width/8.3, anchor="nw", window=help_button)

    def exit_button_clicked(self):
        print("Exit button clicked.")
        if not pygame.mixer.get_init():
            pygame.mixer.init()
        self.play_sound('sounds\\closing.mp3')
        self.root.after(2500, self.exit_app)  

    def exit_app(self):
        print("Exiting app.")
        pygame.mixer.quit()
        self.root.destroy()        


    def help_button_clicked(self):
        self.play_sound('sounds\\huh.mp3')

    def student_button_clicked(self):
        self.play_sound('sounds\\mouse_sound.mp3')
        if self.student_login_app is None or not self.student_login_app.root.winfo_exists():
            self.student_login_app = Student_LoginApp(self.root) 
        else:
            self.student_login_app.show_window()  

    def admin_button_clicked(self):
        self.play_sound('sounds\\nintendo-game-boy-startup.mp3')
        if self.admin_app is None or not self.admin_app.root.winfo_exists():
            self.admin_app = AdminApp(self.root)  
        else:
            self.admin_app.show_window()  

    def play_sound(self, sound_file):
        if not pygame.mixer.get_init():
            pygame.mixer.init()
        try:
            sound = pygame.mixer.Sound(sound_file)
            sound.play()
        except Exception as e:
            print(f"Error playing sound: {e}")

    
if __name__ == "__main__":
    root = tk.Tk()
    app = UniApp(root)
    root.mainloop()
