import tkinter as tk
from tkinter import *
import os, cv2
import shutil
import csv
import numpy as np
from PIL import ImageTk, Image
import pandas as pd
import datetime
import time
import tkinter.font as font
import pyttsx3

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# project module
import show_attendance
import takeImage
import trainImage
import automaticAttedance

# engine = pyttsx3.init()
# engine.say("Welcome!")
# engine.say("Please browse through your options..")
# engine.runAndWait()


def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()


haarcasecade_path = "haarcascade_frontalface_default.xml"
trainimagelabel_path = (
    "./TrainingImageLabel/Trainner.yml"
)
trainimage_path = "TrainingImage"
if not os.path.exists(trainimage_path):
    os.makedirs(trainimage_path)

studentdetail_path = (
    "./StudentDetails/studentdetails.csv"
)
attendance_path = "Attendance"

window = Tk()
window.title("Face Recognizer")
window.geometry("1280x720")
dialog_title = "QUIT"
dialog_text = "Are you sure want to close?"
window.configure(background="#1c1c1c")  # Dark theme


# to destroy screen
def del_sc1():
    sc1.destroy()


# error message for name and no
def err_screen():
    global sc1
    sc1 = tk.Tk()
    sc1.geometry("400x110")
    sc1.iconbitmap("AMS.ico")
    sc1.title("Warning!!")
    sc1.configure(background="#1c1c1c")
    sc1.resizable(0, 0)
    tk.Label(
        sc1,
        text="Enrollment & Name required!!!",
        fg="yellow",
        bg="#1c1c1c",  # Dark background for the error window
        font=("Verdana", 16, "bold"),
    ).pack()
    tk.Button(
        sc1,
        text="OK",
        command=del_sc1,
        fg="yellow",
        bg="#333333",  # Darker button color
        width=9,
        height=1,
        activebackground="red",
        font=("Verdana", 16, "bold"),
    ).place(x=110, y=50)

def testVal(inStr, acttyp):
    if acttyp == "1":  # insert
        if not inStr.isdigit():
            return False
    return True


logo = Image.open("UI_Image/0001.png")
logo = logo.resize((50, 47), Image.LANCZOS)
logo1 = ImageTk.PhotoImage(logo)
titl = tk.Label(window, bg="#1c1c1c", relief=RIDGE, bd=10, font=("Verdana", 30, "bold"))
titl.pack(fill=X)
l1 = tk.Label(window, image=logo1, bg="#1c1c1c",)
l1.place(x=470, y=10)


titl = tk.Label(
    window, text="CLASS VISION", bg="#1c1c1c", fg="yellow", font=("Verdana", 27, "bold"),
)
titl.place(x=525, y=12)

a = tk.Label(
    window,
    text="Welcome to CLASS VISION",
    bg="#1c1c1c",  # Dark background for the main text
    fg="yellow",  # Bright yellow text color
    bd=10,
    font=("Verdana", 35, "bold"),
)
a.pack()


ri = Image.open("UI_Image/register.png")
r = ImageTk.PhotoImage(ri)
label1 = Label(window, image=r)
label1.image = r
label1.place(x=100, y=270)

COLORS = {
    "background": "#101820",
    "surface": "#17232e",
    "surface_light": "#20313e",
    "text": "#f3f7f9",
    "muted": "#9cafb8",
    "accent": "#2dd4bf",
    "accent_dark": "#159a8c",
    "warning": "#f4c95d",
}
window.configure(background=COLORS["background"])
window.minsize(980, 620)

try:
    window.iconbitmap("AMS.ico")
except tk.TclError:
    pass

header = tk.Frame(window, bg=COLORS["surface"], height=86)
header.pack(fill=X)
header.pack_propagate(False)

logo = Image.open("UI_Image/0001.png").resize((46, 43), Image.LANCZOS)
logo1 = ImageTk.PhotoImage(logo)
tk.Label(header, image=logo1, bg=COLORS["surface"]).pack(side=LEFT, padx=(30, 14), pady=20)

