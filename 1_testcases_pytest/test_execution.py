__author__ 		= "Muhammad Aditya Ridharrahman"
__version__ 	= "1.0"
__email__ 		= "aditya.ridharrahman@geekseat.com.au"
__status__ 		= "development"


import os
import sys
import pytest
from pathlib import Path

root = Path(__file__).parents[1]   #get the root directory
root_model = os.path.join(str(root),'model')
sys.path.append(root_model)

import model

USER_NAME 			= "aditya.ridharrahman@geekseat.com.au"
PASSWORD 			= "ZXasqw12"
HUB3C_URL			= "https://test.hub3c.com/Account/Login"
HUB3C_DASHBOARD_URL = "http://test.hub3c.com/Home/Index"


step = model.Hub3cUtility()

@pytest.mark.skip(reason = None)
def test_login_hub3c():
	step.setup_browser(browser="Chrome", url=HUB3C_URL)
	step.login_hub3c(username=USER_NAME, password=PASSWORD)
	step.logout_hub3c()

@pytest.mark.skip(reason = None)
def test_verify_hired1st():
	step.setup_browser(browser="Chrome", url=HUB3C_URL)
	step.login_hub3c(username=USER_NAME, password=PASSWORD)
	step.verify_hired1st()
	step.logout_hub3c()

def test_register_hub3c():
	step.setup_browser(browser = "Chrome", url = HUB3C_URL)
	step.register_hub3c()