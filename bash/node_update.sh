#!/bin/bash
# Developer: NR-SkaterBoy
# Github: https://github.com/NR-SkaterBoy
# E-mail: nr.rick.dev@gmail.com
# Node update

PASSWD=$(zenity --password --title=authentication)

if zenity --question --title="Node Update" --text="Would you like to run apt update?" --no-wrap; then
    echo -e $PASSWD | sudo -S npm cache clean -f
    echo -e $PASSWD | sudo -S npm install -g n
    echo -e $PASSWD | sudo -S n stable
fi