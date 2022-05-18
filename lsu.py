#!/usr/bin/python3
# Developer/Author: NR-SkaterBoy
# Github: https://github.com/NR-SkaterBoy
# Website: https://richardneuvald.tk
# E-mail: nr.rick.dev@gmail.com
# Linux Systems source package Updater
# Version: Alpha 0.5

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
import webbrowser
import time
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
from PIL import ImageTk, Image
import platform
import language

# You won't get error message if you are on windows
if (platform.system() != "Windows"):
    import cpuinfo
    import psutil

# Set the file(s) rights
directory = "bash"
for file in os.listdir(directory):
    files = os.path.join(directory, file)
    os.chmod(files, stat.S_IRWXU)

# Terminal
# os.system("gnome-terminal 'bash -c \"sudo apt-get update; exec bash\"'") # It opens terminal

# LogTypes:

# () => task        @not necessary
# [] => function    @important          Do not use to gather information


def criticalLog(msg):
    logging.basicConfig(
        level=logging.CRITICAL,
        format="{asctime} {levelname} {message}",
        style='{',
        filename="logs/dev.log",
        filemode="a"
    )
    logging.critical(msg)


def errorLog(msg):
    logging.basicConfig(
        level=logging.ERROR,
        format="{asctime} {levelname} {message}",
        style='{',
        filename="logs/dev.log",
        filemode="a"
    )
    logging.error(msg)


def warningLog(msg):
    logging.basicConfig(
        level=logging.WARNING,
        format="{asctime} {levelname} {message}",
        style='{',
        filename="logs/dev.log",
        filemode="a"
    )
    logging.warning(msg)


def infoLog(msg):
    logging.basicConfig(
        level=logging.INFO,
        format="{asctime} {levelname} {message}",
        style='{',
        filename="logs/dev.log",
        filemode="a"
    )
    logging.info(msg)


def debugLog(msg):
    logging.basicConfig(
        level=logging.DEBUG,
        format="{asctime} {levelname} {message}",
        style='{',
        filename="logs/dev.log",
        filemode="a"
    )
    logging.debug(msg)

# LogFolder and neccesary file(s)


def createFolders():
    if (not os.path.isdir("logs")):
        os.mkdir(os.path.join("logs"))
    if (not os.path.isdir("files")):
        os.mkdir(os.path.join("files"))


createFolders()


def node_file():
    if (not os.path.isfile("files/node.json")):
        node = {}
        node["Node Update"] = "Disable"
        json_object = json.dumps(node, indent=3)
        with open("files/node.json", "w") as node_file:
            node_file.write(json_object)
        return json.dumps(node)


def pm2_file():
    if (not os.path.isfile("files/pm2.json")):
        pm2 = {}
        pm2["pm2 Update"] = "Disable"
        json_object = json.dumps(pm2, indent=3)
        with open("files/pm2.json", "w") as pm2_file:
            pm2_file.write(json_object)
        return json.dumps(pm2)


def forever_file():
    if (not os.path.isfile("files/forever.json")):
        forever = {}
        forever["forever Update"] = "Disable"
        json_object = json.dumps(forever, indent=3)
        with open("files/forever.json", "w") as forever_file:
            forever_file.write(json_object)
        return json.dumps(forever)


node_file()
pm2_file()
forever_file()


