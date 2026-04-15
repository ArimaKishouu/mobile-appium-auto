from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_screen import BaseScreen

class EchoScreen(BaseScreen):
    ECHO_SCREEN_TITLE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Echo Screen")')
    MESSAGE_INPUT = (AppiumBy.ACCESSIBILITY_ID, 'messageInput')
    MESSAGE_SAVE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'messageSaveBtn')
    USER_MESSAGE_TITLE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Here\'s what you said before:")')

    def is_open(self):
        return self.find(self.ECHO_SCREEN_TITLE)

    def input_message(self, value):
        self.type(self.MESSAGE_INPUT, value)

    def save_message(self):
        self.click(self.MESSAGE_SAVE_BUTTON)

    def get_saved_message_text(self, expected_message):
        locator = (AppiumBy.ACCESSIBILITY_ID, expected_message)
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        ).text


