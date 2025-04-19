from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import numpy as np
import os
import cv2

class Help:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1550x830+0+0")
        self.root.title("Face Recognition System")
    
    
    
    
    
    
if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()