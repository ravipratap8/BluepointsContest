import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expect

from pages.contactpage import ContactPage


@pytest.mark.usefixtures("setup")
class BaseClass:
    def waitForPresenceOfElement(self,element, time):
        contactpage = ContactPage(self.browser)
        WebDriverWait(self.browser, 7).until(expect.presence_of_element_located(contactpage.forenameField()))
