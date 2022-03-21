import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expect
from pages.cartpage import CartPage
from pages.homepage import HomePage
from pages.locators import Locators
from pages.shoppingpage import ShoppingPage
from utilities.BaseClass import BaseClass


class TestCaseThree(BaseClass):

    def test_TC03(self):
        homepage = HomePage(self.browser)
        homepage.startShoppingButton().click()  # shopping page to Contact Page
        # ShopItems
        shoppingpage = ShoppingPage(self.browser)
        # explicit wait
        element = WebDriverWait(self.browser, 3).until(
            expect.presence_of_element_located(Locators.buyButtonLocator(self,"Funny Cow")))

        shoppingpage.actionBuyItem("Stuffed Frog", 2)
        shoppingpage.actionBuyItem("Fluffy Bunny", 5)
        shoppingpage.actionBuyItem("Valentine Bear", 3)
        # Navigate To Cart
        homepage.cartMenu().click()
        # explicit wait
        element = WebDriverWait(self.browser, 3).until(expect.presence_of_element_located(Locators.checkOutButton))

        # verify Cart
        cartpage = CartPage(self.browser)
        cartpage.verifyAllCartSubtotal()
