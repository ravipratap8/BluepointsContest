from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Navigate to Application URL
browser = webdriver.Chrome(executable_path="C:/Users/002SGR744/browserdrivers/chromedriver.exe")
browser.get("https://jupiter.cloud.planittesting.com/#/")

# Go to shopping Page
browser.find_element(by=By.XPATH, value="//a[contains(text(),'Start Shopping')]").click()

time.sleep(2)
# buy 2 "Funny Cow"
browser.find_element \
    (by=By.XPATH,
     value="//li[@class='product ng-scope']//h4[text()='VALUE']/parent::div//a[text()='Buy']".replace("VALUE",
                                                                                                      "Funny Cow")).click()

browser.find_element \
    (by=By.XPATH,
     value="//li[@class='product ng-scope']//h4[text()='VALUE']/parent::div//a[text()='Buy']".replace("VALUE",
                                                                                                      "Funny Cow")).click()

# buy 1 "Fluffy Bunny"

browser.find_element \
    (by=By.XPATH,
     value="//li[@class='product ng-scope']//h4[text()='VALUE']/parent::div//a[text()='Buy']".replace("VALUE",
                                                                                                      "Fluffy Bunny")).click()

# Go to cart

browser.find_element(by=By.XPATH, value="//a[contains(text(),'Cart')]").click()

time.sleep(2)
# Verify Cart
listOfItems = []
for eachrow in browser.find_elements(by=By.XPATH, value="//table/tbody/tr"):
    items = eachrow.find_element(by=By.XPATH, value="td[3]/input").get_attribute('value')
    print(items)
    listOfItems.append(items)

print(listOfItems)

#close browser
browser.close()