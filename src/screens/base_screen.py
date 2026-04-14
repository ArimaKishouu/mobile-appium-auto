from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseScreen:

    def __init__(self, driver):
        self.driver = driver

    def find(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
            )

    def click(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def type (self, locator, value, clear_first=True):
        element = self.find(locator)
        if clear_first:
            element.clear()
        element.send_keys(value)

    def get_text (self, locator):
        return self.find(locator).text





