#!/bin/bash
# Developer: NR-SkaterBoy
# Github: https://github.com/NR-SkaterBoy
# E-mail: nr.rick.dev@gmail.com
# Linux Systems source package update

shell=True

. /etc/os-release

case "$ID" in
    "ubuntu" | "kali" | "raspbian")
        pip install -r ../requirements.txt
        sudo apt install python3.6 -y
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
# Launc LSU
python3 lsu.py