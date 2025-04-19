from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import numpy as np
import os
import cv2

class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Training Dataset")

        # Background image
        img_bg = Image.open(r"C:\Users\surya\.vscode\Face recognition IOC\Images_GUI\banner.jpg")
        img_bg = img_bg.resize((1366,830), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img_bg)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1366, height=830)
        
        # Title Label
        title_lbl = Label(
            bg_img,
            text="Train Data Set",
            font=("times new roman", 35, "bold"),
            bg="#1a1a1a",
            fg="white",
        )
        title_lbl.place(x=0, y=0, width=1366, height=60)

        # Training button 1
        std_img_btn=Image.open(r"C:\Users\surya\Python-FYP-Face-Recognition-Attendence-System-master\Images_GUI\t_btn1.png")
        std_img_btn=std_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.train_classifier,image=self.std_img1,cursor="hand2")
        std_b1.place(x=600,y=270,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.train_classifier,text="Train Dataset",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=600,y=450,width=180,height=45)

    # ==================Create Function of Traing===================
    def train_classifier(self):
        data_dir=("Images")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # conver in gray scale 
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)
        
        #=================Train Classifier=============
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classfr.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset Complated!",parent=self.root)







if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()
    