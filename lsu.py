#!/usr/bin/python3
# Developer: NR-SkaterBoy
# Github: https://github.com/NR-SkaterBoy
# E-mail: nr.rick.dev@gmail.com
# Linux Systems source package Updater
# Version: Alpha 0.5

# TODO: Add pm2 update
# TODO: Make topmodel class

# Import modules
import os
import sys
import socket
import re
import uuid
import json
import logging
import stat
import subprocess
from subprocess import run
import webbrowser
import time
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
import platform

# You won't get error message if you are on windows
if (platform.system() != "Windows"):
    import cpuinfo
    import psutil

# Set the file(s) rights
directory = "bash"
for file in os.listdir(directory):
    files = os.path.join(directory, file)
    # print(files)
    os.chmod(files, stat.S_IRWXU)

# Terminal
# os.system("gnome-terminal 'bash -c \"sudo apt-get update; exec bash\"'") // It opens terminal

# LogTypes


def criticalLog():
    logging.basicConfig(
        level=logging.CRITICAL,
        format="{asctime} {levelname} {message}",
        style='{',
        filename="logs/critical.log",
        filemode="a"
    )


def errorLog():
    logging.basicConfig(
        level=logging.ERROR,
        format="{asctime} {levelname} {message}",
        style='{',
        filename="logs/error.log",
        filemode="a"
    )


def warningLog():
    logging.basicConfig(
        level=logging.WARNING,
        format="{asctime} {levelname} {message}",
        style='{',
        filename="logs/warning.log",
        filemode="a"
    )


def infoLog():
    logging.basicConfig(
        level=logging.INFO,
        format="{asctime} {levelname} {message}",
        style='{',
        filename="logs/info.log",
        filemode="a"
    )


def debugLog():
    logging.basicConfig(
        level=logging.DEBUG,
        format="{asctime} {levelname} {message}",
        style='{',
        filename="logs/debug.log",
        filemode="a"
    )


