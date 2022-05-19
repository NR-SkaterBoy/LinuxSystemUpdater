#!/usr/bin/python3
# Developer/Author: NR-SkaterBoy
# Github: https://github.com/NR-SkaterBoy
# Website: https://richardneuvald.tk
# E-mail: nr.rick.dev@gmail.com
# Linux Systems source package Updater

import json
import os

if (not os.path.isdir("files")):
    os.mkdir(os.path.join("files"))

if (not os.path.isfile("files/language.json")):
    language = {}
    language["Language"] = "English"
    json_object = json.dumps(language, indent=3)
    with open("files/language.json", "w") as language_file:
        language_file.write(json_object)
        json.dumps(json_object)


# Set language
read_lang_file = open("files/language.json", "r")
getLang = json.load(read_lang_file)

if getLang["Language"] == "English":
    eng_lang = open("./locales/englis.json", "r")
    lang = json.load(eng_lang)
elif getLang["Language"] == "Hungary":
    hun_lang = open("./locales/hungary.json", "r")
    lang = json.load(hun_lang)

# Main (pref.: m)
m_app_name = lang["main"]["app_name"]
m_app_title = lang["main"]["app_title"]
m_upd_btn = lang["main"]["upd_btn"]
m_web_btn = lang["main"]["web_btn"]
m_git_btn = lang["main"]["git_btn"]
m_h_category = lang["main"]["help"]["category"]
m_h_sup_sys = lang["main"]["help"]["sup_sys"]
m_h_about = lang["main"]["help"]["about"]
m_h_settings = lang["main"]["help"]["setting"]
m_h_quit = lang["main"]["help"]["quit"]
m_n_category = lang["main"]["news"]["category"]
m_n_questionaire = lang["main"]["news"]["questionaire"]
m_i_category = lang["main"]["info"]["category"]
m_i_log_file = lang["main"]["info"]["log_file"]
m_i_last_log = lang["main"]["info"]["last_log"]
m_i_system = lang["main"]["info"]["system"]
# Settings (pref.: s)
s_window_name = lang["settings"]["window_name"]
s_title = lang["settings"]["title"]
s_node = lang["settings"]["node"]
s_pm2 = lang["settings"]["pm2"]
s_lang_title = lang["settings"]["l_title"]
s_lang_en = lang["settings"]["english"]
s_lang_hu = lang["settings"]["hungary"]
s_h_category = lang["settings"]["help"]["category"]
s_h_whatisit = lang["settings"]["help"]["whatisit"]
s_m_category = lang["settings"]["modules"]["category"]
s_m_node = lang["settings"]["modules"]["node"]
s_m_pm2 = lang["settings"]["modules"]["pm2"]
# Title of messagebox (pref.: t)
t_howtouse = lang["tmessagebox"]["howtouseit"]
t_error = lang["tmessagebox"]["error"]
t_sup_sys = lang["tmessagebox"]["sup_sys"]
t_sys_inf = lang["tmessagebox"]["sys_inf"]
t_about = lang["tmessagebox"]["about_project"]
t_lastlog = lang["tmessagebox"]["lastlog"]
t_notify = lang["tmessagebox"]["notify"]
# Description of messagebox (pref.: d)
d_restart = lang["dmessagebox"]["restart"]
d_howtouse = lang["dmessagebox"]["howtouse"]
d_about = lang["dmessagebox"]["about"]
d_not_res = lang["dmessagebox"]["notify_res"]
