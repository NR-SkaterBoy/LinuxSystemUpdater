#!/usr/bin/python3
# Developer: NR-SkaterBoy
# Github: https://github.com/NR-SkaterBoy
# E-mail: nr.rick.dev@gmail.com
# Linux Systems source package Updater
# Version: Alpha 0.3

# Import modules
import os
import stat
import subprocess
import webbrowser
import time
import platform
from pickle import NONE
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *

# Set the file(s) rights
os.chmod("bash/system_update.sh", stat.S_IRWXU)


class LSU:
    def __init__(self, master):
        self.master = master
        master.title("Linux Updater")
        master.geometry("800x450+50+50")
        root.resizable(width=False, height=False)
        master.configure(background="#181d31")
        # master.iconbitmap("icons/lsu.ico")
        photo = PhotoImage(file="icons/logo2.png")
        master.iconphoto(False, photo)

        # LogFolder
        if (os.path.isdir("logs") != True):
            os.mkdir(os.path.join("logs"))

        # Autolog
        # *** Datas *** #
        runtime = time.strftime("%Y%m%d-%H%M%S")  # When launched this software
        sys = platform.platform()
        py = platform.python_version()
        platform.system()

        logFile = open(f"logs/autolog.log", "a")
        logFile.write(
            f"Launched time: {runtime}\nPlatform: {sys}\nPython version: {py}\n\n")
        logFile.close()

        def runningSystemUpdate():
            subprocess.call("bash/system_update.sh")

        def openMyWebsite():
            webbrowser.open_new(r"https://richardneuvald.tk")

        def openMyGithub():
            webbrowser.open_new(r"https://github.com/NR-SkaterBoy")

        def supportedSystem():
            messagebox.showwarning("Supported Systems",
                                   "Ubuntu, Kali Linux, Raspbian")

        def aboutSoftware():
            messagebox.showinfo("About this project", "Most PC users stick to Windows and are not willing to change to Linux because there are fewer GUI applications and they would need to learn the basic Linux commands. Moreover, most Linux-based systems get an update every week and some people think it is a waste of time to type the update commands.\n\nThis app may come handy for both beginners and advanced users because it is able to update the system by simply clicking a button. It supports over 10 different systems and has a built-in OS recognizer.\n\nVersion: Alpha 0.3")

        def quitLSU():
            root.quit()

        def openQuestionnaire():
            webbrowser.open_new(r"https://forms.gle/Xb5kY6cajjvRHTNB7")

        def openLastLog():
            lastLog = []
            if len(os.listdir("logs")) == 0:
                messagebox.showerror("Error", "No log file")
            else:
                with open("logs/autolog.log", encoding="utf-8") as f:
                    for line in (f.readlines()[-4:]):
                        lastLog.append(line)
                    messagebox.showinfo("Last Log", f"{lastLog[0]}{lastLog[1]}{lastLog[2]}")

        # Menu
        self.menubar = Menu(root, background='#ffffff', foreground='black',
                            activebackground='white', activeforeground='black')
        help = Menu(self.menubar, tearoff=0, background='#ffffff')
        help.add_command(label="Supported System", command=supportedSystem)
        help.add_command(label="About", command=aboutSoftware)
        help.add_command(label="Quit", command=quitLSU)
        self.menubar.add_cascade(label="Help", menu=help)
        userHelp = Menu(self.menubar, tearoff=0, background='#ffffff')
        # userHelp.add_command(label="Changelog", command=changelog) # Not available yet
        userHelp.add_command(label="Questionnaire", command=openQuestionnaire)
        self.menubar.add_cascade(label="News", menu=userHelp)
        logs = Menu(self.menubar, tearoff=0, background='#ffffff')
        logs.add_command(label="Open last Log", command=openLastLog)
        self.menubar.add_cascade(label="Logger", menu=logs)
        # Title
        self.label = Label(root, text='System\nUpdater', bg="#181d31",
                           fg="#ffffff", font=('arial', 40, 'bold')).place(x=60, y=25)
        # Btn of sysupdate
        self.add_btn = Button(root, text='Update your system', bg='#F0F8FF', width=20, font=(
            'arial', 12, 'normal'), command=runningSystemUpdate).place(x=70, y=190)
        # Btn of my website
        self.add_btn = Button(root, text='Visit my Website', bg='#F0F8FF', width=20, font=(
            'arial', 12, 'normal'), command=openMyWebsite).place(x=70, y=250)
        # Btn of my github profile
        self.add_btn = Button(root, text='Follow me on Github', bg='#F0F8FF', width=20, font=(
            'arial', 12, 'normal'), command=openMyGithub).place(x=70, y=310)
        # Pictures
        self.lsu_pic = Canvas(root, height=470, width=449,
                              bg="#181d31", borderwidth=0, highlightthickness=0)
        self.picture_file = PhotoImage(file='pictures/lsu.png')
        self.lsu_pic.create_image(470, 0, anchor=NE, image=self.picture_file)
        self.lsu_pic.place(x=290, y=54)
        # Menu
        root.config(menu=self.menubar)


root = Tk()
lsu = LSU(root)
root.mainloop()
