#!/usr/bin/python3
# Developer: NR-SkaterBoy
# Github: https://github.com/NR-SkaterBoy
# E-mail: nr.rick.dev@gmail.com
# Linux Systems source package Updater
# Version: Alpha 0.4

# Import modules
from cgitb import text
import os
import sys
import socket
import re
import tkinter
import uuid
import json
import logging
import stat
import subprocess
import webbrowser
import time
import platform
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *

# You won't get error message if you are on windows
if (platform.system() != "Windows"):
    import cpuinfo
    import psutil

# Set the file(s) rights
os.chmod("bash/system_update.sh", stat.S_IRWXU)

# Terminal
# os.system("gnome-terminal 'bash -c \"sudo apt-get update; exec bash\"'") // It opens terminal


class LSU:
    def __init__(self, master):
        self.master = master
        master.title("Linux Updater")
        master.geometry("800x450+50+50")
        root.resizable(True, True)
        root.minsize(width=800, height=450)
        master.configure(background="#181d31")
        # master.iconbitmap("icons/lsu.ico")
        photo = PhotoImage(file="icons/logo2.png")
        master.iconphoto(False, photo)

        # LogFolder and
        def createFolders():
            if (os.path.isdir("logs") != True):
                os.mkdir(os.path.join("logs"))
            if (os.path.isdir("extensions") != True):
                os.mkdir(os.path.join("extensions"))
        createFolders()

        # Autolog
        # *** Datas *** #
        runtime = time.strftime("%Y-%m-%d - %H:%M:%S")
        sys = platform.platform()
        py = platform.python_version()
        platform.system()

        def runtimeLog():
            logFile = open(f"logs/autolog.log", "a")
            logFile.write(
                f"Launched time: {runtime}\nPlatform: {sys}\nPython version: {py}\n")
            logFile.close()
        runtimeLog()

        # About Device
        # LogTypes
        def criticalLog():
            logging.basicConfig(
                level=logging.CRITICAL,
                format="{asctime} {levelname:<50} {message}",
                style='{',
                filename="logs/applog.log",
                filemode="a"
            )

        def errorLog():
            logging.basicConfig(
                level=logging.ERROR,
                format="{asctime} {levelname:<40} {message}",
                style='{',
                filename="logs/applog.log",
                filemode="a"
            )

        def warningLog():
            logging.basicConfig(
                level=logging.WARNING,
                format="{asctime} {levelname:<30} {message}",
                style='{',
                filename="logs/applog.log",
                filemode="a"
            )

        def infoLog():
            logging.basicConfig(
                level=logging.INFO,
                format="{asctime} {levelname:<20} {message}",
                style='{',
                filename="logs/applog.log",
                filemode="a"
            )

        def debugLog():
            logging.basicConfig(
                level=logging.DEBUG,
                format="{asctime} {levelname:<10} {message}",
                style='{',
                filename="logs/applog.log",
                filemode="a"
            )

        # It doesn't work on windows
        def getSystemInfo():
            try:
                info = {}
                info['Platform'] = platform.system()
                info['Platform-release'] = platform.release()
                info['Platform-version'] = platform.version()
                info['Architecture'] = platform.machine()
                info['Hostname'] = socket.gethostname()
                info['IP-address'] = socket.gethostbyname(socket.gethostname())
                info['MAC-address'] = ':'.join(re.findall('..',
                                               '%012x' % uuid.getnode()))
                if (platform.system() != "Windows"):
                    info['Processor'] = cpuinfo.get_cpu_info()['brand_raw']
                    info['RAM'] = str(
                        round(psutil.virtual_memory().total / (1024.0 ** 3)))+" GB"
                json_object = json.dumps(info, indent=3)
                with open("extensions/sysinfo.json", "w") as f:
                    f.write(json_object)
                    f.close()
                return json.dumps(info)
            except:
                logging.basicConfig(
                    filename="logs/error_sysinfo.log", encoding='utf-8', level=logging.INFO)
                logging.info(f"Time: {runtime}", exc_info=True)
        getSystemInfo()

        def runningSystemUpdate():
            try:
                subprocess.call("bash/system_update.sh")
            except Exception as e:
                criticalLog()
                logging.critical(
                    "\n\nYou have to use Linux system", exc_info=True)

        def openMyWebsite():
            webbrowser.open_new(r"https://richardneuvald.tk")

        def openMyGithub():
            webbrowser.open_new(r"https://github.com/NR-SkaterBoy")

        def supportedSystem():
            messagebox.showwarning("Supported Systems",
                                   "Ubuntu, Kali Linux, Raspbian")

        def systemInfo():
            log = json.load(open("extensions/sysinfo.json", "r"))
            messagebox.showinfo("System Information", log) # TODO: Edit output
        # systemInfo()

        def aboutSoftware():
            messagebox.showinfo("About this project", "Most PC users stick to Windows and are not willing to change to Linux because there are fewer GUI applications and they would need to learn the basic Linux commands. Moreover, most Linux-based systems get an update every week and some people think it is a waste of time to type the update commands.\n\nThis app may come handy for both beginners and advanced users because it is able to update the system by simply clicking a button. It supports over 10 different systems and has a built-in OS recognizer.\n\nVersion: Alpha 0.4")

        def quitLSU():
            logFile = open(f"logs/autolog.log", "a")
            logFile.write(
                f"Exit time: {runtime}\n\n")
            logFile.close()
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
                    messagebox.showinfo(
                        "Last Log", f"{lastLog[0]}{lastLog[1]}{lastLog[2]}")
        
        
        def setting():
            add_node = IntVar()
            
            def save():
                if (add_node.get() == 1):
                    save_btn["state"] = NORMAL
                    save_btn.configure(text="HEY")
            
            settings = tkinter.Tk()
            settings.title("Settings")
            settings.geometry("300x300")
            settings.resizable(False, False)
            Checkbutton(settings, variable=add_node, offvalue=0, text='Node Update', bg='#F0F8FF', width=20, font=(
            'arial', 12, 'normal'), command=save).place(x=50, y=30)
            save_btn = Button(settings, text='Save', state=DISABLED, bg='#F0F8FF', width=20, font=('arial', 12, 'normal'), command=None).place(x=50, y=240)
            settings.mainloop()
        setting()
            

        # Menu
        self.menubar = Menu(root, background='#ffffff', foreground='black',
                            activebackground='white', activeforeground='black')
        help = Menu(self.menubar, tearoff=0, background='#ffffff')
        help.add_command(label="Supported System", command=supportedSystem)
        help.add_command(label="About", command=aboutSoftware)
        help.add_command(label="About System", command=systemInfo)
        help.add_command(label="Quit", command=quitLSU)
        self.menubar.add_cascade(label="Help", menu=help)
        userHelp = Menu(self.menubar, tearoff=0, background='#ffffff')
        userHelp.add_command(label="Changelog", command=setting) # Not available yet
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


if __name__ == "__main__":
    try:
        root = Tk(className="Linux System Updater")
        lsu = LSU(root)
        root.mainloop()
    except Exception as e:
        logging.basicConfig(
            level=logging.CRITICAL,
            format="{asctime} {levelname:<8} {message}",
            style='{',
            filename="logs/applog.log",
            filemode="a"
        )
        logging.critical("\n\nThere was an error with LSU!", exc_info=True)
