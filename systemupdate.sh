#!/bin/bash
# Developer: NR-SkaterBoy
# Github: https://github.com/NR-SkaterBoy
# E-mail: nr.rick.dev@gmail.com
# Linux Systems source package update

# Help menu
if [[ "$1" == "--help" ]] || [[ "$1" == "-h" ]]; then
echo -e "\nUsage: systemupdate.sh"
echo -e "\nOptions:\n  --help\t\t\tprint this help message\n  -h\t\t\tsame as --help"
echo " "
echo "Supported OS:"
echo -e "\t1.\tUbuntu\t\t\t2.\tKali Linux"
echo -e "\t3.\tDebian\t\t\t4.\tFedora"
echo -e "\t5.\tRasberry\t\t6.\tZorin OS"
echo -e "\t7.\tElementary OS\t\t8.\tLinux Mint"
echo -e "\t9.\tArch Linux\t\t10.\tManjaro"
echo -e "\t11.\tGentoo"
exit
fi

# Linux Systems
systems=("ubuntu" "kali" "debian" "fedora" "rasberry" "zorin" "elementary" "linux mint" "arch" "manjaro" "gentoo")

# Linux version ID
. /etc/os-release

# Script update
echo -e "\e[33mKeep the script up to date! Don't forget to upgrade!"
echo -e "\e[39m"

read -p "Would you like to update the script? (Y/N): " ans

if [[ $ans == [yY] || $ans == [yY][eE][sS] ]]; then
    git pull
fi

if [[ $ID == ${systems[0]} ]] || [[ $ID == ${systems[1]} ]] || [[ $ID == ${systems[2]} ]] || [[ $ID == ${systems[3]} ]] || [[ $ID == ${systems[4]} ]] || [[ $ID == ${systems[5]} ]] || [[ $ID == ${systems[6]} ]] || [[ $ID == ${systems[7]} ]] || [[ $ID == ${systems[8]} ]] || [[ $ID == ${systems[9]} ]]; then
    case "$ID" in
    ${systems[0]}) # Ubuntu
        sudo apt update && sudo apt upgrade -y && sudo apt autoremove -y
        ;;
    ${systems[1]}) # Kali
        sudo apt update && sudo apt upgrade -y && sudo apt full-upgrade -y && sudo apt autoremove -y
        ;;
    ${systems[2]}) # Debian
        sudo apt update && sudo apt upgrade && sudo apt autoremove -y
        ;;
    ${systems[3]}) # Fedora
        sudo dnf upgrade -y
        ;;
    ${systems[4]}) # Rasberry
        sudo apt update && sudo apt full-upgrade
        ;;
    ${systems[5]}) # Zorin
        apt update && apt upgrade && apt autoremove
        ;;
    ${systems[6]}) # Elementary OS
        sudo apt update && sudo apt upgrade -y && sudo apt autoremove -y
        ;;
    ${systems[7]}) # Linux Mint
        sudo apt update && sudo apt upgrade -y && sudo apt autoremove -y
        ;;
    ${systems[8]}) # Arch
        sudo pacman -Syyu
        ;;
    ${systems[9]}) # Manjaro
        sudo pacman -Syyu
        ;;
    ${systems[10]}) # Gentoo
        sudo emerge --sync && sudo emerge --update --deep --with-bdeps=y @world
        ;;
    esac
    clear
    echo -e "\e[32mSuccesful Update!"
    echo -e "\e[32mSuccesful Update!"
    echo -e "\e[32mSuccesful Update!\e[39m"
    echo " "
    echo " "
    echo " "
else
    clear
    echo -e "\e[31mUpdate failed! Please check the supported OS!"
    echo -e "\e[31mUpdate failed! Please check the supported OS!"
    echo -e "\e[31mUpdate failed! Please check the supported OS!\e[39m"
    echo " "
    echo " "
    echo " "
    exit
fi
