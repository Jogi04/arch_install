#!/bin/python

import time
import configparser
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class WoL:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('/home/jogi/programming/python/fun_projects/config_WoL.ini')
        self.password = self.config['credentials']['password']
        self.wake_on_lan()

    def wake_on_lan(self):
        self.init_webdriver()
        self.login_to_fritzbox_web_ui()
        self.navigate_to_target_host()
        self.wake_host()

    def init_webdriver(self):
        options = Options()
        options.add_argument('--headless')
        self.driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver', options=options, service_log_path='/dev/null')
        addons = ['/home/jogi/programming/python/fun_projects/uBlock0_1.32.5b9.firefox.signed.xpi']
        for addon in addons:
            self.driver.install_addon(addon)

    def login_to_fritzbox_web_ui(self):
        self.driver.get('http://192.168.178.1/')
        self.driver.find_element_by_id('uiPass').send_keys(self.password)
        self.driver.find_element_by_id('submitLoginBtn').click()

    def navigate_to_target_host(self):
        self.driver.find_element_by_id('lan').click()
        self.driver.find_element_by_id('net').click()
        time.sleep(18)
        self.driver.find_element_by_id('edit_landevice258').click()

    def wake_host(self):
        time.sleep(20)
        # scroll to the end of the page so the "start host" button is not obscured by "ok"/"cancel" button
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element_by_name('btn_wake').click()
        print('remote host started...')
