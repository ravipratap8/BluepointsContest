from selenium.webdriver.common.by import By


class Locators:
    # HomePage:
    contactTab = (By.XPATH, "//a[contains(text(),'Contact')]")
    startShoppingButton = (By.XPATH, "//a[contains(text(),'Start Shopping')]")
    cartMenu = (By.XPATH, "//a[contains(text(),'Cart')]")
    # ContactPage:
    forenameField = (By.XPATH, "//input[@id='forename']")
    surnameField = (By.XPATH, "//input[@id='surname']")
    emailField = (By.XPATH, "//input[@id='email']")
    telephoneField = (By.XPATH, "//input[@id='telephone']")
    messageField = (By.XPATH, "//textarea[@id='message']")
    submitButton = (By.XPATH, "//a[text()='Submit']")
    successMessage = (By.XPATH, "//div[contains(@class,'alert-success')]")
    backButton = (By.XPATH, "//a[contains(text(),'Back')]")

    # ShoppingPage:
    def productPriceLocator(self, itemname):
        productPriceLocator = "//li[@class='product ng-scope']//h4[text()='VALUE']/parent::div//span"
        productPriceLocator = productPriceLocator.replace("VALUE", itemname)
        return (By.XPATH, productPriceLocator)

    def buyButtonLocator(self, itemname):
        buyButtonLocator = "//li[@class='product ng-scope']//h4[text()='VALUE']/parent::div//a[text()='Buy']"
        buyButtonLocator = buyButtonLocator.replace("VALUE", itemname)
        return (By.XPATH, buyButtonLocator)

    # CartPage:
    tableRows = (By.XPATH, "//table/tbody/tr")
    columnItem = (By.XPATH, "td[1]")
    columnPrice = (By.XPATH, "td[2]")
    columnQuantity = (By.XPATH, "td[3]/input")
    columnSubtotal = (By.XPATH, "td[4]")
    columnActions = (By.XPATH, "td[5]")
    checkOutButton = (By.XPATH, "//a[contains(text(),'Check Out')]")
