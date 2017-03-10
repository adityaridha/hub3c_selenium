from model.utility import Hub3cUtility

__author__ 		= "Muhammad Aditya Ridharrahman"
__version__ 	= "1.0"
__email__ 		= "aditya.ridharrahman@geekseat.com.au"
__status__ 		= "development"
__last_update__ = "10th Feb 2017"


USER_NAME 			= "aditya.ridharrahman@geekseat.com.au"
PASSWORD 			= "ZXasqw12"
HUB3C_URL			= "https://demo.hub3c.com/"
HUB3C_DASHBOARD_URL = "http://test.hub3c.com/Home/Index"


step = Hub3cUtility()

def func(x):
	return x + 1

def test_answer_2():
	assert func(5) == 6

def test_login_hub3c():
	step.setup_browser(browser="Firefox", url=HUB3C_URL)
	step.login_hub3c(username=USER_NAME, password=PASSWORD)
