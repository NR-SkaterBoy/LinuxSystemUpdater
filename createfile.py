import os
import json
# import shutil

log_folder = f"/home/{os.getlogin()}/lsu/logs"
files_folder = f"/home/{os.getlogin()}/lsu/files"
# img_folder = f"/home/{os.getlogin()}/lsu/img/"

modules_file = f"/home/{os.getlogin()}/lsu/files/modules.json"
application_file = f"/home/{os.getlogin()}/lsu/files/app.json"

if not os.path.isdir(f"/home/{os.getlogin()}/lsu"):
    os.mkdir(f"/home/{os.getlogin()}/lsu")

# LogFolder and neccesary file(s) [Modules]
if (not os.path.isdir(log_folder)):
    os.mkdir(os.path.join(log_folder))
if (not os.path.isdir(files_folder)):
    os.mkdir(os.path.join(files_folder))
    
if (not os.path.isfile(modules_file)):
    modules = {}
    modules["node update"] = "Disable"
    modules["pm2 update"] = "Disable"
    modules["forever update"] = "Disable"
    json_object = json.dumps(modules, indent=3)
    with open(modules_file, "w") as modules_file:
        modules_file.write(json_object)
    json.dumps(modules)
    
if (not os.path.isfile(application_file)):
    app = {}
    app["language"] = "English"
    app["editor"] = "nano"
    json_object = json.dumps(app, indent=3)
    with open(application_file, "w") as app_file:
        app_file.write(json_object)
    json.dumps(app)

# Image folder with images
# if (not os.path.isdir(img_folder)):
#     os.mkdir(os.path.join(img_folder))
    

# fetch all files
# for file_name in os.listdir("img"):
#     source = "img/" + file_name
#     destination = img_folder + file_name
#     if os.path.isfile(source):
#         shutil.copy(source, destination)
#         print('copied', file_name)