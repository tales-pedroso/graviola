# -*- coding: utf-8 -*-
'''
selenium Webdriver code
'''

from config import GECKODRIVER_PATH
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

def create_driver():
    service = Service(GECKODRIVER_PATH)
    driver = webdriver.Firefox(service = service)
    driver.maximize_window()
    return driver

    