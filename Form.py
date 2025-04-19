from tkinter import *
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import mysql.connector
import cv2
import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Table, TableStyle, Paragraph

class form:
    def __init__(self, root):
        self.root = root
        self.root.geometry("810x760+0+0")
        self.root.title("Form Pannel")

        # ========== Variables ===========
        self.var_date = StringVar()  # Variable for date
        self.var_contractor = StringVar()  # Variable for contractor
        self.var_location = StringVar()  # Variable for location
        self.var_workers = StringVar()  # Variable for number of workers
        self.var_remarks = StringVar()  # Variable for remarks, suggestions, or complaints
        self.var_start_time_hour = StringVar()  # Variable for start time hour
        self.var_start_time_min = StringVar()  # Variable for start time minute
        self.var_end_time_hour = StringVar()  # Variable for end time hour
        self.var_end_time_min = StringVar()  # Variable for end time minute
        self.csv_data = None  # Variable to store CSV data

        # Background image
        img_bg = Image.open(r"Interface_images\background")
        img_bg = img_bg.resize((810, 760), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img_bg)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=810, height=760)
        
        # Title Label
        title_lbl = Label(
            bg_img,
            text="ToolBox Talk Form",
            font=("times new roman", 35, "bold"),
            bg="#1a1a1a",
            fg="white",
        )
        title_lbl.place(x=0, y=0, width=810, height=60)
        
        # Frame
        main_frame = Frame(bg_img, bd=2, bg="#222222")
        main_frame.place(x=0, y=61, width=995, height=800)

        # Tool box Label Frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="#333333", relief=RIDGE, text="Tool Box Talk", font=("times new roman", 15, "bold"), fg="white")
        Left_frame.place(x=6, y=10, width=790, height=680)
        
        # Frame image
        img_Left = Image.open(r"C:\Users\surya\.vscode\Face recognition IOC\Interface_images\student.jpg")
        img_Left = img_Left.resize((970,130),Image.Resampling.LANCZOS)
        self.photoimg_Left = ImageTk.PhotoImage(img_Left)
        
        f_lbl = Label(Left_frame, image=self.photoimg_Left)
        f_lbl.place(x=3, y=0, width=780, height=130)
        
        # Form Label Frame
        form_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, font=("times new roman", 15, "bold"))
        form_frame.place(x=3, y=135, width=780, height=510)
        
        # Date Label
        Date_label = Label(form_frame, text="Date:", font=("times new roman", 15, "bold"), bg="white")
        Date_label.place(x=10, y=20)  # Position at (x=10, y=20)

        # Date Entry
        Date_entry = DateEntry(form_frame, selectmode='day', width=18, font=("times new roman", 15, "bold"), textvariable=self.var_date)
        Date_entry.place(x=130, y=20)  # Position at (x=100, y=20)

        # Contractor Label
        Contractor_label = Label(form_frame, text="Contractor:", font=("times new roman", 15, "bold"), bg="white")
        Contractor_label.place(x=10, y=70)  # Position at (x=10, y=70)

        # Contractor Entry
        Contractor_entry = ttk.Entry(form_frame, width=20, font=("times new roman", 15, "bold"), textvariable=self.var_contractor)
        Contractor_entry.place(x=130, y=70)  # Position at (x=100, y=70)
        
        # Location Label
        Location_label = Label(form_frame, text="Location:", font=("times new roman",  15, "bold"), bg="white")
        Location_label.place(x=10, y=120)  # Position at (x=300, y=20)

        # Location Entry
        Location_entry = ttk.Entry(form_frame, width=20, font=("times new roman", 15, "bold"), textvariable=self.var_location)
        Location_entry.place(x=130, y=120)  # Position at (x=400, y=20)
        
        # Time Label
        time_label = Label(form_frame, text="Time:", font=("times new roman", 15, "bold"), bg="white")
        time_label.place(x=10, y=170)  # Position at (x=300, y=70)

        # Start Time Spinboxes
        start_hour_sb = Spinbox(form_frame, from_=0, to=23, wrap=True, textvariable=self.var_start_time_hour, width=2, font=("times new roman", 15, "bold"), justify=CENTER)
        start_hour_sb.place(x=130, y=170)

        start_min_sb = Spinbox(form_frame, from_=0, to=59, wrap=True, textvariable=self.var_start_time_min, width=2, font=("times new roman", 15, "bold"), justify=CENTER)
        start_min_sb.place(x=170, y=170)

        # "to" Label
        to_label = Label(form_frame, text="to", font=("times new roman", 15, "bold"), bg="white")
        to_label.place(x=220, y=170)  # Position at (x=480, y=70)

        # End Time Spinboxes
        end_hour_sb = Spinbox(form_frame, from_=0, to=23, wrap=True, textvariable=self.var_end_time_hour, width=2, font=("times new roman", 15, "bold"), justify=CENTER)
        end_hour_sb.place(x=260, y=170)

        end_min_sb = Spinbox(form_frame, from_=0, to=59, wrap=True, textvariable=self.var_end_time_min, width=2, font=("times new roman", 15, "bold"), justify=CENTER)
        end_min_sb.place(x=300, y=170)
        
        # Remarks Label
        Remarks_label = Label(form_frame, text="Remarks/suggestion/complaints (if any):", font=("times new roman", 15, "bold"), bg="white")
        Remarks_label.place(x=400, y=20)  # Position at (x=10, y=70)
        
        # Remarks Entry 
        Remarks_entry = Text(form_frame, height=3, width=35, font=("times new roman", 15, "bold"), bg="#F5F5F5", relief="ridge", borderwidth=2)
        Remarks_entry.place(x=400, y=55)  # Position at (x=100, y=70)

        # Worker Label
        Worker_label = Label(form_frame,text="Number of Workers:", font=("times new roman", 15, "bold"), bg="white")
        Worker_label.place(x=400, y=140)  # Position at (x=10, y=70)

        # Worker Entry
        Worker_entry = ttk.Entry(form_frame, textvariable=self.var_workers, width=20, font=("times new roman", 15, "bold"))
        Worker_entry.place(x=400, y=170)  # Position at (x=100, y=70)

        # Next frame
        Point_frame = LabelFrame(form_frame, bd=2, bg="white", relief=RIDGE, font=("times new roman", 15, "bold"))
        Point_frame.place(x=3, y=220, width=770, height=280)
        
        # Discussion Label
        Diss = Label(Point_frame, text="Common point to be Discussed", font=("times new roman", 15, "bold"), bg="white", fg="#5E2612")
        Diss.place(x=10, y=10)
        
        # Status Label
        Status = Label(Point_frame, text="Status ", font=("times new roman", 15, "bold"), bg="white", fg="#5E2612")
        Status.place(x=400, y=10)
        
        # Bullet points and Check buttons
        bullet_points = [
            "Use of proper PPEs & tools",
            "Emergency vehicle & First Aid Box",
            "Enquiry of health status",
            "Work permit status"
        ]

        # Variables for Checkbuttons
        self.check_vars = [IntVar() for _ in range(len(bullet_points))]

        # Place bullet points and check buttons in tabular form
        for i, point in enumerate(bullet_points):
            # Bullet point label
            bullet_label = Label(Point_frame, text=f"• {point}", font=("times new roman", 14), bg="white", anchor="w")
            bullet_label.place(x=20, y=50 + i * 30)  # Adjust y-coordinate for spacing

            # Check button for status
            check_button = Checkbutton(Point_frame, variable=self.check_vars[i], bg="white")
            check_button.place(x=400, y=50 + i * 30)  # Align with the Status label

        # "Discussed Topic of the Day" Label
        Discussed_topic_label = Label(Point_frame, text="Discussed Topic of the Day", font=("times new roman", 15, "bold"), bg="white", fg="#5E2612")
        Discussed_topic_label.place(x=500, y=10)  # Position to the right of the Status Label

        # Text Entry Box for "Discussed Topic of the Day"
        self.var_discussed_topic = StringVar()  # Variable to store the discussed topic
        self.Discussed_topic_entry = Text(Point_frame, height=5, width=25, font=("times new roman", 15, "bold"), bg="#F5F5F5", relief="ridge", borderwidth=2)
        self.Discussed_topic_entry.place(x=500, y=40)

        # Add a Label to display the CSV import status
        self.csv_import_status = Label(Point_frame, text="No CSV file imported", font=("times new roman", 12, "bold"),fg="red")
        self.csv_import_status.place(x=150, y=180, width=400, height=30)

        # Button to import CSV
        import_button = Button(Point_frame, text="Import CSV", command=self.import_csv, font=("times new roman", 15, "bold"), bg="#4CAF50", fg="white")
        import_button.place(x=180, y=220, width=150, height=40)

        # Button to generate PDF
        pdf_button = Button(Point_frame, text="Generate PDF", command=self.generate_pdf, font=("times new roman", 15, "bold"), bg="#2196F3", fg="white")
        pdf_button.place(x=370, y=220, width=150, height=40)

    def import_csv(self):
        """Function to import CSV file and store data."""
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            try:
                self.csv_data = pd.read_csv(file_path, header=None)  # Read CSV without headers
                self.var_workers.set(len(self.csv_data))  # Update var_workers with the number of records
                self.csv_import_status.config(text="CSV file imported successfully", bg="green")
                messagebox.showinfo("Success", "CSV file imported successfully!")
            except Exception as e:
                self.csv_import_status.config(text="Failed to import CSV file")
                messagebox.showerror("Error", f"Failed to import CSV file: {e}")

    def generate_pdf(self):
        """Function to generate PDF with form data and CSV data."""
        pdf_file_path = "attendance_report.pdf"
        c = canvas.Canvas(pdf_file_path, pagesize=A4)  # Use A4 size
        width, height = A4  # Set width and height to A4 dimensions

        # Title
        c.setFont("Helvetica-Bold", 20)
        c.drawCentredString(width / 2, height - 50, "Tool Box/Hira Talk")

        c.setFont("Helvetica", 12)
        c.drawString(100, height - 100, "Date ".ljust(62) + f":    {self.var_date.get()}")
        c.drawString(100, height - 120, "Name of the Contractor ".ljust(50) + f":    {self.var_contractor.get()}")
        c.drawString(100, height - 140, "Location ".ljust(60) + f":    {self.var_location.get()}")
        c.drawString(100, height - 160, "Time ".ljust(61) + f":    {self.var_start_time_hour.get()}:{self.var_start_time_min.get()} - {self.var_end_time_hour.get()}:{self.var_end_time_min.get()}")
        c.drawString(100, height - 180, "Number of Workerman present ".ljust(43) + f":    {self.var_workers.get()}")
        c.drawString(100, height - 200, "Remarks/suggestion/complaints (if any) ".ljust(41) + f":    {self.var_remarks.get()}")

        # Common point to be Discussed section
        c.setFont("Helvetica-Bold", 14)

        # Prepare data for the table
        bullet_points = [
            "Use of proper PPEs & tools",
            "Emergency vehicle & First Aid Box",
            "Enquiry of health status",
            "Work permit status"
        ]
        data = [["Point to be Discussed", "Status", "Discussed Topic of the Day"]]  # Table headers
        for i, point in enumerate(bullet_points):
            status = "Yes" if self.check_vars[i].get() else "No"
            if i == 0:
                text = self.Discussed_topic_entry.get("1.0", "end-1c")
                styles = getSampleStyleSheet()
                style = styles["BodyText"]
                style.fontSize = 14  # Increase font size
                style.alignment = 1  # Center align text
                style.leading = 20  # Increase line spacing
                para = Paragraph(text, style)  # Create a paragraph for the discussed topic
                data.append([point, status, para])  # Use the paragraph for the first row
            else:
                data.append([point, status, ""])  # Use empty strings for the remaining rows

        # Create the table
        table = Table(data, colWidths=[200, 50, 180])  # Increase the width of the content cell
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.white),  # Header background
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),  # Header text color
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center align all cells
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Header font
            ('FONTSIZE', (0, 0), (-1, -1), 12),  # Font size for all cells
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Header padding
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),  # Table body background
            ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Grid lines
            ('VALIGN', (0, 1), (-1, -1), 'TOP'),  # Align content to top
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white]),  # Set background color for rows
            ('SPAN', (2, 1), (2, -1)),  # Span the content cell across all rows
            ('ALIGN', (2, 1), (2, -1), 'LEFT'),  # Left align the content cell
            ('LEFTPADDING', (2, 1), (2, -1), 20),  # Set left padding to 0
            ('RIGHTPADDING', (2, 1), (2, -1), 20),  # Set right padding to 0
            ('TOPPADDING', (2, 1), (2, -1), 5),  # Add padding to the top side of the content cell
            ('BOTTOMPADDING', (2, 1), (2, -1), 5),  # Add padding to the bottom side of the content cell
            ('ROWHEIGHTS', (0, 0), (-1, -1), (50,)),  # Increase the height of the content cell
        ]))

        # Draw the table on the PDF
        table.wrapOn(c, width, height)
        table.drawOn(c, 100, height - 320)  # Adjust y-coordinate for proper positioning
        
        # CSV Data
        if self.csv_data is not None:
            # Add headers manually
            headers = ["Sr. No.", "Name", "Designation", "Attendance"]
            data = [headers] + [[i + 1] + [row[0].upper()] + row[1:].tolist() for i, row in enumerate(self.csv_data.values)]
            table = Table(data, colWidths=[50, 150, 100, 130])
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ]))
            table.wrapOn(c, 100, height - 380)
            table.drawOn(c, 100, height - 380)

        c.save()
        messagebox.showinfo("Success", f"PDF generated successfully: {pdf_file_path}")

if __name__ == "__main__":
    root = Tk()
    obj = form(root)
    root.mainloop()