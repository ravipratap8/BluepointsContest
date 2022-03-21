from pages.locators import Locators
from pages.shoppingpage import ShoppingPage


class CartPage(Locators):
    def __init__(self, browser):
        self.browser = browser

    def verifyCartItems(self, expecteditem, expectedquantity):
        dictOfItemsAndQuantity = {}
        rows = self.browser.find_elements(*Locators.tableRows)
        for eachrow in rows:
            item = eachrow.find_element(*Locators.columnItem).text.strip()
            quantity = eachrow.find_element(*Locators.columnQuantity).get_attribute('value')
            dictOfItemsAndQuantity[item] = quantity
        print(dictOfItemsAndQuantity)
        assert expecteditem in dictOfItemsAndQuantity, f"Expected Item {expecteditem} is not in cart"
        assert dictOfItemsAndQuantity[expecteditem] == expectedquantity, \
            f"Expected Quantity of {expecteditem} is {expectedquantity} but Actual Quantity in cart is {dictOfItemsAndQuantity[expecteditem]}"

    def verifyAllCartSubtotal(self):
        rows = self.browser.find_elements(*Locators.tableRows)
        for eachrow in rows:
            item = eachrow.find_element(*Locators.columnItem).text.strip()
            quantity = eachrow.find_element(*Locators.columnQuantity).get_attribute('value')
            Subtotal = eachrow.find_element(*Locators.columnSubtotal).text.strip().replace('$', '')
            price = eachrow.find_element(*Locators.columnPrice).text.strip().replace('$', '')
            assert float(Subtotal) == float(price) * float(quantity), \
                f"Subtotal of {item} looks incorrect, as per the quantity selected"
