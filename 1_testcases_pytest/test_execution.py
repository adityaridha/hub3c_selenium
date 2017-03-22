import sys
sys.path.append("D:\Work\hub3c_selenium")
import pytest
from model.step_builder import *

__author__ 		= "Muhammad Aditya Ridharrahman"
__version__ 	= "1.0"
__email__ 		= "aditya.ridharrahman@geekseat.com.au"
__status__ 		= "development"


USER_NAME 			= "aditya.ridharrahman@geekseat.com.au"
PASSWORD 			= "ZXasqw12"
HUB3C_URL			= "https://test.hub3c.com/"
HUB3C_DASHBOARD_URL = "http://test.hub3c.com/Home/Index"


step = Hub3cUtility()

@pytest.mark.skip(reason=None)
def test_login_hub3c():
	step.setup_browser(browser="Chrome", url=HUB3C_URL)
	step.login_hub3c(username=USER_NAME, password=PASSWORD)
	step.logout_hub3c()

@pytest.mark.skip(reason=None)
def test_verify_hired1st():
	step.setup_browser(browser="Chrome", url=HUB3C_URL)
	step.login_hub3c(username=USER_NAME, password=PASSWORD)
	step.verify_hired1st()
	step.logout_hub3c()

def test_register_hub3c():
	step.setup_browser(browser="Chrome", url=HUB3C_URL)
	step.register_hub3c()