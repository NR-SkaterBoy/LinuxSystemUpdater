#!/usr/bin/python3
# Developer: NR-SkaterBoy
# Github: https://github.com/NR-SkaterBoy
# E-mail: nr.rick.dev@gmail.com
# Linux Systems source package update

# Imports
import subprocess, os, stat

# Set the file(s) rights
directory = "bash"
for i in os.listdir(directory):
    files = os.path.join(directory, i)
    # print(files)
    os.chmod(files, stat.S_IRWXU)
subprocess.run("bash/install.sh")

