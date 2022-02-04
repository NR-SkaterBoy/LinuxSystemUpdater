# Import modules
import subprocess
import os, sys, stat
import tkinter as tk

# Set the files right
os.chmod("./bash/source_update.sh", stat.S_IRWXU)
os.chmod("./bash/system_update.sh", stat.S_IRWXU)

# Import os-update script
def running_os_update_script():
    subprocess.call("./bash/system_update.sh")

# Import source update
def running_source_update_script():
    subprocess.call("./bash/source_update.sh")

# Colors
background_color = "#050505"
btn_color = "#42485d"

root = tk.Tk()
root.title("System Update")
root.configure(background=background_color)

# Name of application
root.geometry("600x400+50+50")

# OS Update BTN
os_update_button = tk.Button(
    root,
    text="Update", 
    bg=btn_color,
    command=running_os_update_script,
    height=1,
    width=15
).grid(row=0, column=0)

# Source Update BTN
source_update_button = tk.Button(
    root,
    text="Source Update",
    bg=btn_color,
    command=running_source_update_script,
    height=1,
    width=15,
).grid(row=1, column=1)

# Systemboox

root.mainloop()