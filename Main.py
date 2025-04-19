from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from Employee import employee  # File name is Prototype_student.py and class name is Student
from Face_recognition import Face_Recognition
from Train import Train
from Attendance import Attendance
from Developer import Developer
import os

class Face_recognition_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x830+0+0")
        self.root.title("Face Recognition Attendance Monitoring System")

        # Background image
        img_bg = Image.open(r"C:\Users\surya\.vscode\Face recognition IOC\Interface_images\Refinery.webp")
        img_bg = img_bg.resize((1550, 830), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img_bg)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1550, height=830)
        
        img = Image.open(r"C:\Users\surya\.vscode\Face recognition IOC\Interface_images\OIP (1).jpeg")
        img = img.resize((400,250),Image.Resampling.LANCZOS)
        self.photoimgl = ImageTk.PhotoImage(img)
        
        f_lbl = Label(self.root, image=self.photoimgl)
        f_lbl.place(x = 1120,y = 70, width = 400, height = 250)

        # Title Label
        title_lbl = Label(
            bg_img,
            text="Attendance Monitoring System for Toolbox Talk",
            font=("times new roman", 35, "bold"),
            bg="#1a1a1a",
            fg="white",
        )
        title_lbl.place(x=0, y=0, width=1550, height=60)

        # Button Styles
        button_bg = "#333333"  # Dark gray background
        button_hover_bg = "#555555"  # Lighter gray for hover
        button_fg = "white"  # White text

        # Reusable method to create buttons with hover effect
        def create_button(text, x, y, command=None):
            button = Button(
                bg_img,
                text=text,
                cursor="hand2",
                font=("times new roman", 15, "bold"),
                bg=button_bg,
                fg=button_fg,
                activebackground=button_hover_bg,
                activeforeground=button_fg,
                command=command  # Set the command here
            )
            button.place(x=x, y=y, width=220, height=40)

            # Bind hover events to the button
            button.bind("<Enter>", lambda e: on_enter(button))
            button.bind("<Leave>", lambda e: on_leave(button))

        # Hover effect methods
        def on_enter(button):
            button.config(bg="#555555")  # Change background color on hover

        def on_leave(button):
            button.config(bg="#333333")  # Revert background color when mouse leaves

        # Buttons
        create_button("Employee Details", 100, 170, command=self.employee_details)
        create_button("Face Detection", 100, 270, command=self.face_detection)
        create_button("Attendance", 100, 370, command=self.attendance)
        create_button("Train Data", 100, 470, command=self.train_data)
        create_button("Photos", 100, 570, command=self.open_img)
        create_button("Exit", 100, 670)

        def on_text_enter(label):
            label.config(fg="yellow")  # Change text color on hover

        def on_text_leave(label):
            label.config(fg="cyan")  # Revert text color when mouse leaves

        # Developer Label
        developer_label = Label(
            bg_img,
            text="Developer",
            font=("Arial", 12, "bold"),
            fg="cyan",
            bg="#1a1a1a",
            cursor="hand2"
        )
        developer_label.place(x=1400, y=750)  # Position at bottom right
        developer_label.bind("<Enter>", lambda e: on_text_enter(developer_label))
        developer_label.bind("<Leave>", lambda e: on_text_leave(developer_label))
        developer_label.bind("<Button-1>", lambda e: self.developer())
        # # Developer Label
        # developer_label = Label(
        #     bg_img,
        #     text="Developer",
        #     font=("Arial", 12, "bold"),
        #     fg="cyan",
        #     bg="#1a1a1a",
        #     cursor="hand2"
        # )
        # developer_label.place(x=1300, y=750)  # Position at bottom right
        # developer_label.bind("<Enter>", lambda e: on_text_enter(developer_label))
        # developer_label.bind("<Leave>", lambda e: on_text_leave(developer_label))

    def open_img(self):
        os.startfile("Images")
    
    def employee_details(self):
        self.new_window = Toplevel(self.root)
        self.app = employee(self.new_window)
        
    def face_detection(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)
        
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
    
    def attendance(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)
    
    def developer(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition_system(root)
    root.mainloop()