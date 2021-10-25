#!/bin/bash
# Developer: NR-SkaterBoy
# Github: https://github.com/NR-SkaterBoy
# Linux Systems source package update

# Help menu
if [[ "$1" == "--help" ]] || [[ "$1" == "-h" ]]; then
echo -e "\nUsage: systemupdate.sh [Operating System]"
echo -e "Example: systemupdate.sh kali"
echo -e "\nOptions:\n  --help\t\t\tprint this help message\n  -h\t\t\tsame as --help"
exit
fi

# Linux Systems
system[0]="Ubuntu"
system[1]="Kali"
system[2]="Debian"
system[3]="Fedora"
system[4]="Rasberry"
system[5]="Termux"
system[6]="Elementary"
system[7]="Linux Mint"
system[8]="Arch"
system[9]="Manjaro"

echo -e "\nAvailable systems:"
echo -e "\t\t\t1.\tUbuntu\t\t\t6.\tTermux"
echo -e "\t\t\t2.\tKali\t\t\t7.\tElementary"
echo -e "\t\t\t3.\tDebian\\t\t\t8.\tLinux Mint"
echo -e "\t\t\t4.\tFedora\t\t\t9.\tArch"
echo -e "\t\t\t5.\tRasberry\t\t10.\tManjaro"
echo " "
echo "Please select your Operating System! Use the SYSTEM NAME!"
echo " "
read opsys

case "$opsys" in
    ${system[0]}) # Ubuntu
        sudo apt update && sudo apt upgrade -y && sudo apt autoremove -y
        ;;
    ${system[1]}) # Kali
        sudo apt update && sudo apt upgrade -y && sudo apt full-upgrade -y && sudo apt autoremove -y
        ;;
    ${system[2]}) # Debian
        sudo apt update && sudo apt upgrade && sudo apt autoremove -y
        ;;
    ${system[3]}) # Fedora
        sudo dnf upgrade -y
        ;;
    ${system[4]}) # Rasberry
        sudo apt update && sudo apt full-upgrade
        ;;
    ${system[5]}) # Termux
        apt update && apt upgrade && apt autoremove
        ;;
    ${system[6]}) # Elementary OS
        sudo apt update && sudo apt upgrade -y && sudo apt autoremove -y
        ;;
    ${system[7]}) # Linux Mint
        sudo apt update && sudo apt upgrade -y && sudo apt autoremove -y
        ;;
    ${system[8]}) # Arch
        sudo pacman -Syyu
        ;;
    ${system[9]}) # Manjaro
        sudo pacman -Syyu
        ;;
esac
clear
echo "Error! Please use valid SYSTEM!" 1>&2
exit 64
