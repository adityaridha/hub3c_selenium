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


USER_NAME 			= "marsha@freehub.com"
PASSWORD 			= "ZXasqw12"
HUB3C_URL			= "https://test-ntj7zzeiwb.hub3c.com/"
HUB3C_DASHBOARD_URL = "http://test.hub3c.com/Home/Index"
AUTH_URL			= "https://test-auth-d2kluue7bb.hub3c.com/account/login?returnUrl=%2Fconnect%2Fauthorize%2Flogin%3Fclient_id%3Dweb-app%26redirect_uri%3Dhttps%253A%252F%252Ftest-ntj7zzeiwb.hub3c.com%26response_mode%3Dform_post%26response_type%3Dcode%2520id_token%26scope%3Dopenid%2520profile%2520offline_access%2520auth-api%26state%3DOpenIdConnect.AuthenticationProperties%253DBlBx0bfLwzLjHikinRt7GRnBqoCBZpS-nLHLSyHfp75Rm7dLs-K0vWmN-D91FqU-LuHUcQ2z2Xd5PhpWkcVOE1j7s1j1wY9QRgt7tEyd30byZSY-CoP3J7ZoNIk4HHmaQK7G4p_PCpkKwI_3AT2fN6Fvnmj-BZbPzQXOKJjRP8PF30JHwRxCXKdZ0_8mJGOcTR3jyLh6BomPOXrLPPx45yy8-87DHLN2ycUOY0rLXgc%26nonce%3D636413899118312578.NjdjOTg1ZTEtMDlmNC00Y2I3LWJlZGQtMmRkZWZhM2VhODYwZThlNWY4ZWItZDRjNi00Mjc0LWE2ZWUtZGFiMTE2YTgxZjNk%26domain_hint%3Dtest-ntj7zzeiwb%26post_logout_redirect_uri%3Dhttps%253A%252F%252Ftest-ntj7zzeiwb.hub3c.com"

class LoginHub3C(unittest.TestCase):

	def setUp(self, browser='Phantom' or 'Chrome'):
		if browser == 'Phantom' : self.driver = webdriver.PhantomJS("D:\\programs\\phantomjs-1.9.8-windows\\phantomjs.exe")
		if browser == 'Chrome' 	: self.driver = webdriver.Chrome()
		if browser == 'Firefox' : self.driver = webdriver.Firefox()
		#phantom 1.9 = "D:\\programs\\phantomjs-1.9.8-windows\\phantomjs.exe"

	# def  setUp(self):
	# 	# this is how you set up a test to run on Sauce Labs
	# 	desired_cap = {
	# 		'platform': "Mac OS X 10.9",
	# 		'browserName': "chrome",
	# 		'version': "31",
	# 	}
	# 	self.driver = webdriver.Remote(
	# 		command_executor='http://adityaridha:3e23cd13-d55f-49e6-8daf-80bcd1e1bfc1@ondemand.saucelabs.com:80/wd/hub',
	# 		desired_capabilities=desired_cap)

	def test_login_hub3c(self):
		driver = self.driver
		driver.maximize_window()
		driver.get(HUB3C_URL)

		driver_type = str(type(driver))
		print(driver_type)
		if driver_type == "<class 'selenium.webdriver.phantomjs.webdriver.WebDriver'>":
			phantom = True
			print("Driver = PhantomJS")

		try :
			WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "Email")))
			print("Login page ready...")
		except TimeoutException:
			print("Loading took too much time!")

		print(driver.title)

		print("fill in the user credential")
		username = driver.find_element_by_id("Email")
		username.send_keys(USER_NAME)
		print("send emaal")
		password = driver.find_element_by_id("Password")
		password.send_keys(PASSWORD)
		print("send password")
		login = driver.find_element_by_xpath("//button[contains(text(),'Log in')]")
		driver.execute_script("arguments[0].click();", login)
		# login.click()
		print("click login button")

		if USER_NAME == 'mike@hub3c.com' :
			time.sleep(2)
			select = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/span")	
			select.click()
			time.sleep(1)
			select.send_keys(Keys.DOWN + Keys.ENTER)
			time.sleep(1)
			select = driver.find_element_by_id("btnSubmit")
			select.click()

		print("wait for home page")
		print(driver.title)


		try :
			WebDriverWait(driver, 30).until(
				EC.presence_of_element_located((By.XPATH, ".//*[@id='scheduler']/table/tbody/tr[2]/td/div")))
			print("Page is ready!")
		except TimeoutException:
			print("Login take took too much time!")
			self.assertIn("Job2Job - Home", driver.title)

		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Subscription Expired')]")))
			print("Ada subscription expired")
			subscription_popup = driver.find_element_by_xpath("//button[contains(text(),'OK')]")
			if phantom == True :
				driver.execute_script("arguments[0].click();", subscription_popup)
			subscription_popup.click()

		except TimeoutException:
			print("All subscription good")




		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, ".//*[@id='releasenotes_wnd_title']")))
			print("Ada release note")
			release_note = driver.find_elements_by_xpath("html/body/div[12]/div[1]/div/a/span")
			if phantom == True :
				driver.execute_script("arguments[0].click();", release_note)
			release_note.click()

		except TimeoutException:
			print("Ga ada release note")


		print("Done")

		driver.quit()

if __name__ == "__main__":
    unittest.main()