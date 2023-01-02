from tkinter import *

OPTIONS = [
"hello_world",
"save_file",
"create_object"
] #etc


def hello_world():
    print("Hello World")
    pass


def save_file():
    print("File Saved")
    pass


def create_object():
    print("Object Created")
    pass


def picker():
    if variable.get() == "hello_world":
        hello_world()
    if variable.get() == "save_file":
        save_file()
    if variable.get() == "create_object":
        create_object()


root = Tk()
root.geometry("100x100")
root.title("Dropdown demo")

variable = StringVar(root)
variable.set(OPTIONS[0]) # default value

om = OptionMenu(root, variable, *OPTIONS)
om.pack()

caller_button = Button(text="Call function", command=lambda: picker())
caller_button.pack(pady=10)


mainloop()

import tkinter as tk
from tkinter import ttk, messagebox


def show_about_info():
    messagebox.showinfo(
        title="About",
        message="Tkinter is GUI for Python programing language."
    )


def quit_app():
    root.destroy()


def example():
    print("Example")


root = tk.Tk()
root.title("Menu dropdown example")
root.option_add("*tearOff", False)

main = ttk.Frame(root)
main.pack(fill="both", expand=True, padx=1, pady=(4, 0))

menubar = tk.Menu()
root.config(menu=menubar)

file_menu = tk.Menu(menubar)
help_menu = tk.Menu(menubar)

menubar.add_cascade(menu=file_menu, label="File")
menubar.add_cascade(menu=help_menu, label="Help")

file_menu.add_command(label="New", command=example)
file_menu.add_command(label="Save File", command=example)
file_menu.add_command(label="Open File", command=example)
file_menu.add_command(label="Close Tab", command=example)
file_menu.add_command(label="Exit", command=quit_app)

help_menu.add_command(label="About", command=show_about_info)

notebook = ttk.Notebook(main)
notebook.pack(fill="both", expand=True)


root.mainloop()
