from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

''' define browoser connection '''
# driver  = webdriver.PhantomJS("D:\\programs\\phantomjs-1.9.8-windows\\phantomjs.exe")
driver = webdriver.Chrome()

''' define URL address '''
driver.get("https://test-ntj7zzeiwb.hub3c.com/Bulletin/Home")

print(driver.title)
print(driver.current_url)




email = driver.find_element_by_id("Email")
email.send_keys("marsha@freehub.com")
print("input email")

password = driver.find_element_by_id("Password")
password.send_keys("ZXasqw12")
print("input password")

login = driver.find_element_by_xpath("//button[contains(text(),'Log in')]")
login.click()
print("click login")

time.sleep(5)
#
driver.get("https://test-ntj7zzeiwb.hub3c.com/Bulletin/Home")
time.sleep(2)


driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))



box = driver.find_element_by_xpath("/html/body")
box.send_keys(Keys.TAB + Keys.TAB + "Lorem Ipsum")

Keys.

driver.switch_to.default_content()
driver.find_element_by_xpath('//*[@id="btn-newpost"]').click()
# driver.find_elements_by_xpath(".//*[@id='admin-header']/div/div/div[1]/div[1]/a[1]/i")
# print("login sukses")




