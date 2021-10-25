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
    systems=("Ubuntu" "Kali" "Debian" "Fedora" "Rasberry" "Termux" "Elementary" "Linux Mint" "Arch" "Manjaro")


echo -e "\nAvailable systems:"
echo -e "\t\t\t1.\tUbuntu\t\t\t6.\tTermux"
echo -e "\t\t\t2.\tKali\t\t\t7.\tElementary"
echo -e "\t\t\t3.\tDebian\\t\t\t8.\tLinux Mint"
echo -e "\t\t\t4.\tFedora\t\t\t9.\tArch"
echo -e "\t\t\t5.\tRasberry\t\t10.\tManjaro"
echo " "
echo "Please select your Operating System! Use the SYSTEM NAME!"
echo " "
read -p "Type your system: " opsys

if [[ $opsys == ${systems[0]} ]] || [[ $opsys == ${systems[1]} ]] || [[ $opsys == ${systems[2]} ]] || [[ $opsys == ${systems[3]} ]] || [[ $opsys == ${systems[4]} ]] || [[ $opsys == ${systems[5]} ]] || [[ $opsys == ${systems[6]} ]] || [[ $opsys == ${systems[7]} ]] || [[ $opsys == ${systems[8]} ]] || [[ $opsys == ${systems[9]} ]]; then
    case "$opsys" in
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
    ${systems[5]}) # Termux
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
    esac
    clear
    echo -e "\e[32mSuccesfull Update!"
    echo -e "\e[32mSuccesfull Update!"
    echo -e "\e[32mSuccesfull Update!"
    echo " "
    echo " "
    echo " "
else
    clear
    echo -e "\e[31mError! Please enter valid SYSTEM!"
    echo -e "\e[31mError! Please enter valid SYSTEM!"
    echo -e "\e[31mError! Please enter valid SYSTEM!"
    echo " "
    echo " "
    echo " "
    exit
fi