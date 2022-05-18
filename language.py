#!/usr/bin/python3
# Developer/Author: NR-SkaterBoy
# Github: https://github.com/NR-SkaterBoy
# Website: https://richardneuvald.tk
# E-mail: nr.rick.dev@gmail.com
# Linux Systems source package Updater

import json

# Set language
read_lang_file = open("files/language.json", "r")
getLang = json.load(read_lang_file)

if getLang["Language"] == "English":
    eng_lang = open("locales/englis.json", "r")
    en = json.load(eng_lang)

    # Main (pref.: m)
    m_app_name = en["main"]["app_name"]
    m_app_title = en["main"]["app_title"]
    m_upd_btn = en["main"]["upd_btn"]
    m_web_btn = en["main"]["web_btn"]
    m_git_btn = en["main"]["git_btn"]
    m_h_category = en["main"]["help"]["category"]
    m_h_sup_sys = en["main"]["help"]["sup_sys"]
    m_h_about = en["main"]["help"]["about"]
    m_h_settings = en["main"]["help"]["setting"]
    m_h_quit = en["main"]["help"]["quit"]
    m_n_category = en["main"]["news"]["category"]
    m_n_questionaire = en["main"]["news"]["questionaire"]
    m_i_category = en["main"]["info"]["category"]
    m_i_log_file = en["main"]["info"]["log_file"]
    m_i_last_log = en["main"]["info"]["last_log"]
    m_i_system = en["main"]["info"]["system"]

    # Settings (pref.: s)
    s_window_name = en["settings"]["window_name"]
    s_title = en["settings"]["title"]
    s_node = en["settings"]["node"]
    s_pm2 = en["settings"]["pm2"]
    s_lang_title = en["settings"]["l_title"]
    s_lang_en = en["settings"]["english"]
    s_lang_hu = en["settings"]["hungary"]
    s_h_category = en["settings"]["help"]["category"]
    s_h_whatisit = en["settings"]["help"]["whatisit"]
    s_m_category = en["settings"]["modules"]["category"]
    s_m_node = en["settings"]["modules"]["node"]
    s_m_pm2 = en["settings"]["modules"]["pm2"]

    # Title of messagebox (pref.: t)
    t_howtouse = en["tmessagebox"]["howtouseit"]
    t_error = en["tmessagebox"]["error"]
    t_sup_sys = en["tmessagebox"]["sup_sys"]
    t_sys_inf = en["tmessagebox"]["sys_inf"]
    t_about = en["tmessagebox"]["about_project"]
    t_lastlog = en["tmessagebox"]["lastlog"]
    t_notify = en["tmessagebox"]["notify"]

    # Description of messagebox (pref.: d)
    d_restart = en["dmessagebox"]["restart"]
    d_howtouse = en["dmessagebox"]["howtouse"]
    d_about = en["dmessagebox"]["about"]
    d_not_res = en["dmessagebox"]["notify_res"]

elif getLang["Language"] == "Hungary":
    hun_lang = open("locales/hungary.json", "r")
    hu = json.load(hun_lang)

    # Main (pref.: m)
    m_app_name = hu["main"]["app_name"]
    m_app_title = hu["main"]["app_title"]
    m_upd_btn = hu["main"]["upd_btn"]
    m_web_btn = hu["main"]["web_btn"]
    m_git_btn = hu["main"]["git_btn"]
    m_h_category = hu["main"]["help"]["category"]
    m_h_sup_sys = hu["main"]["help"]["sup_sys"]
    m_h_about = hu["main"]["help"]["about"]
    m_h_settings = hu["main"]["help"]["setting"]
    m_h_quit = hu["main"]["help"]["quit"]
    m_n_category = hu["main"]["news"]["category"]
    m_n_questionaire = hu["main"]["news"]["questionaire"]
    m_i_category = hu["main"]["info"]["category"]
    m_i_log_file = hu["main"]["info"]["log_file"]
    m_i_last_log = hu["main"]["info"]["last_log"]
    m_i_system = hu["main"]["info"]["system"]

    # Settings (pref.: s)
    s_window_name = hu["settings"]["window_name"]
    s_title = hu["settings"]["title"]
    s_node = hu["settings"]["node"]
    s_pm2 = hu["settings"]["pm2"]
    s_lang_title = hu["settings"]["l_title"]
    s_lang_en = hu["settings"]["english"]
    s_lang_hu = hu["settings"]["hungary"]
    s_h_category = hu["settings"]["help"]["category"]
    s_h_whatisit = hu["settings"]["help"]["whatisit"]
    s_m_category = hu["settings"]["modules"]["category"]
    s_m_node = hu["settings"]["modules"]["node"]
    s_m_pm2 = hu["settings"]["modules"]["pm2"]

    # Title of messagebox (pref.: t)
    t_howtouse = hu["tmessagebox"]["howtouseit"]
    t_error = hu["tmessagebox"]["error"]
    t_sup_sys = hu["tmessagebox"]["sup_sys"]
    t_sys_inf = hu["tmessagebox"]["sys_inf"]
    t_about = hu["tmessagebox"]["about_project"]
    t_lastlog = hu["tmessagebox"]["lastlog"]
    t_notify = hu["tmessagebox"]["notify"]

    # Description of messagebox (pref.: d)
    d_restart = hu["dmessagebox"]["restart"]
    d_howtouse = hu["dmessagebox"]["howtouse"]
    d_about = hu["dmessagebox"]["about"]
    d_not_res = hu["dmessagebox"]["notify_res"]
