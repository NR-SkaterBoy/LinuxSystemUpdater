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
# Linux Systems
systems=("ubuntu" "kali" "fedora" "raspbian")

# Linux version ID
. /etc/os-release


if [[ $ID == ${systems[0]} ]] || [[ $ID == ${systems[1]} ]] || [[ $ID == ${systems[2]} ]] || [[ $ID == ${systems[3]} ]] || [[ $ID == ${systems[4]} ]] || [[ $ID == ${systems[5]} ]] || [[ $ID == ${systems[6]} ]] || [[ $ID == ${systems[7]} ]] || [[ $ID == ${systems[8]} ]] || [[ $ID == ${systems[9]} ]]; then
    case "$ID" in
    ${systems[0]} | ${systems[1]} | ${systems[3]}) # Ubuntu-Kali-Raspbian
        zenity --password --title=authentication | sudo -S apt update && sudo -S apt upgrade -y && sudo -S apt autoremove -y
        ;;
    ${systems[2]}) # Fedora
        zenity --password --title=Authentication | sudo -S dnf upgrade -y
        ;;
     esac
    zenity --notification --text "Succesful Update!" 
    # System restart
    if zenity --question --title="Restart" --text="Please restart the system!\n\nWould you like to restart the system?" --no-wrap; then
        zenity --password --title=Authentication | shutdown -r now
    fi
    exit
else
    zenity --error --title="Error" --text="Update failed!\nPlease check the supported systems or your internet connection!" --no-wrap
    exit
fi
