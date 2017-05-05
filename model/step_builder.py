from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from datetime import datetime
from faker import Factory
import csv
import time

__author__      = "Muhammad Aditya Ridharrahman"
__version__     = "1.0"
__email__       = "aditya.ridharrahman@geekseat.com.au"
__status__      = "development"
__last_update__ = "10th Feb 2017"


class Hub3cUtility() :

    def __init__(self):
        self.current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        print("prepare browser configuration")

    def setup_browser(self, browser, url):
        if browser == 'Firefox': self.driver = webdriver.Firefox()
        if browser == 'Chrome' : self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        self.driver.get(url)
        assert url == self.driver.current_url

    def close_browser(self):
        print("closing the browser")
        self.driver.quit()

    def login_hub3c(self, username, password):
        driver = self.driver
        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "UserName")))
            print("Login page is ready!")
        except TimeoutException:
            print("Loading took too much time!")

        print("fill in the user credential")
        driver.find_element_by_id("UserName").send_keys(username)
        driver.find_element_by_id("Password").send_keys(password)
        driver.find_element_by_name('go').click()
        time.sleep(5)

        if username == 'mike@hub3c.com':
            time.sleep(2)
            driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/span").click()
            time.sleep(1)
            select.send_keys(Keys.DOWN + Keys.ENTER)
            time.sleep(1)
            driver.find_element_by_id("btnSubmit").click()

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

    def logout_hub3c(self):
        self.driver.find_element_by_xpath(".//*[@id='sidebar-left']/div[1]/div/nav/ul/li[8]/a/span").click()
        self.close_browser()

    def verify_hired1st(self):
        driver = self.driver
        driver.find_element_by_xpath(".//*[@id='25']/a").click()

    def register_hub3c(self):

        fake = Factory.create()
        business = fake.company()
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = first_name + "." + last_name + "@gmail.com"
        password = "ZXasqw12"

        driver = self.driver
        driver.find_element_by_partial_link_text('Create account').click()

        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "BusinessName")))
            print("Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")

        driver.find_element_by_id('BusinessName').send_keys(business)
        driver.find_element_by_xpath("html/body/div[1]/div[3]/div/div[2]/div[1]/form/div[2]/span/span").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='Title_listbox']/li[2]").click()

        driver.find_element_by_id('FirstName').send_keys(first_name)
        driver.find_element_by_id('LastName').send_keys(last_name)

        time.sleep(1)
        driver.find_element_by_xpath('html/body/div[1]/div[3]/div/div[2]/div[1]/form/div[5]/span/span/span[1]').click()

        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "DefaultTimezone_listbox")))
            print("Selection is ready!")
        except TimeoutException:
            print("Loading took too much time!")

        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='DefaultTimezone_listbox']/li[82]").click()

        driver.find_element_by_xpath(".//*[@id='EmailAddress']").send_keys(email)
        driver.find_element_by_xpath(".//*[@id='Password']").send_keys(password)
        driver.find_element_by_xpath(".//*[@id='RepeatPassword']").send_keys(password)
        driver.find_element_by_xpath("html/body/div[1]/div[3]/div/div[2]/div[1]/form/div[8]/label/span").click()
        print(driver.find_element_by_xpath(".//*[@id='button-submit']"))

        driver.find_element_by_xpath(".//*[@id='button-submit']").click()

        with open('registration.csv', 'a') as csvfile:
            registration_data = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            registration_data.writerow([driver.current_url, email, password, first_name, last_name])

        driver.quit()


if __name__ == "__main__":
    pass