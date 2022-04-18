#!/bin/bash
# Developer: NR-SkaterBoy
# Github: https://github.com/NR-SkaterBoy
# E-mail: nr.rick.dev@gmail.com
# Node update

# PASSWD=$(zenity --password --title=authentication)
export SUDO_ASKPASS="bash/pass.sh"

if which mode > /dev/null
    then
        if zenity --question --title="Node Update" --text="Would you like to run node update?" --no-wrap; then
            sudo -A npm cache clean -f
            sudo -A npm install -g n
            sudo -A n stable
        fi
    else
        if zenity --question --title="Node Installing..." --text="Would you like to install node package?" --no-wrap; then
            sudo -A apt install node
            sudo -A apt install npm
        fi
fi