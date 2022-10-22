#!/bin/bash
# Developer: NR-SkaterBoy
# Github: https://github.com/NR-SkaterBoy
# E-mail: nr.rick.dev@gmail.com
# Linux Systems source package update

shell=True
. /etc/os-release

package_list=(python3.10 python3-tk)

function pkgscheck() {
    case "$ID" in
        "ubuntu" | "kali" | "raspbian" | "sparky")
            for pkg in "${package_list[@]}"
            do
                echo -e "\033[1m\033[34m[\033[31m+\033[34m] Checking for $pkg\033[0m"
                sleep 1
                if ! hash $pkg 2>/dev/null; then
                    echo -e "\033[1m\033[31mNot Found\033[0m"
                    apt-get install $pkg -y
                else
                    echo -e "\033[1m\033[32mFound\033[0m"
                fi
            done
            pip3 install -r requirements.txt
        ;;
        *)
            exit 1
        ;;
    esac
}

pkgscheck

# echo 'alias lsu="bash /home/$USER/lsu/run.sh"' >> /home/ricsi/.bashrc
# echo 'alias lsu="bash /home/$USER/lsu/run.sh"' >> /home/ricsi/.bash_aliases
# source ~/.bashrc
# source ~/.bash_aliases

# Launch LSU
python3 lsu.py