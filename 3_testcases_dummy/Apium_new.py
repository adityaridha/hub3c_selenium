import unittest
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class Untitled(unittest.TestCase):
    reportDirectory = 'reports'
    reportFormat = 'xml'
    dc = {}
    testName = 'Untitled'
    driver = None

    def setUp(self):
        self.dc['reportDirectory'] = self.reportDirectory
        self.dc['reportFormat'] = self.reportFormat
        self.dc['testName'] = self.testName
        self.dc['udid'] = "SWEESK8PG6CETSJ7'"
        self.dc['appPackage'] = "au.geekseat.com.hub3candroid'"
        self.dc['appActivity'] = ".activities.SplashActivity'"
        self.dc['noReset'] = true
        self.driver = webdriver.Remote('http://localhost:4723', desired_caps)

    def testUntitled(self):
        self.driver.find_element_by_xpath("xpath=//*[@id='textUsername']").send_keys('marsha@freehub.com')
        self.driver.find_element_by_xpath("xpath=//*[@id='textPassword']").send_keys('ZXasqw12')
        self.driver.find_element_by_xpath("xpath=//*[@text='Sign in']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='tab_profile']").click()
        self.driver.find_element_by_xpath(
            "xpath=(//*[@id='sideNavHeader']/*[@class='android.widget.ImageView'])[2]").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='Logout']").click()

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
