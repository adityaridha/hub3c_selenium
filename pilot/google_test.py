import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
 



# # create a new Firefox session
# driver = webdriver.Firefox()
# driver.implicitly_wait(30)
# driver.maximize_window()
 
# # navigate to the application home page
# driver.get("http://www.google.com")
 
# # get the search textbox
# search_field = driver.find_element_by_id("lst-ib")
# search_field.clear()
 
# # enter search keyword and submit
# search_field.send_keys("Selenium WebDriver Interview questions")
# search_field.submit()
 
# # get the list of elements which are displayed after the search
# # currently on result page using find_elements_by_class_name  method
# lists= driver.find_elements_by_class_name("_Rm")
 
# # get the number of elements found
# print ('found' + str(len(lists)) + 'search')
 
# # iterate through each element and print the text that is
# # name of the search
 
# i=0
# for listitem in lists:
#    print (listitem)
#    i=i+1
#    if(i>10):
#       break
 
# close the browser window
# driver.quit()



