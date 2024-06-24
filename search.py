from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
from tkinter import ttk
import mysql.connector
import os
# Set the path to the assets directory
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Admin\Desktop\TKinter\Project\Login\assets searchmodify\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def swap_to_add():
    window.destroy()
    os.system('python add.py')

def swap_to_dashboard():
    window.destroy()
    os.system('python dashboard.py')

def swap_to_delete():
    window.destroy()
    os.system('python delete.py')

def swap_to_login():
    window.destroy()
    os.system('python login.py')

def swap_to_updatestudent():
    window.destroy()
    os.system('python updatestudent.py')

# Function to connect to MySQL database
def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1', user='root', password='104969', db='studentManagement'
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
    student_id = entry_1.get()
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        try:
            query = "SELECT StudentID, Gender, FullName, Email, Address, Department FROM students WHERE StudentID = %s"
            cursor.execute(query, (student_id,))
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

# Initialize Tkinter window
window = Tk()
window.geometry("1450x780")
window.configure(bg="#FFFFFF")

# Set up the canvas
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

# Load images and place them on the canvas
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(228.0, 410.0, image=image_image_1)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(216.0, 112.0, image=image_image_2)

canvas.create_text(129.0, 231.0, anchor="nw", text="Admin Username", fill="#FFFFFF", font=("Inika", 20 * -1))

# Define buttons and their actions
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0, command=swap_to_updatestudent, relief="flat")
button_1.place(x=1.28369140625, y=535.62451171875, width=455.7162780761719, height=81.54146575927734)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0, command=swap_to_login, relief="flat")
button_2.place(x=0.0, y=698.70751953125, width=455.7162780761719, height=81.54146575927734)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(image=button_image_3, borderwidth=0, highlightthickness=0, command=swap_to_delete, relief="flat")
button_3.place(x=0.0, y=617.166015625, width=455.7162780761719, height=81.54146575927734)

button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_4 = Button(image=button_image_4, borderwidth=0, highlightthickness=0, command=swap_to_add, relief="flat")
button_4.place(x=0.0, y=454.0830078125, width=455.7162780761719, height=81.54146575927734)

button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
button_5 = Button(image=button_image_5, borderwidth=0, highlightthickness=0, command=lambda: print("button_5 clicked"), relief="flat")
button_5.place(x=1.28369140625, y=372.54150390625, width=455.7162780761719, height=81.54146575927734)

button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
button_6 = Button(image=button_image_6, borderwidth=0, highlightthickness=0, command=swap_to_dashboard, relief="flat")
button_6.place(x=1.28369140625, y=291.0, width=455.7162780761719, height=81.54146575927734)

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(994.0, 638.0, image=image_image_3)

canvas.create_text(873.0, 18.0, anchor="nw", text="Search Student", fill="#000000", font=("Imprima Regular", 32 * -1))

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(994.5, 636.5, image=entry_image_1)
entry_1 = Entry(bd=0, bg="#FFFDFD", fg="#000716", highlightthickness=0)
entry_1.place(x=783.5, y=619.0, width=422.0, height=33.0)

canvas.create_text(925.0, 582.0, anchor="nw", text="Enter Student ID", fill="#000000", font=("Imprima Regular", 20 * -1))

button_image_7 = PhotoImage(file=relative_to_assets("button_7.png"))
button_7 = Button(image=button_image_7, borderwidth=0, highlightthickness=0, command=fetch_and_display_students, relief="flat")
button_7.place(x=905.0, y=669.0, width=179.341552734375, height=39.0)

# Create Treeview widget for displaying student data
tree = ttk.Treeview(window, columns=("StudentID", "Gender", "FullName", "Email", "Address", "Department"), show='headings')
tree.heading("StudentID", text="Student ID")
tree.heading("Gender", text="Gender")
tree.heading("FullName", text="Full Name")
tree.heading("Email", text="Email")
tree.heading("Address", text="Address")
tree.heading("Department", text="Department")
tree.place(x=600, y=100, width=800, height=400)

# Run the Tkinter event loop
window.resizable(False, False)
window.mainloop()


