#!/usr/bin/python3
# Developer: NR-SkaterBoy
# Github: https://github.com/NR-SkaterBoy
# E-mail: nr.rick.dev@gmail.com
# Linux Systems source package update

# Imports
import subprocess, os, stat

os.chmod("bash/install.sh", stat.S_IRWXU)
subprocess.run("bash/install.sh")

