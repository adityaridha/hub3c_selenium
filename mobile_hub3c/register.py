from appium import webdriver
import time
import faker

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.0'
desired_caps['deviceName'] = 'SWEESK8PG6CETSJ7'
# desired_caps['app'] = "D:\\works\\geekseat.apk"
desired_caps['appPackage'] = "au.geekseat.com.hub3candroid'"
desired_caps['appActivity'] = ".activities.SplashActivity'"
desired_caps['noReset'] = False
desired_caps['automationName'] = 'uiautomator2'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


time.sleep(5)
register = driver.find_element_by_id('au.geekseat.com.hub3candroid:id/textForgotPassword')
x = register.location['x']
y = register.location['y']
positions = []
positions.append((x + 10, y))
positions.append((x + 20, y))
driver.tap(positions)
driver.find_element_by_id('au.geekseat.com.hub3candroid:id/editBusinessName').send_keys('Appium automation')
