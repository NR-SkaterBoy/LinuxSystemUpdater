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

git pull
shell=True
export SUDO_ASKPASS="myaskpass.sh"
# Linux Systems
systems=("ubuntu" "kali" "debian" "fedora" "raspbian" "zorin" "elementary" "linuxmint" "arch" "manjaro" "gentoo")

# Linux version ID
. /etc/os-release


if [[ $ID == ${systems[0]} ]] || [[ $ID == ${systems[1]} ]] || [[ $ID == ${systems[2]} ]] || [[ $ID == ${systems[3]} ]] || [[ $ID == ${systems[4]} ]] || [[ $ID == ${systems[5]} ]] || [[ $ID == ${systems[6]} ]] || [[ $ID == ${systems[7]} ]] || [[ $ID == ${systems[8]} ]] || [[ $ID == ${systems[9]} ]]; then
    case "$ID" in
    ${systems[0]}) # Ubuntu
        sudo -A apt update && sudo -A apt upgrade -y && sudo -A apt autoremove -y
        ;;
    ${systems[1]}) # Kali
        sudo -A apt update && sudo -A apt upgrade -y && sudo -A apt full-upgrade -y && sudo -A apt autoremove -y
        ;;
    ${systems[2]}) # Debian
        sudo -A apt update && sudo -A apt upgrade && sudo -A apt autoremove -y
        ;;
    ${systems[3]}) # Fedora
        sudo -A dnf upgrade -y
        ;;
    ${systems[4]}) # Raspberry
        sudo -A apt update && sudo -A apt upgrade && sudo -A apt autoremove -y
        ;;
    ${systems[5]}) # Zorin
        sudo -A apt update && sudo -A apt upgrade && sudo -A apt autoremove
        ;;
    ${systems[6]}) # Elementary OS
        sudo -A apt update && sudo -A apt upgrade -y && sudo -A apt autoremove -y
        ;;
    ${systems[7]}) # Linux Mint
        sudo -A apt update && sudo -A apt upgrade -y && sudo -A apt autoremove -y
        ;;
    ${systems[8]}) # Arch
        sudo -A pacman -Syyu
        ;;
    ${systems[9]}) # Manjaro
        sudo -A pacman -Syyu
        ;;
    ${systems[10]}) # Gentoo
        sudo -A emerge --sync && sudo -A emerge --update --deep --with-bdeps=y @world
        ;;

    esac
    zenity --notification --text "Succesful Update!" 
    # System restart
    if zenity --question --title="Restart" --text="Please restart the system!\n\nWould you like to restart the system?" --no-wrap; then
        sudo shutdown -r now
    fi
    exit
else
    zenity --error --title="Error" --text="Update failed!\nPlease check the supported systems or your internet connection!" --no-wrap
    exit
fi
