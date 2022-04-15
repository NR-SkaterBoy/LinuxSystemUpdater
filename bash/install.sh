#!/bin/bash
# Developer: NR-SkaterBoy
# Github: https://github.com/NR-SkaterBoy
# E-mail: nr.rick.dev@gmail.com
# Linux Systems source package update

shell=True

. /etc/os-release

case "$ID" in
    "ubuntu" | "kali" | "raspbian" | "sparky")
        pip install -r ../requirements.txt
        sudo apt-get install -y python3.6
        sudo apt install python3-tk -y
        sudo apt install python-tk -y
    ;;
    # "fedora") # Fedora - Later
    #     sudo dnf install python3-tkinter
    # ;;
    *)
        exit 1
    ;;
esac
# Launch LSU
python3 lsu.py