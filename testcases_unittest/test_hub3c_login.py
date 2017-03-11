import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time

__author__ 		= "Muhammad Aditya Ridharrahman"
__version__ 	= "1.0"
__email__ 		= "aditya.ridharrahman@geekseat.com.au"
__status__ 		= "development"
__last_update__ = "10th Feb 2017"


USER_NAME 			= "aditya.ridharrahman@geekseat.com.au"
PASSWORD 			= "ZXasqw12"
HUB3C_URL			= "https://demo.hub3c.com/"
HUB3C_DASHBOARD_URL = "http://test.hub3c.com/Home/Index"

class LoginHub3C(unittest.TestCase):

	def setUp(self, browser='Firefox' or 'Chrome'):
		if browser == 'Firefox' : self.driver = webdriver.Firefox()
		if browser == 'Chrome' 	: self.driver = webdriver.Chrome("C:\\Python\\webdriver\\chromedriver.exe")
		
	def test_login_hub3c(self):
		driver = self.driver
		driver.get(HUB3C_URL)
		self.assertIn(HUB3C_URL, driver.current_url)

		try :
			WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "UserName")))
			print("Page is ready!")
		except TimeoutException:
			print("Loading took too much time!")

		print(driver.title)
		print(driver.current_url)

		print("fill in the user credential")
		username = driver.find_element_by_id("UserName")
		username.send_keys(USER_NAME)
		password = driver.find_element_by_id("Password")
		password.send_keys(PASSWORD)
		login = driver.find_element_by_name('go')
		login.click()
		
		if USER_NAME == 'mike@hub3c.com' :
			time.sleep(2)
			select = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/span")	
			select.click()
			time.sleep(1)
			select.send_keys(Keys.DOWN + Keys.ENTER)
			time.sleep(1)
			select = driver.find_element_by_id("btnSubmit")
			select.click()
			
		try :
			WebDriverWait(driver, 10).until(EC.title_is("Hub3c - Home"))
			print("Page is ready!")
		except TimeoutException:
			print("Login take took too much time!")
			self.assertIn("Hub3c - Home", driver.title)

		# self.assertIn(HUB3C_DASHBOARD_URL, driver.current_url)
		# driver.save_screenshot('capture\login.png')
		time.sleep(1)
		driver.quit()

if __name__ == "__main__":
    unittest.main()