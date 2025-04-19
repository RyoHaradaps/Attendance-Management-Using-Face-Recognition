from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class employee:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x580+0+0")
        self.root.title("Employee")

        # ========== Variables ===========
        self.var_dept=StringVar() # Add at every Combobox or Label, Example (textvariable=self.var_dept)
        self.var_epid=StringVar()
        self.var_emp_name=StringVar()
        self.var_desig=StringVar()
        self.var_radio=StringVar()
        
        # Background image
        img_bg = Image.open(r"Interface_images\background")
        img_bg = img_bg.resize((1550, 830), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img_bg)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1550, height=830)
        
        # Title Label
        title_lbl = Label(
            bg_img,
            text="Employee Management System",
            font=("times new roman", 35, "bold"),
            bg="#1a1a1a",
            fg="white",
        )
        title_lbl.place(x=0, y=0, width=1550, height=60)
        
        # Frame
        main_frame = Frame(bg_img, bd=2, bg="#222222")
        main_frame.place(x=0, y=61, width=1550, height=525)

        # Left Label Frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="#333333", relief=RIDGE, text="Employee Details", font=("times new roman", 15, "bold"), fg="white")
        Left_frame.place(x=8, y=10, width=775, height=500)
        
        # Left Frame image
        img_Left = Image.open(r"C:\Users\surya\.vscode\Face recognition IOC\Interface_images\worker.jpg")
        img_Left = img_Left.resize((965,330),Image.Resampling.LANCZOS)
        self.photoimg_Left = ImageTk.PhotoImage(img_Left)
        
        f_lbl = Label(Left_frame, image=self.photoimg_Left)
        f_lbl.place(x = 3,y = 0, width = 765, height = 130)
        
        
        # Left Class Student Information Label Frame
        Company_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, font=("times new roman", 15, "bold"))
        Company_frame.place(x=5, y=135, width=765, height=330)
        
        # EmpID Label
        EmpId_label = Label(Company_frame, text="Pass no/Emp Id:",  font=("times new roman", 15, "bold"), bg="white")
        EmpId_label.grid(row=0, column=0, padx=(10, 0), pady=(20, 0), sticky=W)  # Increased vertical padding
        
        EmpId_entry = ttk.Entry(Company_frame, textvariable=self.var_epid, width=20, font=("times new roman", 15, "bold"))
        EmpId_entry.grid(row=0, column=1, padx=(10, 0), pady=(20, 0), sticky=W)  # Increased vertical padding
        
        # Employee name Label
        Emp_Name_label = Label(Company_frame, text="Name:", font=("times new roman", 15, "bold"), bg="white")
        Emp_Name_label.grid(row=0, column=2, padx=(10, 0), pady=(20, 0), sticky=W)  # Increased vertical padding
        
        Emp_Name_entry = ttk.Entry(Company_frame, textvariable=self.var_emp_name, width=20, font=("times new roman", 15, "bold"))
        Emp_Name_entry.grid(row=0, column=3, padx=(10, 0), pady=(20, 0), sticky=W)  # Increased vertical padding
        
        # Department Label
        Dept_label = Label(Company_frame, text="Department:", font=("times new roman", 15, "bold"), bg="white")
        Dept_label.grid(row=1, column=0, padx=(10, 0), pady=(30, 0), sticky=W)  # Increased vertical padding
        
        Dept_combo = ttk.Combobox(Company_frame, textvariable=self.var_dept, font=("times new roman", 14, "bold"), width=18, state="readonly")
        Dept_combo["values"] = ("Select Department", "Contracts", "Corp. Comm.", "ED/CGM/GM Sectt", "Engg Services", "Finance", "Fire & Safety", "HSE", "Human Resource", "Info. Systems", "Inspection", "Instrumentation", "Maint Mech", "Maint-Civil", "Maint-Elect", "Materials", "Medical", "P&U", "Production", "Projects", "Quality Control", "TPM", "Techn. Services", "Vigilance")
        Dept_combo.current(0)
        Dept_combo.grid(row=1, column=1, padx=(11, 0), pady=(30, 0), sticky=W)
        
        # Desig Label
        Desig = Label(Company_frame, text="Designation:", font=("times new roman", 15, "bold"), bg="white")
        Desig.grid(row=1, column=2, padx=(10, 0), pady=(30, 0), sticky=W)  # Increased vertical padding
        
        Desig = ttk.Entry(Company_frame, textvariable=self.var_desig, font=("times new roman", 15, "bold"))
        Desig.grid(row=1, column=3, padx=(10, 0), pady=(30, 0), sticky=W)  # Increased vertical padding
        

        # Create a separate frame for radio buttons
        radio_frame = Frame(Company_frame, bg="white")
        radio_frame.grid(row=5, column=0, columnspan=4, pady=(20, 0))  # Place it below the other fields

        # Creating a style for the radio buttons
        style = ttk.Style()
        style.configure("Custom.TRadiobutton", background="lightblue", foreground="black", font=("times new roman", 15, "bold"))

        # Radio Buttons
        Radiobutton1 = ttk.Radiobutton(radio_frame, variable=self.var_radio, text="Take Photo Sample", value="YES", style="Custom.TRadiobutton")
        Radiobutton1.grid(row=0, column=0, padx=(15, 0), pady=(15, 0))  # Increased vertical padding

        Radiobutton2 = ttk.Radiobutton(radio_frame, variable=self.var_radio, text="Do Not Take Photo Sample", value="NO", style="Custom.TRadiobutton")
        Radiobutton2.grid(row=0, column=1, padx=(15, 0), pady=(15, 0))  # Increased vertical padding
        
        # Button Frame 1
        button_frame1=Frame(Company_frame, bd=2,bg="white", relief=RIDGE)
        button_frame1.place(x=3, y=200, width=755, height=44)
        
        Save_btn = Button(button_frame1, command=self.add_data, text="Save", width=14, font=("times new roman", 15, "bold"), bg="#777777",fg="white")
        Save_btn.grid(row=0, column=0,padx=1,pady=1,sticky=W)
        
        Update_btn = Button(button_frame1, command=self.update_data, text="Update", width=15, font=("times new roman", 15, "bold"), bg="#777777",fg="white")
        Update_btn.grid(row=0, column=1, padx=2,sticky=W)
        
        Delete_btn = Button(button_frame1, command=self.delete_data, text="Delete", width=15, font=("times new roman", 15, "bold"), bg="#777777",fg="white")
        Delete_btn.grid(row=0, column=2, padx=2,sticky=W)
        
        Reset_btn = Button(button_frame1, command=self.reset_data, text="Reset", width=15, font=("times new roman", 15, "bold"), bg="#777777",fg="white")
        Reset_btn.grid(row=0, column=3, padx=1,sticky=W)
        
        # Button Frame 2
        button_frame2=Frame(Company_frame, bd=2,bg="white", relief=RIDGE)
        button_frame2.place(x=3, y=250, width=755, height=44)

        TakePhoto_btn = Button(button_frame2, command=self.generate_dataset, text="Take Photo Sample", width=30, font=("times new roman", 15, "bold"), bg="#999999",fg="white")
        TakePhoto_btn.grid(row=0, column=0)
        
        UpdatePhoto_btn = Button(button_frame2, text="Update Photo Sample ", width=30, font=("times new roman", 15, "bold"), bg="#999999",fg="white")
        UpdatePhoto_btn.grid(row=0, column=1, padx=10)
        
        
        
        # Right Label Frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="#333333", relief=RIDGE, text="Employee Information", font=("times new roman", 15, "bold"), fg="white")
        Right_frame.place(x=790, y=10, width=737, height=500)
        
        img_Right = Image.open(r"C:\Users\surya\.vscode\Face recognition IOC\Interface_images\worker2.jpeg")
        img_Right = img_Right.resize((760,230),Image.Resampling.LANCZOS)
        self.photoimg_Right = ImageTk.PhotoImage(img_Right)
        
        f_lbl = Label(Right_frame, image=self.photoimg_Right)
        f_lbl.place(x = 5,y = 0, width = 722, height = 100)
        
        # =========== Search System ===========
        Search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("times new roman", 15, "bold"))
        Search_frame.place(x=5, y=100, width=722, height=80)
        
        Search_label = Label(Search_frame, text="Search By:", font=("times new roman", 15, "bold"), bg="#FFCCBC", fg="blue")
        Search_label.grid(row=0, column=0, padx=(10, 0), sticky=W)
        self.var_searchTX=StringVar()
        
        Search_combo = ttk.Combobox(Search_frame,textvariable=self.var_searchTX, font=("times new roman", 14, "bold"), width=10, state="readonly")
        Search_combo["values"] = ("Select","Pass no/Emp Id", "Designation")
        Search_combo.current(0)
        Search_combo.grid(row=0, column=1, padx=10, pady=(10, 10), sticky=W)  # Added bottom padding
        
        self.var_search=StringVar()
        Search_label = ttk.Entry(Search_frame,textvariable=self.var_search, font=("times new roman", 15, "bold"))
        Search_label.grid(row=0, column=2, padx=(0, 10), pady=(10, 12), sticky=W)  # Increased vertical padding

        Search_btn = Button(Search_frame,command=self.search_data, text="Search", width=9, font=("times new roman", 15, "bold"), bg="#777777",fg="white")
        Search_btn.grid(row=0, column=3, padx=4)
        
        SaveAll_btn = Button(Search_frame, text="Save All", width=9, font=("times new roman", 15, "bold"), bg="#777777",fg="white")
        SaveAll_btn.grid(row=0, column=4, padx=4)
        
        # =========== Table Frame ===========
        Table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        Table_frame.place(x=5, y=185, width=722, height=280)
        
        scroll_x = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_frame, orient=VERTICAL)
        
        
        self.company_table = ttk.Treeview(Table_frame, columns=("Pass no/Emp Id","Name","Dept","Designation","Photo_sample"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.company_table.xview)
        scroll_y.config(command=self.company_table.yview)

        # =========== Table Column ===========
        self.company_table.heading("Pass no/Emp Id",text="Pass no/Emp Id")
        self.company_table.heading("Name",text="Name")
        self.company_table.heading("Dept",text="Department")
        self.company_table.heading("Designation",text="Designation")
        self.company_table.heading("Photo_sample",text="Photo_sample")
        self.company_table["show"] = "headings"  # Show Headings

        # Set column widths
        self.company_table.column("Pass no/Emp Id",width=100)
        self.company_table.column("Name",width=100)
        self.company_table.column("Dept",width=100)
        self.company_table.column("Designation",width=100)
        self.company_table.column("Photo_sample",width=100)

        self.company_table.pack(fill=BOTH, expand=1)
        self.company_table.bind("<ButtonRelease>",self.get_cursor)  # Fetching cursor
        self.fetch_data() # Fetching Data
        
        
                # ========== Function Declaration For Buttons ==========
    
    # Save Button Function
    def add_data(self):
           if self.var_dept.get()=="Select Department" or self.var_epid.get()=="" or self.var_emp_name.get()=="" or self.var_desig.get()=="" :
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
           else:
                try:
                    conn = mysql.connector.connect(
                            host="localhost",
                            user="root",  
                            password="4125",
                            database="face_recog"
                        )
                    my_cursor = conn.cursor()
                    my_cursor.execute("INSERT INTO company VALUES (%s, %s, %s, %s, %s)",
                            (
                                self.var_epid.get(),
                                self.var_emp_name.get(),
                                self.var_dept.get(),
                                self.var_desig.get(),
                                self.var_radio.get()
                            )
                        )
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success","All Records are Saved!",parent=self.root)
                except Exception as es:
                    messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    
    # ========== Fetch Data for Cursor ==========
    def fetch_data(self):
        conn = mysql.connector.connect(
                            host="localhost",
                            user="root",  
                            password="4125",
                            database="face_recog"
                        )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from company")
        data=my_cursor.fetchall()
        
        if len(data)!=0:
            self.company_table.delete(*self.company_table.get_children())
            for i in data:
                self.company_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    # ============= Get Cursor for Update ==============
    def get_cursor(self, event=""):
        cursor_focus=self.company_table. focus()
        content=self.company_table.item(cursor_focus)
        data=content["values"]

        self.var_epid.set(data[0]),
        self.var_emp_name.set(data[1]),
        self.var_dept.set(data[2]),
        self.var_desig.set(data[3]),
        self.var_radio.set(data[4])
    
    # Update Button function
    def update_data(self):
        if self.var_dept.get()=="Select Department" or self.var_epid.get()=="" or self.var_emp_name.get()=="" or self.var_desig.get()=="" :
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update", "Do you want to Update this Employee details", parent=self.root)
                if Update>0:
                    conn = mysql.connector.connect(
                            host="localhost",
                            user="root",  
                            password="4125",
                            database="face_recog"
                        )
                    my_cursor = conn.cursor()
                    my_cursor.execute("update company set Name=%s,Department=%s,Designation=%s,Photo_sample=%s where Emp_id=%s",
                            (   
                                self.var_emp_name.get(),
                                self.var_dept.get(),
                                self.var_desig.get(),
                                self.var_radio.get(),
                                self.var_epid.get()
                            ))
                    
                else:
                    if not Update:
                        return   
                messagebox.showinfo("Success","Successfully Updated!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    
    # Delete Button function
    def delete_data(self):
        if self.var_epid.get()=="":
            messagebox.showerror("Error", "Employee Id/Pass no is required!", parent=self.root)
        else:
            try:
                Delete=messagebox.askyesno("Delete", "Do you really want to delete this employee details?", parent=self.root)
                if Delete>0:
                    conn = mysql.connector.connect(
                            host="localhost",
                            user="root",  
                            password="4125",
                            database="face_recog"
                        )
                    my_cursor = conn.cursor()
                    my_cursor.execute("delete from company where Emp_id=%s",(self.var_epid.get(),))
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    
    # Reset Button function
    def reset_data(self):
        self.var_epid.set(""),
        self.var_emp_name.set(""),
        self.var_dept.set("Select Department"),
        self.var_desig.set(""),
        self.var_radio.set("")
        
    # ===========================Search Data===================
    def search_data(self):
        if self.var_search.get()=="" or self.var_searchTX.get()=="Select":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='4125',host='localhost',database='face_recog')
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT Emp_id,Name,Department,Designation,Photo_sample FROM company where Emp_id='" +str(self.var_search.get()) + "'" )
                # my_cursor.execute("select * from student where Roll_No= " +str(self.var_search.get())+" "+str(self.var_searchTX.get())+"")
                rows=my_cursor.fetchall()        
                if len(rows)!=0:
                    self.company_table.delete(*self.company_table.get_children())
                    for i in rows:
                        self.company_table.insert("",END,values=i)
                    if rows==None:
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    
    # Generate Dataset Function
    def generate_dataset(self):
        if self.var_dept.get()=="Select Department" or self.var_epid.get()=="" or self.var_emp_name.get()=="" or self.var_desig.get()=="" :
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        elif self.var_radio.get() == "NO":
            messagebox.showwarning("Warning", "Please check the radio button to take a photo sample.", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="4125",
                    database="face_recog"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM company")
                my_result = my_cursor.fetchall()
                id=0
                for x in my_result:
                    id+=1

                my_cursor.execute("update company set Name=%s,Department=%s,Designation=%s,Photo_sample=%s where Emp_id=%s",( 
                    self.var_emp_name.get(),
                    self.var_dept.get(),
                    self.var_desig.get(),
                    self.var_radio.get(),
                    self.var_epid.get()==id+1   
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ====================part of opencv=======================

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_croped(img):
                    # conver gary sacle
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #Scaling factor 1.3
                    # Minimum naber 5
                    for (x,y,w,h) in faces:
                        face_croped=img[y:y+h,x:x+w]
                        return face_croped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_croped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_croped(my_frame),(200,200))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path="Images/employee."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)        
                        cv2.imshow("Capture Images",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root) 

   
if __name__ == "__main__":
    root = Tk()
    obj = employee(root)
    root.mainloop()