class Settings(tk.Toplevel):
    def __init__(self, parent):
        try:
            super().__init__(parent)

            self.geometry("300x300")
            self.title(language.s_window_name)
            self.resizable(False, False)
            self.configure(background="#383838")
            self.photo = PhotoImage(file="icons/setting.png")
            self.iconphoto(False, self.photo)

            def node_save():
                if (self.add_node.get() == 1):
                    try:
                        node = {}
                        node["Node Update"] = "Enable"
                        node_json_object = json.dumps(node, indent=3)
                        with open("files/node.json", "w") as node_file:
                            node_file.write(node_json_object)
                        return json.dumps(node)
                    except Exception as node_err:
                        errorLog(
                            f"Error writing node file (Enable) [node_save] - {node_err}")
                else:
                    try:
                        node = {}
                        node["Node Update"] = "Disable"
                        node_json_object = json.dumps(node, indent=3)
                        with open("files/node.json", "w") as node_file:
                            node_file.write(node_json_object)
                        return json.dumps(node)
                    except Exception as node_err:
                        errorLog(
                            "Error writing node file (Disable) [node_save] - {node_err} ")

            def pm2_save():
                if (self.add_pm2.get() == 1):
                    try:
                        pm2 = {}
                        pm2["pm2 Update"] = "Enable"
                        pm2_json_object = json.dumps(pm2, indent=3)
                        with open("files/pm2.json", "w") as pm2_file:
                            pm2_file.write(pm2_json_object)
                        return json.dumps(pm2)
                    except Exception as pm2_err:
                        errorLog(
                            f"Error writing pm2 file (Enable) [pm2_save] - {pm2_err}")
                else:
                    try:
                        pm2 = {}
                        pm2["pm2 Update"] = "Disable"
                        pm2_json_object = json.dumps(pm2, indent=3)
                        with open("files/pm2.json", "w") as pm2_file:
                            pm2_file.write(pm2_json_object)
                        return json.dumps(pm2)
                    except Exception as pm2_err:
                        errorLog(
                            f"Error writing pm2 file (Disable) [pm2_save] - {pm2_err}")

            def forever_save():
                if (self.add_forever.get() == 1):
                    try:
                        forever = {}
                        forever["forever Update"] = "Enable"
                        forever_json_object = json.dumps(forever, indent=3)
                        with open("files/forever.json", "w") as forever_file:
                            forever_file.write(forever_json_object)
                        return json.dumps(forever)
                    except Exception as forever_err:
                        errorLog(
                            f"Error writing forever file (Enable) [forever_save] - {forever_err}")
                else:
                    try:
                        forever = {}
                        forever["forever Update"] = "Disable"
                        forever_json_object = json.dumps(forever, indent=3)
                        with open("files/forever.json", "w") as forever_file:
                            forever_file.write(forever_json_object)
                        return json.dumps(forever)
                    except Exception as forever_err:
                        errorLog(
                            f"Error writing forever file (Disable) [forever_save] - {forever_err}")
                    finally:
                        if (not os.path.isfile("files/forever.json")):
                            self.destroy()
                            messagebox.showerror(
                                language.t_error, language.d_restart)

            # NODE
            self.node_strngs = open("files/node.json", "r")
            self.data = json.load(self.node_strngs)
            if (self.data["Node Update"] == "Enable"):
                self.node_opts = 1
            else:
                self.node_opts = 0
            self.node_strngs.close()

            # PM2
            self.pm2_strngs = open("files/pm2.json", "r")
            self.data = json.load(self.pm2_strngs)
            if (self.data["pm2 Update"] == "Enable"):
                self.pm2_opts = 1
            else:
                self.pm2_opts = 0
            self.pm2_strngs.close()

            # Forever
            self.forever_strngs = open("files/forever.json", "r")
            self.data = json.load(self.forever_strngs)
            if (self.data["forever Update"] == "Enable"):
                self.forever_opts = 1
            else:
                self.forever_opts = 0
            self.forever_strngs.close()

            def writeLanguageFile():
                if (self.lang.get() == 1):
                    try:
                        language_file = {}
                        language_file["Language"] = "English"
                        language_file_json_object = json.dumps(
                            language_file, indent=3)
                        with open("files/language.json", "w") as language_file:
                            language_file.write(language_file_json_object)
                        messagebox.showinfo(
                            language.t_notify, language.d_not_res)
                        return json.dumps(language_file)
                    except Exception as language_file_err:
                        errorLog(
                            f"Error writing language_file file (Enable) [language_file_save] - {language_file_err}")
                else:
                    try:
                        language_file = {}
                        language_file["Language"] = "Hungary"
                        language_file_json_object = json.dumps(
                            language_file, indent=3)
                        with open("files/language.json", "w") as language_file:
                            language_file.write(language_file_json_object)
                            messagebox.showinfo(
                                language.t_notify, language.d_not_res)
                        return json.dumps(language_file)
                    except Exception as language_file_err:
                        errorLog(
                            f"Error writing language_file file (Disable) [language_file_save] - {language_file_err}")
                    finally:
                        if (not os.path.isfile("files/language.json")):
                            self.destroy()
                            messagebox.showerror(
                                language.t_error, language.d_restart)

            ############################################
            # Button variables
            self.add_node = IntVar(value=self.node_opts)
            self.add_pm2 = IntVar(value=self.pm2_opts)
            self.add_forever = IntVar(value=self.forever_opts)
            self.lang = IntVar(value=None)
            ############################################

            # Add value to lang
            self.read_lang_file = open("files/language.json", "r")
            self.getLang = json.load(self.read_lang_file)
            if self.getLang["Language"] == "English":
                self.lang.set(1)
            elif self.getLang["Language"] == "Hungary":
                self.lang.set(2)

            Label(self, text=language.s_title, bg="#383838", fg="#FFFFFF", font=(
                'arial', 25, 'bold')).place(relx=0.5, rely=0.5, anchor=CENTER, y=-110)
            ttk.Checkbutton(self, text=language.s_node, command=node_save,
                            variable=self.add_node, onvalue=1, offvalue=0, width=15).place(relx=0.5, rely=0.5, anchor=CENTER, y=-60)
            ttk.Checkbutton(self, text=language.s_pm2, command=pm2_save,
                            variable=self.add_pm2, onvalue=1, offvalue=0, width=15).place(relx=0.5, rely=0.5, anchor=CENTER, y=-30)
            # ttk.Checkbutton(self, text="Forever", command=forever_save, variable=add_forever,
            #                 onvalue=1, offvalue=0, width=15).place(relx=0.5, rely=0.5, anchor=CENTER)

            # Language
            Label(self, text=language.s_lang_title, bg="#383838", fg="#FFFFFF", font=(
                'arial', 25, 'bold')).place(relx=0.5, rely=0.5, anchor=CENTER, y=30)

            lang_en = Radiobutton(
                self, text=language.s_lang_en, variable=self.lang, value=1, width=15, command=writeLanguageFile)
            lang_en.place(relx=0.5, rely=0.5, anchor=CENTER, y=70)
            lang_hu = Radiobutton(
                self, text=language.s_lang_hu, variable=self.lang, value=2, width=15, command=writeLanguageFile)
            lang_hu.place(relx=0.5, rely=0.5, anchor=CENTER, y=100)

            def aboutSettings():
                messagebox.showinfo(language.t_howtouse, language.d_howtouse)

            def aboutNode():
                webbrowser.open_new(r"https://nodejs.org/en/about/")

            def aboutPm2():
                webbrowser.open_new(r"https://pm2.keymetrics.io/")

            menu = tk.Menu(self)
            self.configure(menu=menu)
            menubar = Menu(self, background='#ffffff', foreground='black',
                           activebackground='white', activeforeground='black')

            help = Menu(menubar, tearoff=0, background='#ffffff')
            help.add_command(label=language.s_h_whatisit,
                             command=aboutSettings)
            menu.add_cascade(label=language.s_h_category, menu=help)

            modules = Menu(menubar, tearoff=0, background='#ffffff')
            modules.add_command(label=language.s_m_node, command=aboutNode)
            modules.add_command(label=language.s_m_pm2, command=aboutPm2)
            menu.add_cascade(label=language.s_m_category, menu=modules)
        except Exception as settings_err:
            criticalLog(
                f"An error occurred! The following file(s) could not be found in the settings [settings] - {settings_err}")


