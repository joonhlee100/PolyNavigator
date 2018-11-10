#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.support import ui

browser = webdriver.Chrome("/home/sfrazee/Desktop/polybot/PolyRegister/chromedriver")
browser.get('http://my.calpoly.edu/')

loginWait = ui.WebDriverWait(browser,300)
loginWait.until(lambda driver: driver.find_element_by_id('portalWelcome'))

browser.get("https://idp.calpoly.edu/idp/profile/cas/login?service=https://cmsweb.calpoly.edu/psp/CSLOPRD/EMPLOYEE/SA/c/SA_LEARNER_SERVICES.SSS_STUDENT_CENTER.GBL?FolderPath=PORTAL_ROOT_OBJECT.CO_EMPLOYEE_SELF_SERVICE.HC_SSS_STUDENT_CENTER%26IsFolder=false%26IgnoreParamTempl=FolderPath%2cIsFolder%26RL=%26target=main0%26navc=2398?cmd=login%26languageCd=ENG%26userid=PS%26pwd=z&method=post")