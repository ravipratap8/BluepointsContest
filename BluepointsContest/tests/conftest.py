import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from TestData.test_01_testdata import ContactPageTestData


@pytest.fixture(scope="class")
def setup(request):
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get("https://jupiter.cloud.planittesting.com/#/")
    request.cls.browser = browser
    browser.maximize_window()
    yield
    browser.close()

@pytest.fixture(params=ContactPageTestData.contactPageTestData)
def getData(request):
    return request.param
