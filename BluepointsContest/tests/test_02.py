import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expect
from pages.cartpage import CartPage
from pages.homepage import HomePage
from pages.locators import Locators
from pages.shoppingpage import ShoppingPage
from utilities.BaseClass import BaseClass


class TestCaseTwo(BaseClass):

    def test_TC02(self):
        homepage = HomePage(self.browser)
        homepage.startShoppingButton().click()  # shopping page to Contact Page
        # ShopItems
        shoppingpage = ShoppingPage(self.browser)
        # explicit wait
        element = WebDriverWait(self.browser, 3).until(expect.presence_of_element_located(Locators.buyButtonLocator(self,"Funny Cow")))
        shoppingpage.actionBuyItem("Funny Cow", 2)  # buy Funny cow 2 times.
        shoppingpage.actionBuyItem("Fluffy Bunny", 1)  # buy Fluffy Bunny 1 time.
        # Navigate To Cart
        homepage.cartMenu().click()
        # verify Cart
        cartpage = CartPage(self.browser)
        # explicit wait
        element = WebDriverWait(self.browser, 3).until(expect.presence_of_element_located(Locators.checkOutButton))
        cartpage.verifyCartItems("Funny Cow", "2")
        cartpage.verifyCartItems("Fluffy Bunny", "1")
