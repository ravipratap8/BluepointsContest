import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.support.wait import WebDriverWait

from TestData.test_01_testdata import ContactPageTestData
from pages.contactpage import ContactPage
from pages.homepage import HomePage
from pages.locators import Locators
from utilities.BaseClass import BaseClass


class TestCaseOne(BaseClass):

    def test_TC01(self, getData):
        homepage = HomePage(self.browser)
        homepage.contactTab().click()
        # Navigate to Contact Page
        # Fill the form
        # Enter all the details
        contactpage = ContactPage(self.browser)
        # explicit wait
        element = WebDriverWait(self.browser, 5).until(expect.presence_of_element_located(Locators.forenameField))
        contactpage.forenameField().send_keys(getData["forename"])  # forename
        contactpage.emailField().send_keys(getData["email"])  # emailField
        contactpage.messageField().send_keys(getData["message"])  # messageField
        # Submit
        element = WebDriverWait(self.browser, 5).until(expect.presence_of_element_located(Locators.submitButton))
        contactpage.submitButton().click()
        # wait for sending feedback
        # explicit wait
        element = WebDriverWait(self.browser, 15).until(expect.presence_of_element_located(Locators.successMessage))

        # Verify
        successMessage = contactpage.successMessage().text

        expectedMessage = "Thanks test, we appreciate your feedback."

        assert successMessage == expectedMessage
        element = WebDriverWait(self.browser, 5).until(expect.presence_of_element_located(Locators.backButton))
        contactpage.backButton().click()
        element = WebDriverWait(self.browser, 5).until(expect.presence_of_element_located(Locators.forenameField))


