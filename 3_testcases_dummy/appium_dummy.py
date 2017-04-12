import os
from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'SWEESK8PG6CETSJ7'
desired_caps['app'] = 'C:\\Program Files (x86)\\Appium\\node_modules\\appium\\build\\unlock_apk\\unlock_apk-debug.apk'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


driver.press_keycode(3)
time.sleep(2)
home = driver.find_element_by_android_uiautomator('new UiSelector().text("Hub3c")').click()
driver.quit()
