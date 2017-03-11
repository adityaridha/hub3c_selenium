import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from faker import Factory
import time

__author__ 		= "Muhammad Aditya Ridharrahman"
__version__ 	= "1.0"
__maintainer__ 	= "Rob Knight"
__email__ 		= "aditya.ridharrahman@geekseat.com.au"
__status__ 		= "development"
__last_update__ = "10th Feb 2017"


USER_NAME 		= "mike@hub3c.com"
PASSWORD 		= "ZXasqw12"
HUB3C_URL		= "https://test.hub3c.com/"
FAKE 			= Factory.create()
BUSINESS		= FAKE.company()
FIRST_NAME 		= FAKE.first_name()
LAST_NAME		= FAKE.last_name()
EMAIL 			= FIRST_NAME+"."+LAST_NAME+"@gmail.com"
PASSWORD		= "ZXasqw12"

class PythonOrgSearch(unittest.TestCase):

	def setUp(self, browser='Firefox' or 'Chrome'):
		if browser == 'Firefox' : self.driver = webdriver.Firefox()
		if browser == 'Chrome' 	: self.driver = webdriver.Chrome("C:\\Python\\selenium\\webdriver\\chromedriver_win32\\chromedriver.exe")

	def test_search_in_python_org(self):
		driver = self.driver
		driver.get(HUB3C_URL)
		self.assertIn(HUB3C_URL, driver.current_url)

		print(driver.title)
		print(driver.current_url)
		select_register = driver.find_element_by_partial_link_text('Create account')
		select_register.click()

		try :
			WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "BusinessName")))
			print("Page is ready!")
		except TimeoutException:
			print("Loading took too much time!")

		fill_account_name = driver.find_element_by_id('BusinessName')
		fill_account_name.send_keys(BUSINESS)
		select_salutation = driver.find_element_by_xpath("html/body/div[1]/div[3]/div/div[2]/div[1]/form/div[2]/span/span")	
		select_salutation.click()
		time.sleep(1)
		select_mr = driver.find_element_by_xpath("//*[@id='Title_listbox']/li[2]")
		select_mr.click()
		
		fill_account_name = driver.find_element_by_id('FirstName')
		fill_account_name.send_keys(FIRST_NAME)
		fill_account_name = driver.find_element_by_id('LastName')
		fill_account_name.send_keys(LAST_NAME)

		time.sleep(1)
		select_time_zone = driver.find_element_by_xpath('html/body/div[1]/div[3]/div/div[2]/div[1]/form/div[5]/span/span/span[1]')
		select_time_zone.click()

		try :
			WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "DefaultTimezone_listbox")))
			print("Selection is ready!")
		except TimeoutException:
			print("Loading took too much time!")


		time_zone = driver.find_element_by_xpath("//*[@id='DefaultTimezone_listbox']/li[82]")
		time_zone.click()

		email = driver.find_element_by_xpath(".//*[@id='EmailAddress']")
		email.send_keys(EMAIL)
		password = driver.find_element_by_xpath(".//*[@id='Password']")
		password.send_keys(PASSWORD)
		retype_password = driver.find_element_by_xpath(".//*[@id='RepeatPassword']")
		retype_password.send_keys(PASSWORD)
		accept_term = driver.find_element_by_xpath("html/body/div[1]/div[3]/div/div[2]/div[1]/form/div[8]/label/span")
		accept_term.click()
		register = driver.find_element_by_xpath(".//*[@id='button-submit']")

		driver.quit()

	   #  user_information = {
    #     "Business Name"              : test_plan['id'],

    #     }

    # print(test_case_id)

    # with open(file.db('testcase_id.txt'), 'w') as f :
    #     json.dump(test_case_id, f)


	# def tearDown(self):
	# 	self.driver.close()

if __name__ == "__main__":
	unittest.main()