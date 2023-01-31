
import secrets
from tkinter import *
import random
import string
import pyperclip
def generate_password(length: int):
    characters = ""
    if not (uppercase.get() or lowercase.get() or numbers.get() or special.get()):
        error_label.config(text="Please select at least one checkbox")
        root.after(3000, clear_error)
        return
    if uppercase.get():
        characters += string.ascii_uppercase
    if lowercase.get():
        characters += string.ascii_lowercase
    if numbers.get():
        characters += string.digits
    if special.get():
        characters += string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def clear_error():
    error_label.config(text="Select any of the checkboxes")
def on_generate():
    password = generate_password(length.get())
    password_var.set(password)

def on_copy():
    """
    Handle the "Copy to clipboard" button press
    """
    pyperclip.copy(password_var.get())

root = Tk()
root.config(bg = "light grey")
root.geometry("400x400")
root.resizable(0, 0)
root.title("PASSWORD GENERATOR")

# Add other widgets to the GUI
Label(root, text="PASSWORD GENERATOR", font='arial 15 bold',bg= "gray").pack()

# Label(root, text="Password Generator", font='arial 15 bold',bg="grey").pack(side=BOTTOM)
Label(root, text="PASSWORD LENGTH", font='arial 10 bold', bg="grey").pack()

length = IntVar()
Spinbox(root, from_=8, to_=32, textvariable=length, width=15).pack()
uppercase = BooleanVar()
lowercase = BooleanVar()
numbers = BooleanVar()
special = BooleanVar()

uppercase_check = Checkbutton(root, text="Uppercase", variable=uppercase)
uppercase_check.pack()
lowercase_check = Checkbutton(root, text="Lowercase", variable=lowercase)
lowercase_check.pack()
numbers_check = Checkbutton(root, text="Numbers", variable=numbers)
numbers_check.pack()
special_check = Checkbutton(root, text="Special", variable=special)
special_check.pack()
password_var = StringVar()
Entry(root, textvariable=password_var).pack()

Button(root, text="GENERATE PASSWORD",bg="grey", command=on_generate).pack(pady=5)
Button(root, text='COPY TO CLIPBOARD',bg="grey", command=on_copy).pack(pady=5)

error_label = Label(root, text="Select any of the checkbox")

root.mainloop()
