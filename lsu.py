#!/usr/bin/python3
# Developer/Author: NR-SkaterBoy
# Github: https://github.com/NR-SkaterBoy
# Website: https://richardneuvald.tk
# E-mail: nr.rick.dev@gmail.com
# Linux Systems source package Updater
# Version: Alpha 0.5


# Import modules
import os
import socket
import re
import uuid
import json
import stat
import subprocess
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

# Import local file
import language
import logger

# Set the file(s) rights
directory = "bash"
for file in os.listdir(directory):
    files = os.path.join(directory, file)
    os.chmod(files, stat.S_IRWXU)

# LogFolder and neccesary file(s) [Modules]
if (not os.path.isdir("logs")):
    os.mkdir(os.path.join("logs"))
if (not os.path.isdir("files")):
    os.mkdir(os.path.join("files"))


if (not os.path.isfile("files/modules.json")):
    modules = {}
    modules["node update"] = "Disable"
    modules["pm2 update"] = "Disable"
    modules["forever update"] = "Disable"
    json_object = json.dumps(modules, indent=3)
    with open("files/modules.json", "w") as modules_file:
        modules_file.write(json_object)
    json.dumps(modules)


if (not os.path.isfile("files/app.json")):
    app = {}
    app["language"] = "English"
    app["editor"] = "nano"
    json_object = json.dumps(app, indent=3)
    with open("files/app.json", "w") as app_file:
        app_file.write(json_object)
    json.dumps(app)


# Linux editors and installed editor(s)
EDITORS = [
    "code",     "subl"
    "atom",     "geany",
    "gedit",    "nano",
    "vi",       "vim",
    "gvim",     "notepad-plus-plus",
    "emacs",    "pico",
    "bluefish", "kate",
]

AVAILABLE_EDITORS = []

# Check all available editors
for editor in EDITORS:
    iseditor = subprocess.run(["which", f"{editor}"])
    if (iseditor.returncode == 0):
        AVAILABLE_EDITORS.append(editor)

# Files
modules_file = "files/modules.json"
application_file = "files/app.json"

# Launched time
l_time = ""


