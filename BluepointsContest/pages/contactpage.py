from pages.locators import Locators


class ContactPage(Locators):
    def __init__(self, browser):
        self.browser = browser

    def forenameField(self):
        return self.browser.find_element(*Locators.forenameField)

    def surnameField(self):
        return self.browser.find_element(*Locators.surnameField)

    def emailField(self):
        return self.browser.find_element(*Locators.emailField)

    def telephoneField(self):
        return self.browser.find_element(*Locators.telephoneField)

    def messageField(self):
        return self.browser.find_element(*Locators.messageField)

    def submitButton(self):
        return self.browser.find_element(*Locators.submitButton)

    def successMessage(self):
        return self.browser.find_element(*Locators.successMessage)

    def backButton(self):
        return self.browser.find_element(*Locators.backButton)