class LSU(tk.Tk):
    def __init__(self):
        super().__init__(className="Linux System Updater")

        self.title(language.m_app_name)
        self.geometry("800x450+50+50")
        self.resizable(True, True)
        self.minsize(width=800, height=450)
        self.configure(background="#181d31")
        # self.iconbitmap("icons/lsu.ico")
        self.photo = PhotoImage(file="icons/lsu.png")
        self.iconphoto(False, self.photo)

        # Autolog
        # *** Data *** #
        self.runtime = time.strftime("%Y-%m-%d - %H:%M:%S")
        self.sys = platform.platform()
        self.py = platform.python_version()

        # Check node folder
        if (os.path.isfile("/usr/bin/node") or os.path.isfile("/usr/local/bin/node")):
            self.get_node_version = subprocess.check_output(['node', '-v'])
            self.node_version = self.get_node_version[:8]
        else:
            self.node_version = "NONE"

        def runtimeLog():
            logFile = open(f"logs/runtime.log", "a")
            logFile.write(
                f"Launched time: {self.runtime}\nPlatform: {self.sys}\nPython version: {self.py}\nNode version: {self.node_version}\n\n")
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
                with open("files/sysinfo.json", "w") as sysinfo_file:
                    sysinfo_file.write(json_object)
                return json.dumps(info)
            except Exception as sysinfo_err:
                errorLog(
                    f"An error occurred while retrieving system information [getSystemInfo] - {sysinfo_err}")
        getSystemInfo()

        def runningSystemUpdate():
            try:
                if (os.path.isfile("files/node.json")):
                    node = open('files/node.json')
                    node_data = json.load(node)
                    if (node_data["Node Update"] == "Enable"):
                        subprocess.call("bash/node_update.sh")
                    node.close()

                if (os.path.isfile("files/pm2.json")):
                    pm2 = open('files/pm2.json')
                    pm2_data = json.load(pm2)
                    if (pm2_data["pm2 Update"] == "Enable"):
                        subprocess.call("bash/pm2_update.sh")
                    pm2.close()

                subprocess.call("bash/system_update.sh")
            except Exception as upd_err:
                errorLog(
                    f"An error occurred while updating the system [runningSystemUpdate] - {upd_err}")

        def openMyWebsite():
            webbrowser.open_new(r"https://richardneuvald.tk")

        def openMyGithub():
            webbrowser.open_new(r"https://github.com/NR-SkaterBoy")

        def supportedSystem():
            messagebox.showwarning(language.t_sup_sys,
                                   "Ubuntu, Kali Linux, Raspbian, Sparky Linux")

        def systemInfo():
            log = json.load(open("files/sysinfo.json", "r"))
            sysinfo = (f"Platform: {log['Platform']}\nPlatform-release: {log['Platform-release']}\nPlatform-version: {log['Platform-version']}\nArchitecture: {log['Architecture']}\nHostname: {log['Hostname']}\nIP-address: {log['IP-address']}\nMAC-address: {log['MAC-address']}\nProcessor: {log['Processor']}\nRAM: {log['RAM']}")
            messagebox.showinfo(language.t_sys_inf, sysinfo)
        # systemInfo()

        def aboutSoftware():
            messagebox.showinfo(language.t_about, language.d_about)

        def quitLSU():
            logFile = open(f"logs/runtime.log", "a")
            logFile.write(
                f"Exit time: {self.runtime}\n\n")
            logFile.close()
            self.protocol("WM_DELETE_WINDOW", self.quit())

        def openQuestionnaire():
            webbrowser.open_new(r"https://forms.gle/Xb5kY6cajjvRHTNB7")

        def openLastLog():
            lastLog = []
            if (not os.path.isfile("logs/runtime.log")):
                messagebox.showerror(language.t_error, "No log file")
            else:
                with open("logs/runtime.log", encoding="utf-8") as lastlog_file:
                    for line in (lastlog_file.readlines()[-4:]):
                        lastLog.append(line)
                    messagebox.showinfo(language.t_lastlog,
                                        "{}{}{}{}".format(*lastLog))

        def openLogFile():
            try:
                os.system("gedit logs/runtime.log")
            except Exception as openLog:
                errorLog(
                    f"Error occured while opening the file [logfile] - {openLog}")

        # Menu
        self.menubar = Menu(self, background='#ffffff', foreground='black',
                            activebackground='white', activeforeground='black')
        help = Menu(self.menubar, tearoff=0, background='#ffffff')
        help.add_command(label=language.m_h_sup_sys, command=supportedSystem)
        help.add_command(label=language.m_h_about, command=aboutSoftware)
        help.add_command(label=language.m_h_settings,
                         command=self.open_settings)
        help.add_command(label=language.m_h_quit, command=quitLSU)
        self.menubar.add_cascade(label=language.m_h_category, menu=help)
        userHelp = Menu(self.menubar, tearoff=0, background='#ffffff')
        # Not available yet
        userHelp.add_command(label=language.m_n_questionaire,
                             command=openQuestionnaire)
        self.menubar.add_cascade(label=language.m_n_category, menu=userHelp)
        info = Menu(self.menubar, tearoff=0, background='#ffffff')
        info.add_command(label=language.m_i_log_file, command=openLogFile)
        info.add_command(label=language.m_i_last_log, command=openLastLog)
        info.add_command(label=language.m_i_system, command=systemInfo)
        self.menubar.add_cascade(label=language.m_i_category, menu=info)
        # Title
        Label(self, text=language.m_app_title, bg="#181d31",
              fg="#ffffff", font=('arial', 40, 'bold')).place(x=60, y=25)
        # Btn of sysupdate
        Button(self, text=language.m_upd_btn, bg='#F0F8FF', width=25, font=(
            'arial', 12, 'normal'), command=runningSystemUpdate).place(x=70, y=190)
        # Btn of my website
        Button(self, text=language.m_web_btn, bg='#F0F8FF', width=25, font=(
            'arial', 12, 'normal'), command=openMyWebsite).place(x=70, y=250)
        # Btn of my github profile
        Button(self, text=language.m_git_btn, bg='#F0F8FF', width=25, font=(
            'arial', 12, 'normal'), command=openMyGithub).place(x=70, y=310)
        # Pictures
        self.lsu_pic = Canvas(self, height=470, width=449,
                              bg="#181d31", borderwidth=0, highlightthickness=0)
        self.picture_file = PhotoImage(file='pictures/lsu.png')
        self.lsu_pic.create_image(470, 0, anchor=NE, image=self.picture_file)
        self.lsu_pic.place(x=310, y=84)
        # Menu
        self.config(menu=self.menubar)

    def open_settings(self):
        settings = Settings(self)
        settings.grab_set()


if __name__ == "__main__":
    try:
        lsu = LSU()
        lsu.mainloop()
    except Exception as startup_err:
        criticalLog(
            f"An error occurred while starting the application - {startup_err}")