class Settings(tk.Toplevel):
    def __init__(self, parent):
        try:
            super().__init__(parent)

            self.geometry("500x300")
            self.title(language.settings)
            self.resizable(False, True)
            self.configure(background="#383838")
            self.photo = PhotoImage(file="icons/setting.png")
            self.iconphoto(False, self.photo)

            def node_save():
                if (self.add_node.get() == 1):
                    try:
                        with open(modules_file, "r+") as node_upd:
                            node = json.load(node_upd)
                            node['node update'] = "Enable"
                            node_upd.seek(0)
                            json.dump(node, node_upd, indent=3)
                            node_upd.truncate()
                    except Exception as node_err:
                        logger.errorLog(
                            f"Error writing node file (Enable) [node_save] - {node_err}")
                else:
                    try:
                        with open(modules_file, "r+") as node_upd:
                            node = json.load(node_upd)
                            node['node update'] = "Enable"
                            node_upd.seek(0)
                            json.dump(node, node_upd, indent=3)
                            node_upd.truncate()
                    except Exception as node_err:
                        logger.errorLog(
                            f"Error writing node file (Enable) [node_save] - {node_err}")

            def pm2_save():
                if (self.add_pm2.get() == 1):
                    try:
                        with open(modules_file, "r+") as pm2_upd:
                            pm2 = json.load(pm2_upd)
                            pm2['pm2 update'] = "Enable"
                            pm2_upd.seek(0)
                            json.dump(pm2, pm2_upd, indent=3)
                            pm2_upd.truncate()
                    except Exception as pm2_err:
                        logger.errorLog(
                            f"Error writing pm2 file (Enable) [pm2_save] - {pm2_err}")
                else:
                    try:
                        with open(modules_file, "r+") as pm2_upd:
                            pm2 = json.load(pm2_upd)
                            pm2['pm2 update'] = "Enable"
                            pm2_upd.seek(0)
                            json.dump(pm2, pm2_upd, indent=3)
                            pm2_upd.truncate()
                    except Exception as pm2_err:
                        logger.errorLog(
                            f"Error writing pm2 file (Enable) [pm2_save] - {pm2_err}")

            def forever_save():
                if (self.add_forever.get() == 1):
                    try:
                        with open(modules_file, "r+") as forever_upd:
                            forever = json.load(forever_upd)
                            forever['forever update'] = "Enable"
                            forever_upd.seek(0)
                            json.dump(forever, forever_upd, indent=3)
                            forever_upd.truncate()
                    except Exception as forever_err:
                        logger.errorLog(
                            f"Error writing forever file (Enable) [forever_save] - {forever_err}")
                else:
                    try:
                        with open(modules_file, "r+") as forever_upd:
                            forever = json.load(forever_upd)
                            forever['forever update'] = "Enable"
                            forever_upd.seek(0)
                            json.dump(forever, forever_upd, indent=3)
                            forever_upd.truncate()
                    except Exception as forever_err:
                        logger.errorLog(
                            f"Error writing forever file (Enable) [forever_save] - {forever_err}")

                        # NODE
            self.node_strngs = open("files/modules.json", "r")
            self.data = json.load(self.node_strngs)
            if (self.data["node update"] == "Enable"):
                self.node_opts = 1
            else:
                self.node_opts = 0
            self.node_strngs.close()

            # PM2
            self.pm2_strngs = open("files/modules.json", "r")
            self.data = json.load(self.pm2_strngs)
            if (self.data["pm2 update"] == "Enable"):
                self.pm2_opts = 1
            else:
                self.pm2_opts = 0
            self.pm2_strngs.close()

            # Forever
            self.forever_strngs = open("files/modules.json", "r")
            self.data = json.load(self.forever_strngs)
            if (self.data["forever update"] == "Enable"):
                self.forever_opts = 1
            else:
                self.forever_opts = 0
            self.forever_strngs.close()

            def setLanguage():
                if (self.lang.get() == 1):
                    try:
                        with open(application_file, "r+") as lang_upd:
                            lang = json.load(lang_upd)
                            lang['language'] = "English"
                            lang_upd.seek(0)
                            json.dump(lang, lang_upd, indent=3)
                            lang_upd.truncate()
                            if (not lang["language"] == "English"):
                                messagebox.showinfo(
                                    language.tm_notify, language.dm_lang_res)
                    except Exception as language_file_err:
                        logger.errorLog(
                            f"Error writing language_file file (Enable) [language_file_save] - {language_file_err}")
                else:
                    try:
                        with open(application_file, "r+") as lang_upd:
                            lang = json.load(lang_upd)
                            lang['language'] = "Hungary"
                            lang_upd.seek(0)
                            json.dump(lang, lang_upd, indent=3)
                            lang_upd.truncate()
                            if (not lang["language"] == "Hungary"):
                                messagebox.showinfo(
                                    language.t_notify, language.dm_lang_res)
                    except Exception as language_file_err:
                        logger.errorLog(
                            f"Error writing language_file file (Disable) [language_file_save] - {language_file_err}")
                    finally:
                        if (not os.path.isfile("files/app.json")):
                            self.destroy()
                            messagebox.showerror(
                                language.tm_error, language.dm_restart)

            ############################################
            # Button variables
            self.add_node = IntVar(value=self.node_opts)
            self.add_pm2 = IntVar(value=self.pm2_opts)
            self.add_forever = IntVar(value=self.forever_opts)
            self.lang = IntVar(value=None)
            self.editor = IntVar(value=None)
            ############################################

            # Add value to lang
            self.read_lang_file = open("files/app.json", "r")
            self.getLang = json.load(self.read_lang_file)
            if self.getLang["language"] == "English":
                self.lang.set(1)
            elif self.getLang["language"] == "Hungary":
                self.lang.set(2)

            read_code_editor = open("files/app.json", "r")
            getEditor = json.load(read_code_editor)
            match getEditor["editor"]:
                case "code": self.editor.set(3)
                case "subl": self.editor.set(4)
                case "atom": self.editor.set(5)
                case "geany": self.editor.set(6)
                case "gedit": self.editor.set(7)
                case "nano": self.editor.set(8)
                case "vi": self.editor.set(9)
                case "vim": self.editor.set(10)
                case "gvim": self.editor.set(11)
                case "notepad-plus-plus": self.editor.set(12)
                case "emacs": self.editor.set(13)
                case "pico": self.editor.set(14)
                case "bluefish": self.editor.set(15)
                case "kate": self.editor.set(16)

            def writeEditor(new_editor):
                with open(application_file, "r+") as default_editor:
                    editor = json.load(default_editor)
                    editor['editor'] = new_editor
                    default_editor.seek(0)
                    json.dump(editor, default_editor, indent=3)
                    default_editor.truncate()

            def setEditor():
                match self.editor.get():
                    case 3: writeEditor("code")
                    case 4: writeEditor("subl")
                    case 5: writeEditor("atom")
                    case 6: writeEditor("geany")
                    case 7: writeEditor("gedit")
                    case 8: writeEditor("nano")
                    case 9: writeEditor("vi")
                    case 10: writeEditor("vim")
                    case 11: writeEditor("gvim")
                    case 12: writeEditor("notepad-plus-plus")
                    case 13: writeEditor("emacs")
                    case 14: writeEditor("pico")
                    case 15: writeEditor("bluefish")
                    case 16: writeEditor("kate")

            Label(self, text=language.t_modul, bg="#383838", fg="#FFFFFF", font=(
                'arial', 25, 'bold')).place(relx=0.5, rely=0.5, anchor=CENTER, y=-110, x=-140)
            ttk.Checkbutton(self, text=language.m_node, command=node_save,
                            variable=self.add_node, onvalue=1, offvalue=0, width=15).place(relx=0.5, rely=0.5, anchor=CENTER, y=-60, x=-140)
            ttk.Checkbutton(self, text=language.m_pm2, command=pm2_save,
                            variable=self.add_pm2, onvalue=1, offvalue=0, width=15).place(relx=0.5, rely=0.5, anchor=CENTER, y=-30, x=-140)
            # ttk.Checkbutton(self, text="Forever", command=forever_save, variable=add_forever,
            #                 onvalue=1, offvalue=0, width=15).place(relx=0.5, rely=0.5, anchor=CENTER)

            # Language
            Label(self, text=language.t_language, bg="#383838", fg="#FFFFFF", font=(
                'arial', 25, 'bold')).place(relx=0.5, rely=0.5, anchor=CENTER, y=30, x=-140)

            lang_en = Radiobutton(
                self, text=language.l_eng, variable=self.lang, value=1, width=15, command=setLanguage)
            lang_en.place(relx=0.5, rely=0.5, anchor=CENTER, y=70, x=-140)
            lang_hu = Radiobutton(
                self, text=language.l_hu, variable=self.lang, value=2, width=15, command=setLanguage)
            lang_hu.place(relx=0.5, rely=0.5, anchor=CENTER, y=100, x=-140)

            Label(self, text=language.t_editor, bg="#383838", fg="#FFFFFF", font=(
                'arial', 25, 'bold')).place(relx=0.5, rely=0.5, anchor=CENTER, y=-110, x=100)

            editor_y = -90
            for editor in AVAILABLE_EDITORS:
                editor_y += 30
                match editor:
                    case "code": Radiobutton(self, text="VSCode", variable=self.editor, value=3, width=15, command=setEditor).place(relx=0.5, rely=0.5, anchor=CENTER, y=editor_y, x=100)
                    case "subl": Radiobutton(self, text="Subl", variable=self.editor, value=4, width=15, command=setEditor).place(relx=0.5, rely=0.5, anchor=CENTER, y=editor_y, x=100)
                    case "atom": Radiobutton(self, text="Atom", variable=self.editor, value=5, width=15, command=setEditor).place(relx=0.5, rely=0.5, anchor=CENTER, y=editor_y, x=100)
                    case "geany": Radiobutton(self, text="Geany", variable=self.editor, value=6, width=15, command=setEditor).place(relx=0.5, rely=0.5, anchor=CENTER, y=editor_y, x=100)
                    case "gedit": Radiobutton(self, text="Gedit", variable=self.editor, value=7, width=15, command=setEditor).place(relx=0.5, rely=0.5, anchor=CENTER, y=editor_y, x=100)
                    case "nano": Radiobutton(self, text="Nano", variable=self.editor, value=8, width=15, command=setEditor).place(relx=0.5, rely=0.5, anchor=CENTER, y=editor_y, x=100)
                    case "vi": Radiobutton(self, text="Vi", variable=self.editor, value=9, width=15, command=setEditor).place(relx=0.5, rely=0.5, anchor=CENTER, y=editor_y, x=100)
                    case "vim": Radiobutton(self, text="Vim", variable=self.editor, value=10, width=15, command=setEditor).place(relx=0.5, rely=0.5, anchor=CENTER, y=editor_y, x=100)
                    case "gvim": Radiobutton(self, text="Gvim", variable=self.editor, value=11, width=15, command=setEditor).place(relx=0.5, rely=0.5, anchor=CENTER, y=editor_y, x=100)
                    case "notepad-plus-plus": Radiobutton(self, text="Notepad++", variable=self.editor, value=12, width=15, command=setEditor).place(relx=0.5, rely=0.5, anchor=CENTER, y=editor_y, x=100)
                    case "emacs": Radiobutton(self, text="Emacs", variable=self.editor, value=13, width=15, command=setEditor).place(relx=0.5, rely=0.5, anchor=CENTER, y=editor_y, x=100)
                    case "pico": Radiobutton(self, text="Pico", variable=self.editor, value=14, width=15, command=setEditor).place(relx=0.5, rely=0.5, anchor=CENTER, y=editor_y, x=100)
                    case "bluefish": Radiobutton(self, text="Bluefish", variable=self.editor, value=15, width=15, command=setEditor).place(relx=0.5, rely=0.5, anchor=CENTER, y=editor_y, x=100)
                    case "kate": Radiobutton(self, text="Kate", variable=self.editor, value=16, width=15, command=setEditor).place(relx=0.5, rely=0.5, anchor=CENTER, y=editor_y, x=100)

            def aboutSettings():
                messagebox.showinfo(language.tm_howtouse, language.dm_howtouse)

            def aboutNode():
                webbrowser.open(r"https://nodejs.org/en/about/")

            def aboutPm2():
                webbrowser.open(r"https://pm2.keymetrics.io/")

            menu = tk.Menu(self)
            self.configure(menu=menu)
            menubar = Menu(self, background='#ffffff', foreground='black',
                           activebackground='white', activeforeground='black')

            help = Menu(menubar, tearoff=0, background='#ffffff')
            help.add_command(label=language.sm_whatis,
                             command=aboutSettings)
            menu.add_cascade(label=language.ml_stngs_menu, menu=help)

            modules = Menu(menubar, tearoff=0, background='#ffffff')
            modules.add_command(label=language.sm_node, command=aboutNode)
            modules.add_command(label=language.sm_pm2, command=aboutPm2)
            menu.add_cascade(label=language.ml_stngs_modul, menu=modules)

        except Exception as settings_err:
            logger.criticalLog(
                f"An error occurred! The following file(s) could not be found in the settings [settings] - {settings_err}")