class LSU:
    def __init__(self, master):
        self.master = master
        master.title("Linux Updater")
        master.geometry("800x450+50+50")
        root.resizable(True, True)
        root.minsize(width=800, height=450)
        master.configure(background="#181d31")
        # master.iconbitmap("icons/lsu.ico")
        photo = PhotoImage(file="icons/lsu.png")
        master.iconphoto(False, photo)

        # LogFolder and neccesary file(s)
        def createFolders():
            if (os.path.isdir("logs") != True):
                os.mkdir(os.path.join("logs"))
            if (os.path.isdir("files") != True):
                os.mkdir(os.path.join("files"))
        createFolders()

        def files():
            if (os.path.isfile("files/node.json") != True):
                node = {}
                node["Node update"] = "Disable"
                json_object = json.dumps(node, indent=3)
                with open("files/node.json", "w") as f:
                    f.write(json_object)
                    f.close()
                return json.dumps(node)
            
            if (os.path.isfile("files/pm2.json") != True):
                pm2 = {}
                pm2["pm2 update"] = "Disable"
                json_object = json.dumps(pm2, indent=3)
                with open("files/pm2.json", "w") as f:
                    f.write(json_object)
                    f.close()
                return json.dumps(node)
        files()

        # Autolog
        # *** Datas *** #
        runtime = time.strftime("%Y-%m-%d - %H:%M:%S")
        sys = platform.platform()
        py = platform.python_version()

        # Check node
        # Check folder
        if (os.path.isfile("/usr/bin/node") == True or os.path.isfile("/usr/local/bin/node") == True):
            node_version = subprocess.check_output(['node', '-v'])
            debugLog()
        else:
            node_version = "NONE"
            debugLog()

        platform.system()

        # FIX: Node output
        # FIX: Check node available
        def runtimeLog():
            logFile = open(f"logs/autolog.log", "a")
            logFile.write(
                f"Launched time: {runtime}\nPlatform: {sys}\nPython version: {py}\nNode version: {node_version}\n")
            logFile.close()
        runtimeLog()

        # About Device
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
                # It doesn't work on windows
                if (platform.system() != "Windows"):
                    info['Processor'] = cpuinfo.get_cpu_info()['brand_raw']
                    info['RAM'] = str(
                        round(psutil.virtual_memory().total / (1024.0 ** 3)))+" GB"
                json_object = json.dumps(info, indent=3)
                with open("files/sysinfo.json", "w") as f:
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
                if (os.path.isfile("files/node.json") == True):
                    f = open('files/node.json')
                    data = json.load(f)
                    if (data["Node update"] == "Enable"):
                        subprocess.call("bash/node_update.sh")
                    f.close()
                subprocess.call("bash/system_update.sh")
            except Exception as e:
                debugLog()

        def openMyWebsite():
            webbrowser.open_new(r"https://richardneuvald.tk")

        def openMyGithub():
            webbrowser.open_new(r"https://github.com/NR-SkaterBoy")

        def supportedSystem():
            messagebox.showwarning("Supported Systems",
                                   "Ubuntu, Kali Linux, Raspbian, Sparky Linux")

        # TODO: Edit output
        def systemInfo():
            log = json.load(open("files/sysinfo.json", "r"))
            messagebox.showinfo("System Information", log)
        # systemInfo()

        def aboutSoftware():
            messagebox.showinfo("About this project", "Most PC users stick to Windows and are not willing to change to Linux because there are fewer GUI applications and they would need to learn the basic Linux commands. Moreover, most Linux-based systems get an update every week and some people think it is a waste of time to type the update commands.\n\nThis app may come handy for both beginners and advanced users because it is able to update the system by simply clicking a button. It supports over 10 different systems and has a built-in OS recognizer.\n\nVersion: Alpha 0.5")

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
                        "Last Log", f"{lastLog[0]}{lastLog[1]}{lastLog[2]}{lastLog[3]}")

        def settings():
            # TODO: Add help
            # FIX: Checkbutton style
            setting = Toplevel()
            setting.title("Settings")
            setting.geometry("300x300")
            setting.resizable(False, False)
            setting.grab_set()
            setting.configure(background="#383838")
            photo = PhotoImage(file="icons/setting.png")
            setting.iconphoto(False, photo)

            def save():
                # NODE
                if (add_node.get() == 1):
                    try:
                        node = {}
                        node["Node update"] = "Enable"
                        json_object = json.dumps(node, indent=3)
                        with open("files/node.json", "w") as f:
                            f.write(json_object)
                            f.close()
                        return json.dumps(node)
                    except Exception as e:
                        criticalLog()
                else:
                    try:
                        node = {}
                        node["Node update"] = "Disable"
                        json_object = json.dumps(node, indent=3)
                        with open("files/node.json", "w") as f:
                            f.write(json_object)
                            f.close()
                        return json.dumps(node)
                    except Exception as e:
                        criticalLog()

                # PM2
                if (add_pm2.get() == 1):
                    try:
                        pm2 = {}
                        pm2["pm2 update"] = "Enable"
                        json_object = json.dumps(pm2, indent=3)
                        with open("files/pm2.json", "w") as f:
                            f.write(json_object)
                            f.close()
                        return json.dumps(pm2)
                    except Exception as e:
                        criticalLog()
                        debugLog()
                else:
                    try:
                        pm2 = {}
                        pm2["pm2 update"] = "Disable"
                        json_object = json.dumps(pm2, indent=3)
                        with open("files/pm2.json", "w") as f:
                            f.write(json_object)
                            f.close()
                        return json.dumps(pm2)
                    except Exception as e:
                        criticalLog()

            # NODE
            node_strngs = open("files/node.json", "r")
            data = json.load(node_strngs)
            if (data["Node update"] == "Enable"):
                node_opts = 1
            else:
                node_opts = 0
            node_strngs.close()

            # PM2
            pm2_strngs = open("files/pm2.json", "r")
            data = json.load(pm2_strngs)
            if (data["pm2 update"] == "Enable"):
                pm2_opts = 1
            else:
                pm2_opts = 0
            pm2_strngs.close()

            add_node = IntVar(value=node_opts)
            add_pm2 = IntVar(value=pm2_opts)

            Label(setting, text="Modules", bg="#383838", fg="#FFFFFF", font=(
                'arial', 25, 'bold')).place(relx=0.5, rely=0.5, anchor=CENTER, y=-110)
            ttk.Checkbutton(setting, text="Node Update", command=save,
                            variable=add_node, onvalue=1, offvalue=0, width=15).place(relx=0.5, rely=0.5, anchor=CENTER, y=-60)
            ttk.Checkbutton(setting, text="pm2 Update", command=save,
                            variable=add_pm2, onvalue=1, offvalue=0, width=15).place(relx=0.5, rely=0.5, anchor=CENTER, y=-30)
        # settings()

        # Menu
        self.menubar = Menu(root, background='#ffffff', foreground='black',
                            activebackground='white', activeforeground='black')
        help = Menu(self.menubar, tearoff=0, background='#ffffff')
        help.add_command(label="Supported System", command=supportedSystem)
        help.add_command(label="About", command=aboutSoftware)
        help.add_command(label="About System", command=systemInfo)
        help.add_command(label="Settings", command=settings)
        help.add_command(label="Quit", command=quitLSU)
        self.menubar.add_cascade(label="Help", menu=help)
        userHelp = Menu(self.menubar, tearoff=0, background='#ffffff')
        # Not available yet
        userHelp.add_command(label="Questionnaire", command=openQuestionnaire)
        self.menubar.add_cascade(label="News", menu=userHelp)
        logs = Menu(self.menubar, tearoff=0, background='#ffffff')
        logs.add_command(label="Open last Log", command=openLastLog)
        self.menubar.add_cascade(label="Logger", menu=logs)
        # Title
        Label(root, text='System\nUpdater', bg="#181d31",
              fg="#ffffff", font=('arial', 40, 'bold')).place(x=60, y=25)
        # Btn of sysupdate
        Button(root, text='Update your system', bg='#F0F8FF', width=20, font=(
            'arial', 12, 'normal'), command=runningSystemUpdate).place(x=70, y=190)
        # Btn of my website
        Button(root, text='Visit my Website', bg='#F0F8FF', width=20, font=(
            'arial', 12, 'normal'), command=openMyWebsite).place(x=70, y=250)
        # Btn of my github profile
        Button(root, text='Follow me on Github', bg='#F0F8FF', width=20, font=(
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
        criticalLog()
        errorLog()
