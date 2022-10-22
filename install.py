#!/usr/bin/python3


# Imports
import subprocess
import os
import stat
# import re
# import app

# Set the file(s) rights
directory = "bash"
for file in os.listdir(directory):
    files = os.path.join(directory, file)
    os.chmod(files, stat.S_IRWXU)
subprocess.run("bash/install.sh")


# # Desktop launcher
# def get_desktop_path():
#     D_paths = list()
#     try:
#         fs = open(os.sep.join((os.path.expanduser("~"),
#                   ".config", "user-dirs.dirs")), 'r')
#         data = fs.read()
#         fs.close()
#     except:
#         data = ""

#     D_paths = re.findall(r'XDG_DESKTOP_DIR=\"([^\"]*)', data)

#     if len(D_paths) == 1:
#         D_path = D_paths[0]
#         D_path = re.sub(r'\$HOME', os.path.expanduser("~"), D_path)
#     else:
#         D_path = os.sep.join((os.path.expanduser("~"), 'Desktop'))

#     if os.path.isdir(D_path):
#         return D_path


# a = get_desktop_path()

# launcher_text = f"""[Desktop Entry] 
# Version={app.__version__}
# Name=Linux Updater
# Exec={os.getcwd()}/lsu.py
# Icon={os.getcwd()}/img/lsu_icon.png
# Type=Application
# Terminal=true
# """

# with open(f"{a}/lsu.desktop", "w") as launcher:
#     launcher.write(launcher_text)
