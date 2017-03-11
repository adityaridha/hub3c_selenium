from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time

__author__      = "Muhammad Aditya Ridharrahman"
__version__     = "1.0"
__email__       = "aditya.ridharrahman@geekseat.com.au"
__status__      = "development"
__last_update__ = "10th Feb 2017"


class Hub3cUtility():

    def __init__(self):
        print("prepare browser configuration")

    def setup_browser(self, browser, url):
        if browser == 'Firefox':
            self.driver = webdriver.Firefox()
            # self.driver.firefox_profile(C:\Users\Geekseat\AppData\Local\Temp\rust_mozprofile.NFKTTkkS1a7v)
        if browser == 'Chrome' : self.driver = webdriver.Chrome()
        self.driver.get(url)
        assert url == self.driver.current_url

    def close_browser(self):
        print("closing the browser")
        self.driver.quit()

    def login_hub3c(self, username, password):
        driver = self.driver
        try :
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "UserName")))
            print("Login page is ready!")
        except TimeoutException:
            print("Loading took too much time!")

        print("fill in the user credential")
        user_name = driver.find_element_by_id("UserName")
        user_name.send_keys(username)
        password_ = driver.find_element_by_id("Password")
        password_.send_keys(password)
        login = driver.find_element_by_name('go')
        login.click()
        time.sleep(5)

        if username == 'mike@hub3c.com' :
            time.sleep(2)
            select = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/span")
            select.click()
            time.sleep(1)
            select.send_keys(Keys.DOWN + Keys.ENTER)
            time.sleep(1)
            select = driver.find_element_by_id("btnSubmit")
            select.click()

        try:
            WebDriverWait(driver, 10).until(EC.title_is("Hub3c - Home"))
            print("Home page is ready!")
        except TimeoutException:
            print("Login take took too much time!")


        print(driver.title)
        assert "Hub3c - Home" == driver.title

        time.sleep(4)
        driver.save_screenshot('..\capture\login1.png')

        # driver.quit()

if __name__ == "__main__":
    pass