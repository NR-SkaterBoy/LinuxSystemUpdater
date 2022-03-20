#!/bin/bash
# Developer: NR-SkaterBoy
# Github: https://github.com/NR-SkaterBoy
# E-mail: nr.rick.dev@gmail.com
# Linux Systems source package update

# Help menu
if [[ "$1" == "--help" ]] || [[ "$1" == "-h" ]]; then
echo " "
echo "Supported OS:"
echo -e "\t1.\tUbuntu\t\t\t2.\tKali Linux"
echo -e "\t3.\tFedora\t\t\t4.\tRaspbian"
exit
fi

# *** Linuy Types *** #
# Just Supported Systems
# Debian: Ubuntu|Kali|Raspbian
# RPM: Fedora

git pull
shell=True

# Linux version ID
. /etc/os-release


if [[ $ID == "ubuntu" ]] || [[ $ID == "kali" ]] || [[ $ID == "raspbian" ]] || [[ $ID == "fedora" ]]; then
    case "$ID" in
    "ubuntu" | "kali" | "raspbian") # Ubuntu-Kali-Raspbian
        zenity --password --title=authentication | sudo -S apt update && sudo -S apt upgrade -y && sudo -S apt autoremove -y
        ;;
    "fedora") # Fedora
        zenity --password --title=Authentication | sudo -S dnf upgrade -y
        ;;
     esac

    # System restart
    if zenity --question --title="Restart" --text="Please restart the system!\n\nWould you like to restart the system?" --no-wrap; then
        zenity --password --title=Authentication | shutdown -r now
    fi
    exit
else
    zenity --error --title="Error" --text="Update failed!\nPlease check the supported systems or your internet connection!" --no-wrap
    exit
fi
