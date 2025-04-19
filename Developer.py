from tkinter import *
from PIL import Image, ImageTk
import webbrowser

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x800+0+0")  # Adjusted window size
        self.root.title("Developer Information")
    
        # Set background color to Pinetar (a shade of green)
        self.canvas = Canvas(self.root, width=1200, height=900, bg="#EECFA1")  # Pinetar color
        self.canvas.pack()
        
        # Add Developer Information heading with rounded rectangle
        self.round_rectangle(300, 0, 900, 60, radius=20, fill="#308014", outline="#EECFA1", width=2)
        
        # Add Developer Information to the Canvas
        self.canvas.create_text(
            600, 30,  # Position of the title (center top)
            text="Developer Information",
            font=("times new roman", 35, "bold"),
            fill="whitesmoke",  # Dark gray text color for better contrast
            anchor=CENTER,  # Center the text
        )

        # Add Headings
        self.canvas.create_text(50, 95, text="Personal Details", font=("times new roman", 25, "bold"), fill="#5E2612", anchor=NW)  # White text
        self.canvas.create_text(50, 180, text="Contact Information", font=("times new roman", 25, "bold"), fill="#5E2612", anchor=NW)  # White text
        self.canvas.create_text(50, 305, text="Skills & Expertise", font=("times new roman", 25, "bold"), fill="#5E2612", anchor=NW)  # White text
        self.canvas.create_text(50, 410, text="About Me", font=("times new roman", 25, "bold"), fill="#5E2612", anchor=NW)  # White text
        self.canvas.create_text(50, 492, text="Projects", font=("times new roman", 25, "bold"), fill="#5E2612", anchor=NW)  # White text

        # Developer Details
        developer_info = """
    Name: P S Suryanarayanan
    Role: Python Developer


    Email: 
    Phone: 
    LinkedIn: 
    GitHub: 


    Programming Languages: Python, C, SQL
    Technologies/Frameworks: GitHub, Google Colab
    Developer Tools: VS Code


    Experienced Python Developer with a strong background in machine learning and database management. Passionate about leveraging advanced technologies to develop solutions for real-world problems, particularly in medical image analysis and system management.


    'Advanced Imaging for Tumor Detection and Prognosis'
        Developed using Python and Google Colab, leveraging Convolutional Neural Networks (CNN) to enhance accuracy in tumor identification.
        Utilized deep learning techniques to train models on a comprehensive dataset, improving detection and classification precision.
        Expertise in medical image analysis, dataset preprocessing, and model optimization.

    'Salon Management'
        Developed using Python and MySQL, implementing efficient database connectivity for record management.
        Designed and maintained a database for storing customer details, payment methods, and billing records.
        Streamlined CRUD operations to improve customer data handling and operational efficiency.
        """

        # Add Developer Details to the Canvas
        self.text_id = self.canvas.create_text(
            50, 110,  # Position of the text (top-left)
            text=developer_info,
            font=("times new roman", 14),
            fill="#8B6508",  # White text color
            anchor=NW,  # Align text to the top-left
            width=1100,  # Set a width to wrap the text within the canvas
        )

        # Make email, phone, LinkedIn, and GitHub clickable
        self.make_clickable("suryanarayanan2005@gmail.com", "mailto:suryanarayanan2005@gmail.com", 125, 214)
        self.make_clickable("+91-9023607811", "tel:+91-9023607811", 131, 235)
        self.make_clickable("linkedin.com/in/pssuryanarayanan", "www.linkedin.com/in/p-s-suryanarayanan", 150 , 257)
        self.make_clickable("github.com/RyoHaradaps", "https://github.com/RyoHaradaps", 140, 278)

        # Load and display the profile image
        self.load_profile_image("C:\\Users\\surya\\.vscode\\Face recognition IOC\\Interface_images\\Devp.jpg")

    def make_clickable(self, text, link, x, y):
        """
        Makes specific text in the Canvas clickable.
        """
        # Create a text item for the clickable link
        text_id = self.canvas.create_text(
            x, y,  # Position of the text
            text=text,
            font=("times new roman", 14),
            fill="#A0522D",  # Light blue text color for links
            anchor=NW,  # Align text to the top-left
        )

        # Bind the text item to open the link when clicked
        self.canvas.tag_bind(text_id, "<Button-1>", lambda e: webbrowser.open(link))

    def load_profile_image(self, path):
        """
        Loads and displays the profile image on the right side of the canvas.
        """
        img = Image.open(path)
        img = img.resize((250, 250), Image.Resampling.LANCZOS)  # Resize image to fit
        self.photoimg = ImageTk.PhotoImage(img)

        # Create a rectangle behind the profile image
        self.canvas.create_rectangle(
            690, 110, 960, 380,  # Position and size of the rectangle (x1, y1, x2, y2)
            fill="#5E2612",  # Light background for the rectangle
            outline="#5E2612",  # Same color border
            width=2,  # Border thickness
        )

        # Add the image to the canvas
        self.canvas.create_image(700, 120, image=self.photoimg, anchor=NW)  # Position the image

    def round_rectangle(self, x1, y1, x2, y2, radius=25, **kwargs):
        points = [x1+radius, y1,
                  x1+radius, y1,
                  x2-radius, y1,
                  x2-radius, y1,
                  x2, y1,
                  x2, y1+radius,
                  x2, y1+radius,
                  x2, y2-radius,
                  x2, y2-radius,
                  x2, y2,
                  x2-radius, y2,
                  x2-radius, y2,
                  x1+radius, y2,
                  x1+radius, y2,
                  x1, y2,
                  x1, y2-radius,
                  x1, y2-radius,
                  x1, y1+radius,
                  x1, y1+radius,
                  x1, y1]

        return self.canvas.create_polygon(points, **kwargs, smooth=True)

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()