brand = tk.Frame(header, bg=COLORS["surface"])
brand.pack(side=LEFT, pady=15)
tk.Label(
    brand, text="CLASS VISION", bg=COLORS["surface"], fg=COLORS["text"],
    font=("Segoe UI Semibold", 20),
).pack(anchor=W)
tk.Label(
    brand, text="FACE ATTENDANCE SYSTEM", bg=COLORS["surface"], fg=COLORS["muted"],
    font=("Segoe UI", 9),
).pack(anchor=W)

tk.Label(
    header, text="●  SYSTEM READY", bg=COLORS["surface"], fg=COLORS["accent"],
    font=("Segoe UI Semibold", 10),
).pack(side=RIGHT, padx=30)

content = tk.Frame(window, bg=COLORS["background"])
content.pack(fill=BOTH, expand=True, padx=34, pady=(28, 20))

tk.Label(
    content, text="Attendance workspace", bg=COLORS["background"], fg=COLORS["text"],
    font=("Segoe UI Semibold", 26),
).pack(anchor=W)
tk.Label(
    content, text="Register students, train recognition, and record attendance.",
    bg=COLORS["background"], fg=COLORS["muted"], font=("Segoe UI", 11),
).pack(anchor=W, pady=(3, 24))

actions = tk.Frame(content, bg=COLORS["background"])
actions.pack(fill=X, expand=True)
for column in range(3):
    actions.columnconfigure(column, weight=1)


def make_action_card(parent, column, image_path, eyebrow, title, description, command):
    card = tk.Frame(parent, bg=COLORS["surface"], padx=20, pady=18)
    card.grid(row=0, column=column, sticky="nsew", padx=(0 if column == 0 else 9, 9 if column < 2 else 0))
    image = Image.open(image_path).resize((86, 86), Image.LANCZOS)
    image_ref = ImageTk.PhotoImage(image)
    image_label = tk.Label(card, image=image_ref, bg=COLORS["surface"])
    image_label.image = image_ref
    image_label.pack(anchor=W)
    tk.Label(
        card, text=eyebrow.upper(), bg=COLORS["surface"], fg=COLORS["accent"],
        font=("Segoe UI Semibold", 9),
    ).pack(anchor=W, pady=(17, 4))
    tk.Label(
        card, text=title, bg=COLORS["surface"], fg=COLORS["text"],
        font=("Segoe UI Semibold", 16),
    ).pack(anchor=W)
    tk.Label(
        card, text=description, bg=COLORS["surface"], fg=COLORS["muted"],
        font=("Segoe UI", 10), justify=LEFT, wraplength=230,
    ).pack(anchor=W, pady=(7, 17))
    tk.Button(
        card, text=title, command=command, cursor="hand2", bd=0, relief=FLAT,
        bg=COLORS["accent_dark"], activebackground=COLORS["accent"],
        fg=COLORS["text"], activeforeground=COLORS["background"],
        font=("Segoe UI Semibold", 10), padx=15, pady=9,
    ).pack(anchor=W, fill=X)


def automatic_attedance():
    automaticAttedance.subjectChoose(text_to_speech)


def view_attendance():
    show_attendance.subjectchoose(text_to_speech)


make_action_card(
    actions, 0, "UI_Image/register.png", "Step 01", "Register student",
    "Capture face images and add a student profile.", lambda: TakeImageUI(),
)
make_action_card(
    actions, 1, "UI_Image/attendance.png", "Step 02", "Take attendance",
    "Recognize faces and record today’s attendance.", automatic_attedance,
)
make_action_card(
    actions, 2, "UI_Image/verifyy.png", "Step 03", "View attendance",
    "Open attendance sheets and review saved records.", view_attendance,
)

footer = tk.Frame(content, bg=COLORS["background"])
footer.pack(fill=X, pady=(24, 0))
tk.Label(
    footer, text="Camera access is required for registration and recognition.",
    bg=COLORS["background"], fg=COLORS["muted"], font=("Segoe UI", 9),
).pack(side=LEFT)
tk.Button(
    footer, text="Exit application", command=quit, cursor="hand2", bd=0,
    bg=COLORS["background"], activebackground=COLORS["surface_light"],
    fg=COLORS["muted"], activeforeground=COLORS["text"],
    font=("Segoe UI Semibold", 10), padx=16, pady=7,
).pack(side=RIGHT)


