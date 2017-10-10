from selenium import webdriver
from faker import Factory

faker = Factory.create()

business    = faker.company()
first_name  = faker.first_name()
last_name   = faker.last_name()
email       = first_name + last_name + "@mailinator.com"
password = "ZXasqw12"

driver = webdriver.Firefox()

''' define URL address '''
driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/Index")

driver.find_element_by_xpath(".//*[@id='BusinessName']").send_keys(business)
driver.find_element_by_xpath("html/body/div[1]/div[3]/div[2]/div[2]/div[1]/form/div[2]/span/span/span[1]").click()
driver.find_element_by_xpath("//*[@id='Title_listbox']/li[2]").click()
driver.find_element_by_xpath(".//*[@id='FirstName']").send_keys(first_name)
driver.find_element_by_xpath(".//*[@id='LastName']").send_keys(last_name)
driver.find_element_by_xpath(".//*[@id='EmailAddress']").send_keys(email)
driver.find_element_by_xpath(".//*[@id='Password']").send_keys(password)
driver.find_element_by_xpath(".//*[@id='RepeatPassword']").send_keys(password)
driver.find_element_by_xpath("html/body/div[1]/div[3]/div[2]/div[2]/div[1]/form/div[7]/label/span").click()
driver.find_element_by_xpath(".//*[@id='button-submit']").click()
driver.get_screenshot_as_file("D:\\works\\hub3c_selenium\\test.png")


print(faker.food())







