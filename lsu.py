#!/usr/bin/python3
# Developer: NR-SkaterBoy
# Github: https://github.com/NR-SkaterBoy
# E-mail: nr.rick.dev@gmail.com
# Linux Systems source package update

# Import modules
import os, stat, subprocess, webbrowser, time, platform, glob
from pickle import NONE
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *

# Set the files right
# os.chmod("bash/myaskpass.sh", stat.S_IRWXU)
# os.chmod("bash/system_update.sh", stat.S_IRWXU)

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

        def runningSystemUpdate():
            subprocess.call("bash/system_update.sh")
        def openMyWebsite():
            webbrowser.open_new(r"https://richardneuvald.tk")
        def openMyGithub():
            webbrowser.open_new(r"https://github.com/NR-SkaterBoy")
        def supportedSystem():
            messagebox.showwarning("Supported Systems", "Ubuntu, Kali Linux, Raspbian")
        def aboutSoftware():
            messagebox.showinfo("About this project", "Most PC users stick to Windows and are not willing to change to Linux because there are fewer GUI applications and they would need to learn the basic Linux commands. Moreover, most Linux-based systems get an update every week and some people think it is a waste of time to type the update commands.\n\nThis app may come handy for both beginners and advanced users because it is able to update the system by simply clicking a button. It supports over 10 different systems and has a built-in OS recognizer.\n\nVersion: Alpha 0.2")
        def quitLSU():
            root.quit()
        def questionnaire():
            webbrowser.open_new(r"https://forms.gle/Xb5kY6cajjvRHTNB7")
        def changelog():
            messagebox.showinfo("Changelog Alpha 0.2", "Soon")
        def createLog():
            getTime = time.strftime("%Y%m%d-%H%M%S")
            is_dir = os.path.isdir("logs")
            if (is_dir != True):
                os.mkdir(os.path.join("logs"))
            
            logFile = open(f"logs/log_{getTime}.txt", "x")
            
            # Sysinfo
            arh = platform.platform()
            system = platform.system()
            vers = platform.version()
            proc = platform.processor()
            pyvers = platform.python_version()
            # distro = platform.freedesktop_os_release()
            
            logFile.write(f"{arh}\n{system}\n{vers}\n{proc}\n{pyvers}")
            logFile.close()
        def openLastLog():
            fileList = glob.glob(os.path.join("logs", "*"))
            fileName = ""
            for log in fileList:
                with open(f"{fileName}") as f:
                    print()

            # Az utolsó file lekérése és kiíratása

        def deleteAllLog():
            fileList = glob.glob(os.path.join("logs", "*"))
            for f in fileList:
                os.remove(f)         
            

        # Menu
        self.menubar = Menu(root, background='#ffffff', foreground='black', activebackground='white', activeforeground='black')  
        help = Menu(self.menubar, tearoff=0, background='#ffffff')  
        help.add_command(label="Supported System", command=supportedSystem)  
        help.add_command(label="About", command=aboutSoftware)  
        help.add_command(label="Quit", command=quitLSU)
        self.menubar.add_cascade(label="Help", menu=help)
        userHelp = Menu(self.menubar, tearoff=0, background='#ffffff')
        # userHelp.add_command(label="Changelog", command=changelog)
        userHelp.add_command(label="Questionnaire", command=questionnaire)
        self.menubar.add_cascade(label="News", menu=userHelp)
        logs = Menu(self.menubar, tearoff=0, background='#ffffff')
        logs.add_command(label="Create new Log", command=createLog)
        logs.add_command(label="Open last Log", command=NONE)
        logs.add_command(label="Delete all Log", command=deleteAllLog)
        self.menubar.add_cascade(label="Logger", menu=logs)
        # Title
        self.label = Label(root, text='System\nUpdater', bg="#181d31", fg="#ffffff", font=('arial', 40, 'bold')).place(x=60, y=25)
        # Btn of sysupdate
        self.add_btn = Button(root, text='Update your system', bg='#F0F8FF', width=20, font=('arial', 12, 'normal'), command=runningSystemUpdate).place(x=70, y=190)
        # Btn of my website
        self.add_btn = Button(root, text='Visit my Website', bg='#F0F8FF', width=20, font=('arial', 12, 'normal'), command=openMyWebsite).place(x=70, y=250)
        # Btn of my github profile
        self.add_btn = Button(root, text='Follow me on Github', bg='#F0F8FF', width=20, font=('arial', 12, 'normal'), command=openMyGithub).place(x=70, y=310)
        # Pictures
        self.lsu_pic = Canvas(root, height=470, width=449, bg="#181d31", borderwidth=0, highlightthickness=0)
        self.picture_file = PhotoImage(file = 'pictures/lsu.png')
        self.lsu_pic.create_image(470, 0, anchor=NE, image=self.picture_file)
        self.lsu_pic.place(x=290, y=54)
        # Menu
        root.config(menu=self.menubar)

root = Tk()
lsu = LSU(root)
root.mainloop()