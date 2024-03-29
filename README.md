# Linux System Update

**Project Overview**<br>

*Most PC users stick to Windows and are not willing to change to Linux because there are fewer GUI applications and they would need to learn the basic Linux commands. Moreover, most Linux-based systems get an update every week and some people think it is a waste of time to type the update commands.
<br><br>
This app may come handy for both beginners and advanced users because it is able to update the system by simply clicking a button. It supports over 10 different systems and has a built-in OS recognizer.*

!["System Updater"](/pictures/window.png)

**What the command does?**<br>

This script uses the update commands `sudo apt update && sudo apt upgrade -y && sudo apt apt autoremove -y`

**How to install the GUI?**
<br>
1. Clone this repository! `git clone https://github.com/NR-SkaterBoy/LinuxSystemUpdate.git`<br>
2. Open the LSU folder! `cd LinuxSystemUpdate/`<br>
3. Run the script! `sudo python3 install.py`
5. Wait for the install to finish!<br><br>

You may need to give additional user input, for example: press <kbd>Enter</kbd> or <kbd>Y</kbd>

**How to launch the GUI?**
<br>
1. Open LSU folder! `cd LinuxSystemUpdate/`<br>
2. Run the .py file! `./lsu.py` or `python3 lsu.py`

**Supported OS - Terminal**<br>

>Ubuntu<br>
>Kali Linux<br>
>Sparky Linux<br>
>Raspbian<br>