class LSU(tk.Tk):
    def __init__(self):
        super().__init__(className="Linux System Updater")

        self.title(language.lsu)
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

        l_time = self.runtime

        def runtimeLog():
            log_data = {
                self.runtime: {
                    "Platform": self.sys,
                    "Python version": self.py,
                    "Node version": self.node_version.decode("utf-8")
                }
            }
            if (not os.path.isfile("logs/runtime.json")):
                with open("logs/runtime.json", "w") as runtime:
                    json.dump([log_data], runtime, indent=3)
            else:
                with open("logs/runtime.json", "r") as file:
                    data = json.load(file)
                data.append(log_data)
                with open("logs/runtime.json", "w") as file:
                    json.dump(data, file, indent=3)
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
                logger.errorLog(
                    f"An error occurred while retrieving system information [getSystemInfo] - {sysinfo_err}")
        getSystemInfo()

        def runningSystemUpdate():
            with open(modules_file, "r") as modules:
                data = json.load(modules)
            try:
                # LSU package updater
                subprocess.call("bash/lsu_update.sh")

                # Node
                if (data["node update"] == "Enable"):
                    subprocess.call("bash/node_update.sh")

                # PM2
                if (data["pm2 update"] == "Enable"):
                    subprocess.call("bash/pm2_update.sh")

                # System update
                subprocess.call("bash/system_update.sh")
            except Exception as upd_err:
                logger.errorLog(
                    f"An error occurred while updating the system [runningSystemUpdate] - {upd_err}")

        def openMyWebsite():
            webbrowser.open(r"https://richardneuvald.tk")

        def openMyGithub():
            webbrowser.open(r"https://github.com/NR-SkaterBoy")

        def supportedSystem():
            messagebox.showwarning(language.tm_supsys,
                                   "Ubuntu, Kali Linux, Raspbian, Sparky Linux")

        def systemInfo():
            log = json.load(open("files/sysinfo.json", "r"))
            sysinfo = (f"Platform: {log['Platform']}\nPlatform-release: {log['Platform-release']}\nPlatform-version: {log['Platform-version']}\nArchitecture: {log['Architecture']}\nHostname: {log['Hostname']}\nIP-address: {log['IP-address']}\nMAC-address: {log['MAC-address']}\nProcessor: {log['Processor']}\nRAM: {log['RAM']}")
            messagebox.showinfo(language.tm_sysinfo, sysinfo)
        # systemInfo()

        def aboutSoftware():
            messagebox.showinfo(language.tm_about, language.dm_about)

        def quitLSU():
            logFile = open(f"logs/runtime.log", "a")
            logFile.write(
                f"Exit time: {self.runtime}\n\n")
            logFile.close()
            self.protocol("WM_DELETE_WINDOW", self.quit())

        def openQuestionnaire():
            webbrowser.open(r"https://forms.gle/Xb5kY6cajjvRHTNB7")

        def openLastLog():
            lastlog_file = open("logs/runtime.json")
            data = json.load(lastlog_file)
            plat = data[-1][f"{l_time}"]["Platform"]
            py = data[-1][f"{l_time}"]["Python version"]
            node = data[-1][f"{l_time}"]["Node version"]
            messagebox.showinfo(f"{language.tm_lastlog} - {l_time}",
                                "Platform: {}\nNode: {}\nPython: {}".format(plat, node, py))

        def openLogFile():
            try:
                read_editor = open("files/app.json", "r")
                def_editor = json.load(read_editor)
                os.system(f"{def_editor['editor']} logs/runtime.json")
            except Exception as openLog:
                logger.errorLog(
                    f"Error occured while opening the file [logfile] - {openLog}")

        def openInstagram():
            webbrowser.open(r"https://www.instagram.com/richardneuvald/")

        def openTwitter():
            webbrowser.open(r"https://twitter.com/richardneuvald")

        def openPayPal():
            webbrowser.open(r"https://www.paypal.com/paypalme/richardneuvald")

        def openBuymeacoffee():
            webbrowser.open(r"https://www.buymeacoffee.com/richardneuvald")

        # Menu
        self.menubar = Menu(self, background='#ffffff', foreground='black',
                            activebackground='white', activeforeground='black')
        help = Menu(self.menubar, tearoff=0, background='#ffffff')
        help.add_command(label=language.lm_supsys, command=supportedSystem)
        help.add_command(label=language.lm_about, command=aboutSoftware)
        help.add_command(label=language.lm_settings,
                         command=self.open_settings)
        help.add_command(label=language.lm_exit, command=quitLSU)
        self.menubar.add_cascade(label=language.ml_lsu_menu, menu=help)
        userHelp = Menu(self.menubar, tearoff=0, background='#ffffff')
        # Not available yet
        userHelp.add_command(label=language.ln_questionaire,
                             command=openQuestionnaire)
        self.menubar.add_cascade(label=language.ml_lsu_news, menu=userHelp)
        info = Menu(self.menubar, tearoff=0, background='#ffffff')
        info.add_command(label=language.li_log_file, command=openLogFile)
        info.add_command(label=language.li_last_log, command=openLastLog)
        info.add_command(label=language.li_sysinfo, command=systemInfo)
        self.menubar.add_cascade(label=language.ml_lsu_info, menu=info)
        # Title
        Label(self, text=language.t_systm_updater, bg="#181d31",
              fg="#ffffff", font=('arial', 40, 'bold')).place(x=60, y=25)
        # Btn of sysupdate
        Button(self, text=language.btn_lsu_sys, bg='#F0F8FF', width=25, font=(
            'arial', 12, 'normal'), command=runningSystemUpdate).place(x=70, y=190)
        # Btn of my website
        Button(self, text=language.btn_lsu_web, bg='#F0F8FF', width=25, font=(
            'arial', 12, 'normal'), command=openMyWebsite).place(x=70, y=250)
        # Btn of my github profile
        Button(self, text=language.btn_lsu_github, bg='#F0F8FF', width=25, font=(
            'arial', 12, 'normal'), command=openMyGithub).place(x=70, y=310)
        # Pictures
        self.lsu_pic = Canvas(self, height=470, width=449,
                              bg="#181d31", borderwidth=0, highlightthickness=0)
        self.picture_file = PhotoImage(file='pictures/lsu.png')
        self.lsu_pic.create_image(470, 0, anchor=NE, image=self.picture_file)
        self.lsu_pic.place(x=310, y=84)
        # Support & Media
        ### Instagram ###
        self.insta = PhotoImage(file="pictures/instagram.png")
        Button(self, image=self.insta, width=25, height=25, bg="#181d31",
               borderwidth=0, command=openInstagram).place(x=30, y=410)
        ### Twitter ###
        self.twitter = PhotoImage(file="pictures/twitter.png")
        Button(self, image=self.twitter, width=25, height=25, bg="#181d31",
               borderwidth=0, command=openTwitter).place(x=60, y=410)
        ### PayPal ###
        self.paypal = PhotoImage(file="pictures/paypal.png")
        Button(self, image=self.paypal, width=25, height=25, bg="#181d31",
               borderwidth=0, command=openPayPal).place(x=90, y=410)
        ### Buymeacoffee ###
        self.coffee = PhotoImage(file="pictures/coffee-cup.png")
        Button(self, image=self.coffee, width=25, height=25, bg="#181d31",
               borderwidth=0, command=openBuymeacoffee).place(x=120, y=410)
        # Menu
        self.config(menu=self.menubar)

    def open_settings(self):
        self.settings = Settings(self)
        self.settings.grab_set()


if __name__ == "__main__":
    try:
        lsu = LSU()
        lsu.mainloop()
    except Exception as startup_err:
        logger.criticalLog(
            f"An error occurred while starting the application - {startup_err}")
