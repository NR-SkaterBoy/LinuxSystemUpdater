#!/usr/bin/python3
# Developer/Author: NR-SkaterBoy
# Github: https://github.com/NR-SkaterBoy
# Website: https://richardneuvald.tk
# E-mail: nr.rick.dev@gmail.com
# Linux Systems source package Updater

import json
import os
from createfile import *

# Set language
read_lang_file = open(f"/home/{os.getlogin()}/lsu/files/app.json", "r")
getLang = json.load(read_lang_file)

if getLang["language"] == "English":
    eng_lang = open("/home/ricsi/Dokumentumok/LinuxSystemUpdate/locales/englis.json", "r")
    lang = json.load(eng_lang)
elif getLang["language"] == "Hungary":
    hun_lang = open("/home/ricsi/Dokumentumok/LinuxSystemUpdate/locales/hungary.json", "r")
    lang = json.load(hun_lang)

# Name of window(s)
lsu = lang["window_name"]["lsu"]
settings = lang["window_name"]["settings"]

# Titles
t_systm_updater = lang["titles"]["systm_updater"]
t_modul = lang["titles"]["modul"]
t_language = lang["titles"]["language"]
t_editor = lang["titles"]["editor"]

# Button(s)
btn_lsu_sys = lang["buttons"]["lsu_sys"]
btn_lsu_web = lang["buttons"]["lsu_web"]
btn_lsu_github = lang["buttons"]["lsu_github"]

# Modul
m_node = lang["modul"]["node"]
m_pm2 = lang["modul"]["pm2"]

# Language
l_eng = lang["language"]["eng"]
l_hu = lang["language"]["hun"]

# Menu Line
ml_lsu_menu = lang["menu_line"]["lsu_menu"]
ml_lsu_news = lang["menu_line"]["lsu_news"]
ml_lsu_info = lang["menu_line"]["lsu_info"]
ml_stngs_menu = lang["menu_line"]["stngs_menu"]
ml_stngs_modul = lang["menu_line"]["stngs_modul"]

# LSU Menu
lm_supsys = lang["lsu_menu"]["supsys"]
lm_about = lang["lsu_menu"]["about"]
lm_settings = lang["lsu_menu"]["settings"]
lm_exit = lang["lsu_menu"]["exit"]

# LSU News
ln_questionaire = lang["lsu_news"]["questionaire"]

# LSU Info
li_log_file = lang["lsu_info"]["log_file"]
li_last_log = lang["lsu_info"]["last_log"]
li_sysinfo = lang["lsu_info"]["sysinfo"]

# Settings Menu
sm_whatis = lang["stngs_menu"]["whatis"]

# Settings Modul
sm_node = lang["stngs_modul"]["node"]
sm_pm2 = lang["stngs_modul"]["pm2"]

# Title of Messagebox
tm_notify = lang["msgbox_title"]["notify"]
tm_error = lang["msgbox_title"]["error"]
tm_howtouse = lang["msgbox_title"]["howtouse"]
tm_supsys = lang["msgbox_title"]["supsys"]
tm_sysinfo = lang["msgbox_title"]["sysinfo"]
tm_about = lang["msgbox_title"]["about"]
tm_lastlog = lang["msgbox_title"]["lastlog"]

# Description of Messagebox
dm_restart = lang["msgbox_des"]["restart"]
dm_howtouse = lang["msgbox_des"]["howtouse"]
dm_about = lang["msgbox_des"]["about"]
dm_lang_res = lang["msgbox_des"]["lang_res"]

# AppInfo
appi = lang["app"]["version"]