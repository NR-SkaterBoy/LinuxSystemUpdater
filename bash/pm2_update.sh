#!/bin/bash
# Developer: NR-SkaterBoy
# Github: https://github.com/NR-SkaterBoy
# E-mail: nr.rick.dev@gmail.com
# Node update

# PASSWD=$(zenity --password --title=authentication)
export SUDO_ASKPASS="bash/pass.sh"

command
returncode_node=$?
cmd_n="which node"
$cmd_n
returncode_node=$?
returncode_pm2=$?
cmd="which pm2"
$cmd
returncode_pm2=$?

if [ $returncode_node -eq 0 ]
then
    if [ $returncode_pm2 -eq 0 ]
    then
        if zenity --question --title="pm2 Update" --text="Would you like to run pm2 update?" --no-wrap; then
            sudo -A npm install pm2 -g
            sudo -A pm2 update
            sudo -A pm2 unstartup
            sudo -A pm2 startup
        fi
    else
        if zenity --question --title="pm2 Installing..." --text="Would you like to install pm2 package?" --no-wrap; then
            sudo -A npm install pm2 -g
        fi
    fi
else
    if zenity --question --title="Node Installing..." --text="Would you like to install node package? This package is required for pm2!" --no-wrap; then
        sudo -A apt install nodejs -y
        sudo -A apt install npm -y
        sudo -A npm install pm2 -g
    fi
fi