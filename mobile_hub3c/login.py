import os
from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.0'
desired_caps['deviceName'] = 'SWEESK8PG6CETSJ7'
desired_caps['udid'] = 'SWEESK8PG6CETSJ7'
# desired_caps['app'] = "D:\\works\\geekseat.apk"
desired_caps['appPackage'] = "au.geekseat.com.hub3candroid'"
desired_caps['appActivity'] = ".activities.SplashActivity'"
desired_caps['noReset'] = False
desired_caps['automationName'] = 'uiautomator2'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


time.sleep(5)
driver.find_element_by_id('au.geekseat.com.hub3candroid:id/textUsername').send_keys("marsha@freehub.com")
driver.find_element_by_id('au.geekseat.com.hub3candroid:id/textPassword').send_keys("ZXasqw12")
driver.find_element_by_id('au.geekseat.com.hub3candroid:id/buttonLogin').click()
time.sleep(5)
driver.find_element_by_id('au.geekseat.com.hub3candroid:id/tab_profile').click()
driver.find_element_by_id('au.geekseat.com.hub3candroid:id/containerSideNavHeader').click()
time.sleep(1)
driver.find_element_by_id('au.geekseat.com.hub3candroid:id/buttonLogout').click()
print("test case success")
time.sleep(5)

# driver.find_element_by_android_uiautomator('new UiSelector().text("Email")').send_keys('marsha@freehub.com')
# driver.find_element_by_xpath("xpath=//*[@id='textUsername']").send_keys('marsha@freehub.com')
# driver.quit()

