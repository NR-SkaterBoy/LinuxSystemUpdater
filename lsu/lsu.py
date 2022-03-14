# # Import modules
import os, sys, stat, subprocess
from pickle import NONE
import tkinter as tk
from tkinter import ttk
from tkinter import *

# print(subprocess.call("pwd"))

#Set the files right
os.chmod("bash/source_update.sh", stat.S_IRWXU)
os.chmod("bash/system_update.sh", stat.S_IRWXU)

# Import os-update script
def running_os_update_script():
    subprocess.call("bash/system_update.sh")

# Import source update
def running_source_update_script():
    subprocess.call("bash/source_update.sh")

# Application

# Colors
background_color = "#181d31"
btn_color = "#42485d"

root = Tk()

# Window, title, icon, background
root.geometry("800x450+50+50")
root.configure(background=background_color)
root.title('Linux Updater')
# root.iconbitmap("icons/lsu.ico")
root.tk.call("wm", "iconphoto", root._w, tk.PhotoImage("icons/logo2png"))

# Title
Label(root, text='System\nUpdater', bg=background_color, fg="#ffffff", font=('arial', 40, 'bold')).place(x=60, y=25)

# Btn of sysupdate
Button(root, text='Update the system', bg='#F0F8FF', font=('arial', 12, 'normal'), command=NONE).place(x=70, y=200)

# Btn of sourceupdate
Button(root, text='LINUX UPDATER', bg='#F0F8FF', font=('arial', 12, 'normal'), command=NONE).place(x=70, y=260)

# Pictures
lsu_pic= Canvas(root, height=470, width=449, bg=background_color, borderwidth=0, highlightthickness=0)
picture_file = PhotoImage(file = 'pictures/lsu.png')
lsu_pic.create_image(470, 0, anchor=NE, image=picture_file)
lsu_pic.place(x=285, y=54)

root.mainloop()