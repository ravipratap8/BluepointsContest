from pages.locators import Locators


class HomePage(Locators):
    def __init__(self, browser):
        self.browser = browser

    def contactTab(self):
        return self.browser.find_element(*Locators.contactTab)

    def startShoppingButton(self):
        return self.browser.find_element(*Locators.startShoppingButton)

    def cartMenu(self):
        return self.browser.find_element(*Locators.cartMenu)
