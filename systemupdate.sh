#!/bin/bash
# Linux Systems source package update

# Help menu
if [[ "$1" == "--help" ]] || [[ "$1" == "-h" ]]; then
    echo -e "\nUsage: systemupdate.sh [Operating System]"
    echo -e "Example: systemupdate.sh kali"
    echo -e "\nOptions:\n  --help\t\t\tprint this help message\n  -h\t\t\tsame as --help"
    exit
fi

# Linux Systems
    system[0]="Ubuntu"          #
    system[1]="Kali"            #
    system[2]="Debian"          #
    system[3]="Fedora"          #
    system[4]="Rasberry"        #
    system[5]="Termux"          #

echo -e "\nAvailable systems:\n\t\t\tUbuntu\n\t\t\tKali\n\t\t\tDebian\n\t\t\tFedora\n\t\t\tRasberry\n"
echo "Please select your Operating System!"
read opsys

case "$opsys" in
    ${system[0]}) # Ubuntu
        sudo apt update && sudo apt upgrade -y
        ;;
    ${system[1]}) # Kali
        sudo apt update && sudo apt upgrade -y && sudo apt full-upgrade -y
        ;;
    ${system[2]}) # Debian
        sudo apt update && sudo apt upgrade
        ;;
    ${system[3]}) # Fedora
        sudo dnf upgrade -y
        ;;
    ${system[4]}) # Rasberry
        sudo apt update && sudo apt full-upgrade
        ;;
    ${system[5]}) # Termux
        apt update && apt upgrade -y
        ;;
esac
