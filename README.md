
# 👨‍💼 Attendance Management Using Face Recognition

This project is a simple and efficient attendance system that uses real-time face recognition to mark attendance. Designed using Python with a Tkinter-based GUI, OpenCV for facial detection, and MySQL for backend storage. Built during my internship at Indian Oil Corporation, Gujarat Refinery.




## 🧰 Tech Stack

| Technology       | Purpose/Use                                 | Official/Trusted Link |
|------------------|----------------------------------------------|------------------------|
| **Python**        | Core programming language                   | [python.org](https://www.python.org/) |
| **OpenCV**        | Face detection and recognition              | [opencv.org](https://opencv.org/) / [PyPI: opencv-python](https://pypi.org/project/opencv-python/) |
| **Tkinter**       | GUI (Graphical User Interface)              | [Tkinter Docs (Python)](https://docs.python.org/3/library/tkinter.html) |
| **MySQL**         | Backend database for storing attendance     | [MySQL Official Site](https://www.mysql.com/) / [MySQL Connector for Python](https://dev.mysql.com/doc/connector-python/en/) |
| **PIL (Pillow)**  | Image preprocessing and manipulation         | [pillow.readthedocs.io](https://pillow.readthedocs.io/en/stable/) |
| **ReportLab**     | Generating attendance reports in PDF format | [reportlab.com](https://www.reportlab.com/documentation/) |

## ⚙️ How to Use
Follow these steps to get the project up and running:

### 1. Install Required Libraries
Make sure you have Python 3 installed.
- To install `pillow`:
    ```bash
    pip install pillow
    ```
- To install `mysql-connector-python`:
    ```bash
    pip install mysql-connector-python
    ```
- To install `opencv-python`:
    ```bash
    pip install opencv-python
    ```
- To install `reportlab`:
    ```bash
    pip install reportlab
    ```

### 2. Set Up the Database
- Open **MySQL** or **MySQL Workbench**
- Create a new database (e.g., `attendance_system`)
- Inside it, create the necessary tables like `employee`, `attendance`, `loginRegister`, etc.
- Make sure your table and field names match those used in the code

### 3. Update Paths and Database Config

- 📌 **NOTE:** 
    - Don’t forget to change the **image paths** in the code to match your local system (especially for saving/loading face images)
    - Make sure to delete `classfr.xml` before training the data images(file will generate/rewrite automatically on every train execution)
    Otherwise, things won’t work as expected!
  
- 🛠️ Also make sure to update your **database settings** in the file:
  - Change the **database name**
  - Update your **MySQL username and password**
  - Ensure the **host** (usually `localhost`) is correct
  - Double-check that the **table names** and **field names** used in your MySQL database match what's in the code

### 4. Run the App
```bash
python main.py
```


## 📸 Snapshots

No worries — you can find all screenshots and interface visuals in the `Report.pdf` available in this repository or You can view all interface screenshots and project details in the link:

👉 [**Project Report: Attendance Management Using Face Recognition**](https://github.com/RyoHaradaps/Attendance-Management-Using-Face-Recognition/blob/33bfdfa2ee01b8c7df5ce9e99392430339f55a88/Report.pdf)

It includes:
- Login/Registration Screens
- Employee Management Window
- Face Recognition Panel
- Real-time Attendance Logs
- Report Generation Interface (PDF/CSV)
- References

Feel free to check it out for a complete visual walkthrough!
## 🤔 What to Watch Out on Work

- Ensure your webcam is working

- Keep lighting consistent for better accuracy

- Use grayscale, resized face images (200x200 px recommended)

- Proxy attendance? Not anymore! 😉

## 📌 Future Improvements

- Can Exact the code into `.exe` file format

- Add CNN-based deep learning for higher recognition accuracy

- Mobile version for remote attendance logging

- Integration with gate pass or HR systems

- Better UI styling with modern frameworks (e.g., PyQt or web-based frontend)

## 📄 License
Open-source for educational and research use. Give credit if reused or forked.
Built with ❤️