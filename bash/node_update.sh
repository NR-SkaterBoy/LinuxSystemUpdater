#!/bin/bash
# Developer: NR-SkaterBoy
# Github: https://github.com/NR-SkaterBoy
# E-mail: nr.rick.dev@gmail.com
# Node update

# PASSWD=$(zenity --password --title=authentication)
export SUDO_ASKPASS="./pass.sh"

if zenity --question --title="Node Update" --text="Would you like to run node update?" --no-wrap; then
    sudo -A npm cache clean -f
    sudo -A npm install -g n
    sudo -A n stable
fi