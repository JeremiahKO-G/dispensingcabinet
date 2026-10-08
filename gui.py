import ctypes
import tkinter as tk
from tkinter import ttk

# load login screen
def load_login_screen():
    # styles
    style = ttk.Style()
    style.configure("Modern.TEntry", padding=5, font=("Segui", 16))

    # wipe the screen
    for widget in root.winfo_children():
        widget.destroy()

    # load the main screen
    root.title('Username_info')

    # grid
    root.rowconfigure(0, weight=2)
    root.rowconfigure(1, weight=2)
    root.rowconfigure(2, weight=1)
    root.rowconfigure(3, weight=1)
    root.columnconfigure(0, weight=1, minsize=root.winfo_width() / 4)
    root.columnconfigure(1, weight=1, minsize=root.winfo_width() / 4)
    root.columnconfigure(2, weight=1, minsize=root.winfo_width() / 4)
    root.columnconfigure(3, weight=1, minsize=root.winfo_width() / 4)

    # wlc logo
    wlc_nursing_logo_img = tk.PhotoImage(file="./images/WLC_Nursing_Logo.png")
    wlc_nursing_logo = ttk.Label(root, image=wlc_nursing_logo_img)
    wlc_nursing_logo.grid(column=1, row=0, padx=5, pady=5, columnspan=2)

    root.wlc_nursing_logo_img = wlc_nursing_logo_img

    # name box
    name_label = ttk.Label(root, text='Name  ', font=("Segui", 14))
    name_label.grid(column=1, row=1, sticky='NE')

    name = ttk.Entry(root, style="Modern.TEntry")
    name.grid(column=2, row=1, sticky='NW')
    name.focus()

    # password box
    password_label = ttk.Label(root, text='Password  ', font=("Segui", 14))
    password_label.grid(column=1, row=1, sticky='E')

    password = ttk.Entry(root, show='*')
    password.grid(column=2, row=1, sticky='W')

    # Login button -> new window with user info
    enter = ttk.Button(root, text='Login', command=lambda: load_menu_screen(name))
    enter.grid(column=2, row=1, sticky='SW')

# load menu screen
def load_menu_screen(name):
    username = name.get()

    # wipe the screen
    for widget in root.winfo_children():
        widget.destroy()

    # load menu
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=2)
    root.rowconfigure(2, weight=1)
    root.columnconfigure(0, weight=1, minsize=root.winfo_width()/4)
    root.columnconfigure(1, weight=2, minsize=root.winfo_width()/2)
    root.columnconfigure(2, weight=1, minsize=root.winfo_width()/4)

    label = tk.Label(font=('Segui', 16), text='Hello ' + username)
    label.grid(column=0, row=0, sticky='NW', columnspan=3)

    # placeholder img
    place_holder_img = tk.PhotoImage(file="./images/placeholder-image-vertical.png")
    place_holder = ttk.Label(root, image=place_holder_img)
    place_holder.grid(column=1, row=1, padx=5, pady=5)

    root.place_holder_img = place_holder_img

    # Login button -> new window with user info
    logout = ttk.Button(root, text='Logout', command=lambda: load_login_screen())
    logout.grid(column=1, row=2, sticky='')

ctypes.windll.shcore.SetProcessDpiAwareness(1)

# create main window
root = tk.Tk()
root.attributes('-fullscreen', True)

load_login_screen()

root.mainloop()