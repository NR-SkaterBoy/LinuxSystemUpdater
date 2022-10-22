__author__ = "NR-SkaterBoy"
__email__ = "nr.rick.dev@gmail.com"
__website__ = "https://richardneuvald.tk/"
__github__ = "https://github.com/NR-SkaterBoy"
__issues__ = "https://github.com/NR-SkaterBoy/LinuxSystemUpdate/issues"
__version__ = "0.9.0"
__update__ = "2022.10.23"

# Folders and files
import os

log_folder = "/home/{}/lsu/logs".format(os.getlogin())
files_folder = "/home/{}/lsu/files".format(os.getlogin())
locales_folder = "/home/{}/lsu/locales/".format(os.getlogin())

modules_json = "/home/{}/lsu/files/modules.json".format(os.getlogin())
application_json = "/home/{}/lsu/files/app.json".format(os.getlogin())
runtime_json = "/home/{}/lsu/logs/runtime.json".format(os.getlogin())
sysinfo_json =  "/home/{}/lsu/files/sysinfo.json".format(os.getlogin())
