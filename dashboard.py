from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import mysql.connector
from tkinter import ttk
import os


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Admin\Desktop\TKinter\Project\Login\assets dashboard\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def swap_to_add():
    window.destroy()
    os.system('python add.py')

def swap_to_delete():
    window.destroy()
    os.system('python delete.py')

def swap_to_login():
    window.destroy()
    os.system('python login.py')

def swap_to_search():
    window.destroy()
    os.system('python search.py')

def swap_to_updatestudent():
    window.destroy()
    os.system('python updatestudent.py')

# Function to connect to MySQL database
def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",  # e.g., "localhost"
            user="root",  # e.g., "root"
            password="104969",
            database="studentmanagement"
        )
        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Connected to MySQL Server version {db_info}")
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print(f"You're connected to database: {record}")
            return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        messagebox.showerror("Database Connection Error", f"Error: {err}")
        return None

# Function to fetch and display student data
def fetch_and_display_students():
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM students")
            results = cursor.fetchall()
            if not results:
                print("No data found in the students table.")
                messagebox.showinfo("No Data", "No data found in the students table.")
                return
            print("Fetched Data:", results)  # Debug: Print fetched data
            for row in results:
                print("Inserting row into tree:", row)  # Debug: Print each row
                tree.insert("", "end", values=row)
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            messagebox.showerror("Database Query Error", f"Error: {err}")
        finally:
            connection.close()
    else:
        print("Connection to database failed.")

# Tkinter window setup
window = Tk()
window.geometry("1450x780")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=780,
    width=1450,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    228.0,
    410.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    229.0,
    124.0,
    image=image_image_2
)

canvas.create_text(
    146.0,
    237.0,
    anchor="nw",
    text="Admin Username",
    fill="#FFFFFF",
    font=("Inika", 20 * -1)
)

# Define the Treeview widget to display student data
tree = ttk.Treeview(window, columns=("StudentID", "Gender", "FullName", "Email", "Address", "Department"), show='headings')
tree.heading("StudentID", text="Student ID")
tree.heading("Gender", text="Gender")
tree.heading("FullName", text="Full Name")
tree.heading("Email", text="Email")
tree.heading("Address", text="Address")
tree.heading("Department", text="Department")
tree.place(x=500, y=100, width=900, height=600)

# Define the button to fetch and display data
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=swap_to_updatestudent,
    relief="flat"
)
button_1.place(
    x=1.28369140625,
    y=535.62451171875,
    width=455.7162780761719,
    height=81.54146575927734
)

# Update "All Student" button to fetch and display student data
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=swap_to_login,  # Command to fetch and display students
    relief="flat"
)
button_2.place(
    x=0.0,
    y=698.70751953125,
    width=455.7162780761719,
    height=81.54146575927734
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=swap_to_delete,
    relief="flat"
)
button_3.place(
    x=0.0,
    y=617.166015625,
    width=455.7162780761719,
    height=81.54146575927734
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=swap_to_add,
    relief="flat"
)
button_4.place(
    x=0.0,
    y=454.0830078125,
    width=455.7162780761719,
    height=81.54146575927734
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=swap_to_search,
    relief="flat"
)
button_5.place(
    x=1.28369140625,
    y=372.54150390625,
    width=455.7162780761719,
    height=81.54146575927734
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command= fetch_and_display_students,
    relief="flat"
)
button_6.place(
    x=1.28369140625,
    y=291.0,
    width=455.7162780761719,
    height=81.54146575927734
)

window.resizable(False, False)
window.mainloop()
