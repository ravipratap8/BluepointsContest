from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Navigate to Application URL
browser = webdriver.Chrome(executable_path="C:/Users/002SGR744/browserdrivers/chromedriver.exe")
browser.get("https://jupiter.cloud.planittesting.com/#/")

# Navigate to Contact Page
browser.find_element(by=By.XPATH, value="//a[contains(text(),'Contact')]").click()  # contactTab
# Fill the form
# testData:
forename = "test"
email = "test@test.com"
message = "please ignore this is just for testing purpose."

time.sleep(2)
# Enter all the details
browser.find_element(by=By.XPATH, value="//input[@id='forename']").send_keys(forename)
# browser.find_element_by_xpath("//input[@id='forename']").send_keys(forename) #forenameField
browser.find_element(by=By.XPATH, value="//input[@id='email']").send_keys(email)  # emailField
# browser.find_element_by_xpath().send_keys(email)
browser.find_element(by=By.XPATH, value="//textarea[@id='message']").send_keys(message)  # messageField
# browser.find_element_by_xpath("//textarea[@id='message']").send_keys(message)

# Submit
browser.find_element(by=By.XPATH, value="//a[text()='Submit']").click()

# wait for sending feedback
time.sleep(5)

# Verify
successMessage = browser.find_element(by=By.XPATH, value="//div[contains(@class,'alert-success')]").text
expectedMessage = "Thanks test, we appreciate your feedback."

assert successMessage == expectedMessage

#close browser
browser.close()