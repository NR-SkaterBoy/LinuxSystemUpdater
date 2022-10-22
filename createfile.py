import os
import json
import shutil
import subprocess
import app



if not os.path.isdir("/home/{}/lsu".format(os.getlogin())):
    os.mkdir("/home/{}/lsu".format(os.getlogin()))

# LogFolder and neccesary file(s) [Modules]
if (not os.path.isdir(app.log_folder)):
    os.mkdir(os.path.join(app.log_folder))
if (not os.path.isdir(app.files_folder)):
    os.mkdir(os.path.join(app.files_folder))
    
if (not os.path.isfile(app.modules_json)):
    modules = {}
    modules["node update"] = "Disable"
    modules["pm2 update"] = "Disable"
    modules["forever update"] = "Disable"
    json_object = json.dumps(modules, indent=3)
    with open(app.modules_json, "w") as modules_file:
        modules_file.write(json_object)
    json.dumps(modules)
    
if (not os.path.isfile(app.application_json)):
    app = {}
    app["language"] = "English"
    app["editor"] = "nano"
    json_object = json.dumps(app, indent=3)
    with open("/home/{}/lsu/files/app.json".format(os.getlogin()), "w") as app_file:
        app_file.write(json_object)
    json.dumps(app)

# Folder of language files
if (not os.path.isdir(app.locales_folder)):
     os.mkdir(os.path.join(app.locales_folder))
    

# Fetch all files
for lang_file in os.listdir("locales"):
    source = "locales/" + lang_file
    destination = app.locales_folder + lang_file
    if os.path.isfile(source):
        shutil.copy(source, destination)
        print('copied', lang_file)

# Create run file
# with open("/home/{}/lsu/run.sh".format(os.getlogin()), "w") as run:
#     run.write("cd {} && ./lsu.py".format(os.getcwd()))