def TakeImageUI():
    ImageUI = Tk()
    ImageUI.title("Take Student Image..")
    ImageUI.geometry("780x480")
    ImageUI.configure(background="#1c1c1c")
    ImageUI.resizable(0, 0)
    titl = tk.Label(ImageUI, bg="#1c1c1c", relief=RIDGE, bd=10, font=("Verdana", 30, "bold"))
    titl.pack(fill=X)
    titl = tk.Label(
        ImageUI, text="Register Your Face", bg="#1c1c1c", fg="green", font=("Verdana", 30, "bold"),
    )
    titl.place(x=270, y=12)
    a = tk.Label(
        ImageUI,
        text="Enter the details",
        bg="#1c1c1c",
        fg="yellow",
        bd=10,
        font=("Verdana", 24, "bold"),
    )
    a.place(x=280, y=75)
    lbl1 = tk.Label(
        ImageUI,
        text="Enrollment No",
        width=10,
        height=2,
        bg="#1c1c1c",
        fg="yellow",
        bd=5,
        relief=RIDGE,
        font=("Verdana", 14),
    )
    lbl1.place(x=120, y=130)
    txt1 = tk.Entry(
        ImageUI,
        width=17,
        bd=5,
        validate="key",
        bg="#333333",  # Dark input background
        fg="yellow",  # Bright text color for input
        relief=RIDGE,
        font=("Verdana", 18, "bold"),
    )
    txt1.place(x=250, y=130)
    txt1["validatecommand"] = (txt1.register(testVal), "%P", "%d")

    # name
    lbl2 = tk.Label(
        ImageUI,
        text="Name",
        width=10,
        height=2,
        bg="#1c1c1c",
        fg="yellow",
        bd=5,
        relief=RIDGE,
        font=("Verdana", 14),
    )
    lbl2.place(x=120, y=200)
    txt2 = tk.Entry(
        ImageUI,
        width=17,
        bd=5,
        bg="#333333",  # Dark input background
        fg="yellow",  # Bright text color for input
        relief=RIDGE,
        font=("Verdana", 18, "bold"),
    )
    txt2.place(x=250, y=200)

    lbl3 = tk.Label(
        ImageUI,
        text="Notification",
        width=10,
        height=2,
        bg="#1c1c1c",
        fg="yellow",
        bd=5,
        relief=RIDGE,
        font=("Verdana", 14),
    )
    lbl3.place(x=120, y=270)

    message = tk.Label(
        ImageUI,
        text="",
        width=32,
        height=2,
        bd=5,
        bg="#333333",  # Dark background for messages
        fg="yellow",  # Bright text color for messages
        relief=RIDGE,
        font=("Verdana", 14, "bold"),
    )
    message.place(x=250, y=270)

    def take_image():
        l1 = txt1.get()
        l2 = txt2.get()
        takeImage.TakeImage(
            l1,
            l2,
            haarcasecade_path,
            trainimage_path,
            message,
            err_screen,
            text_to_speech,
        )
        txt1.delete(0, "end")
        txt2.delete(0, "end")

    # take Image button
    # image
    takeImg = tk.Button(
        ImageUI,
        text="Take Image",
        command=take_image,
        bd=10,
        font=("Verdana", 18, "bold"),
        bg="#333333",  # Dark background for the button
        fg="yellow",  # Bright text color for the button
        height=2,
        width=12,
        relief=RIDGE,
    )
    takeImg.place(x=130, y=350)

    def train_image():
        trainImage.TrainImage(
            haarcasecade_path,
            trainimage_path,
            trainimagelabel_path,
            message,
            text_to_speech,
        )

    # train Image function call
    trainImg = tk.Button(
        ImageUI,
        text="Train Image",
        command=train_image,
        bd=10,
        font=("Verdana", 18, "bold"),
        bg="#333333",  # Dark background for the button
        fg="yellow",  # Bright text color for the button
        height=2,
        width=12,
        relief=RIDGE,
    )
    trainImg.place(x=360, y=350)

window.mainloop()
