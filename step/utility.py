from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from datetime import datetime
import time

__author__      = "Muhammad Aditya Ridharrahman"
__version__     = "1.0"
__email__       = "aditya.ridharrahman@geekseat.com.au"
__status__      = "development"
__last_update__ = "10th Feb 2017"


class Hub3cUtility():

    def __init__(self):
        self.current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        print("prepare browser configuration")

    def setup_browser(self, browser, url):
        if browser == 'Firefox': self.driver = webdriver.Firefox()
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
        except Exception as e:
            print(e)
            driver.get_screenshot_as_file('screenshot-%s.png' % self.current_time)

        print(driver.title)
        assert "Hub3c - Home" == driver.title

        time.sleep(3)
        print("take a screenshot")
        driver.get_screenshot_as_file('..\log_test\login-%s.png' % self.current_time)


if __name__ == "__main__":
    pass