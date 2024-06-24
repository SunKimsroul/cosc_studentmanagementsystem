import os
from pathlib import Path
import pymysql.cursors
from tkinter import Tk, Canvas, Entry, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Admin\Desktop\TKinter\Project\Login\assets add\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def swap_to_dashboard():
    window.destroy()
    os.system('python dashboard.py')

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
canvas.create_text(
    840.0,
    84.0,
    anchor="nw",
    text="Add New Student",
    fill="#000000",
    font=("Imprima Regular", 32 * -1)
)

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(647.5, 268.0, image=entry_image_1)
entry_1 = Entry(bd=0, bg="#FFFDFD", fg="#000716", highlightthickness=0)
entry_1.place(x=591.0, y=240.0, width=113.0, height=54.0)

canvas.create_text(
    588.0,
    208.0,
    anchor="nw",
    text="Student ID",
    fill="#000000",
    font=("Imprima Regular", 20 * -1)
)

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(827.0, 268.0, image=entry_image_2)
entry_2 = Entry(bd=0, bg="#FFFDFD", fg="#000716", highlightthickness=0)
entry_2.place(x=777.0, y=240.0, width=100.0, height=54.0)

canvas.create_text(
    792.0,
    208.0,
    anchor="nw",
    text="Gender",
    fill="#000000",
    font=("Imprima Regular", 20 * -1)
)

entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(734.0, 386.0, image=entry_image_3)
entry_3 = Entry(bd=0, bg="#FFFDFD", fg="#000716", highlightthickness=0)
entry_3.place(x=591.0, y=358.0, width=286.0, height=54.0)

canvas.create_text(
    588.0,
    326.0,
    anchor="nw",
    text="Email",
    fill="#000000",
    font=("Imprima Regular", 20 * -1)
)

entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(1152.0, 268.0, image=entry_image_4)
entry_4 = Entry(bd=0, bg="#FFFDFD", fg="#000716", highlightthickness=0)
entry_4.place(x=1009.0, y=240.0, width=286.0, height=54.0)

canvas.create_text(
    1006.0,
    208.0,
    anchor="nw",
    text="Full Name",
    fill="#000000",
    font=("Imprima Regular", 20 * -1)
)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(228.0, 410.0, image=image_image_1)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(216.0, 112.0, image=image_image_2)

canvas.create_text(
    129.0,
    231.0,
    anchor="nw",
    text="Admin Username",
    fill="#FFFFFF",
    font=("Inika", 20 * -1)
)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0, command=swap_to_updatestudent, relief="flat")
button_1.place(x=1.2837066650390625, y=535.62451171875, width=455.7162780761719, height=81.54146575927734)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0, command=lambda: swap_to_login, relief="flat")
button_2.place(x=0.0, y=698.70751953125, width=455.7162780761719, height=81.54146575927734)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(image=button_image_3, borderwidth=0, highlightthickness=0, command=swap_to_delete, relief="flat")
button_3.place(x=0.0, y=617.166015625, width=455.7162780761719, height=81.54146575927734)

button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_4 = Button(image=button_image_4, borderwidth=0, highlightthickness=0, command=lambda: print("button_4 clicked"), relief="flat")
button_4.place(x=0.0, y=454.0830078125, width=455.7162780761719, height=81.54146575927734)

button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
button_5 = Button(image=button_image_5, borderwidth=0, highlightthickness=0, command=swap_to_search, relief="flat")
button_5.place(x=1.2837066650390625, y=372.54150390625, width=455.7162780761719, height=81.54146575927734)

button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
button_6 = Button(image=button_image_6, borderwidth=0, highlightthickness=0, command=swap_to_dashboard, relief="flat")
button_6.place(x=1.2837066650390625, y=291.0, width=455.7162780761719, height=81.54146575927734)

entry_image_5 = PhotoImage(file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(955.0, 527.0, image=entry_image_5)
entry_5 = Entry(bd=0, bg="#FFFDFD", fg="#000716", highlightthickness=0)
entry_5.place(x=812.0, y=499.0, width=286.0, height=54.0)

canvas.create_text(
    883.0,
    468.0,
    anchor="nw",
    text="Department",
    fill="#000000",
    font=("Imprima Regular", 20 * -1)
)

entry_image_6 = PhotoImage(file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(1149.0, 383.0, image=entry_image_6)
entry_6 = Entry(bd=0, bg="#FFFDFD", fg="#000716", highlightthickness=0)
entry_6.place(x=1007.0, y=355.0, width=284.0, height=54.0)

canvas.create_text(
    1004.0,
    323.0,
    anchor="nw",
    text="Address",
    fill="#000000",
    font=("Imprima Regular", 20 * -1)
)

def button_click():
    StudentID = entry_1.get()
    FullName = entry_4.get()
    Gender = entry_2.get().strip().capitalize()  # Ensure consistent case and remove leading/trailing whitespace
    Email = entry_3.get()
    Address = entry_6.get()
    Department = entry_5.get()

    valid_genders = ['Male', 'Female', 'Other']  # Valid ENUM values
    if Gender not in valid_genders:
        print("Invalid Gender")
        return

    try:
        conn = pymysql.connect(
            host='127.0.0.1', user='root', password='104969', db='studentmanagement'
        )
        a = conn.cursor()
        sql = """INSERT INTO students (StudentID, FullName, Gender, Email, Address, Department) 
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        val = (StudentID, FullName, Gender, Email, Address, Department)
        a.execute(sql, val)
        conn.commit()
        conn.close()
        print("Student added successfully")
        status_check()  # Call status_check function after successful insertion
    except pymysql.MySQLError as e:
        print(f"Error: {e}")

def status_check():
    canvas.create_text(
        800.0,
        590.0,
        anchor="nw",
        text="Student Registered",
        fill="#10b53c",
        font=("Imprima Regular", 32 * -1)
    )

button_image_7 = PhotoImage(file=relative_to_assets("button_7.png"))
button_7 = Button(image=button_image_7, borderwidth=0, highlightthickness=0, command=button_click, relief="flat")
button_7.place(x=724.0, y=698.70751953125, width=455.7162780761719, height=81.54146575927734)

window.resizable(False, False)
window.mainloop()
