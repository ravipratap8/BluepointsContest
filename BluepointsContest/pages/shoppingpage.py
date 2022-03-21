from pages.locators import Locators


class ShoppingPage(Locators):
    def __init__(self, browser):
        self.browser = browser

    def productPrice(self, itemname):
        return self.browser.find_element(*Locators.productPriceLocator(self, itemname))

    def buyButton(self, itemname):
        print(Locators.buyButtonLocator(self, itemname))
        return self.browser.find_element(*Locators.buyButtonLocator(self, itemname))

    def actionBuyItem(self, itemname, quantity):
        for x in range(quantity):
            self.buyButton(itemname).click()
