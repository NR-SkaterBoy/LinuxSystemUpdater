#!/usr/bin/python3
# Developer: NR-SkaterBoy
# Github: https://github.com/NR-SkaterBoy
# E-mail: nr.rick.dev@gmail.com
# Linux Systems source package update

# Import modules
import os, sys, stat, subprocess
import webbrowser
from pickle import NONE
import tkinter as tk
from tkinter import ttk
from tkinter import *

# print(subprocess.call("pwd"))

# Set the files right
os.chmod("bash/myaskpass.sh", stat.S_IRWXU)
os.chmod("bash/source_update.sh", stat.S_IRWXU)
os.chmod("bash/system_update.sh", stat.S_IRWXU)

# Import Sys-update script
def runningSystemUpdate():
    subprocess.call("bash/system_update.sh")
    subprocess.call("bash/source_update.sh")

# Webopen
def openMyWebsite():
    webbrowser.open_new(r"https://richardneuvald.tk")

def openMyGithub():
    webbrowser.open_new(r"https://github.com/NR-SkaterBoy")

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
Button(root, text='Update your system', bg='#F0F8FF', width=20, font=('arial', 12, 'normal'), command=runningSystemUpdate).place(x=70, y=200)

# Btn of my website
Button(root, text='Check my Website', bg='#F0F8FF', width=20, font=('arial', 12, 'normal'), command=openMyWebsite).place(x=70, y=260)

# Btn of my github profile
Button(root, text='Check my Github profile', bg='#F0F8FF', width=20, font=('arial', 12, 'normal'), command=openMyGithub).place(x=70, y=320)


# Pictures
lsu_pic= Canvas(root, height=470, width=449, bg=background_color, borderwidth=0, highlightthickness=0)
picture_file = PhotoImage(file = 'pictures/lsu.png')
lsu_pic.create_image(470, 0, anchor=NE, image=picture_file)
lsu_pic.place(x=285, y=54)

root.mainloop()
