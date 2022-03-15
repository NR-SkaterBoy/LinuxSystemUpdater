#!/bin/bash
# Developer: NR-SkaterBoy
# Github: https://github.com/NR-SkaterBoy
# E-mail: nr.rick.dev@gmail.com
# Linux Systems source package update

shell=True

. /etc/os-release

systems=("ubuntu" "kali" "fedora" "raspbian")

if [[ $ID == ${systems[0]} ]] || [[ $ID == ${systems[1]} ]] || [[ $ID == ${systems[2]} ]] || [[ $ID == ${systems[3]} ]]; then
    case "$ID" in
    ${systems[0]}) # Ubuntu
        sudo apt-get install python3.6 -y
        sudo apt-get install python3-tk -y
        sudo apt-get install python-tk -y
        ;;
    ${systems[1]}) # Kali
        sudo apt-get install python3.6 -y
        sudo apt-get install python3-tk -y
        sudo apt-get install python-tk -y
        ;;
    ${systems[2]}) # Fedora
        sudo dnf install python3.6
        sudo dnf install python3-tk -y
        sudo dnf install python-tk -y
        ;;
    ${systems[3]}) # Debian
        sudo apt-get install python3.6 -y
        sudo apt-get install python3-tk -y
        sudo apt-get install python-tk -y
        ;;
    esac
fi
# Launc LSU
python3 lsu.py