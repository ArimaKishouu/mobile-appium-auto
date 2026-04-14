from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_screen import BaseScreen


class LoginScreen(BaseScreen):
    LOGIN_INPUT = (AppiumBy.ACCESSIBILITY_ID, "username")
    PASSWORD_INPUT = (AppiumBy.ACCESSIBILITY_ID, "password")
    LOGIN_BTN = (AppiumBy.ACCESSIBILITY_ID, "loginBtn")
    SUCCESSFUL_TITLE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Secret Area")')
    LOGOUT_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'content-desc("Logout")')
    LOGIN_TITLE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Login")')
    UNSUCCESSFUL_LOGIN_MESSAGE = (By.ID, "android:id/message")

    def is_open(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.LOGIN_TITLE))

    def enter_username(self, value):
        self.type(self.LOGIN_INPUT, value)

    def enter_password(self, value):
        self.type(self.PASSWORD_INPUT, value)

    def tap_login(self):
        self.click(self.LOGIN_BTN)

    def is_successful_login(self):
        return self.find(self.SUCCESSFUL_TITLE).text

    def is_unsuccessful_login(self):
        return self.find(self.UNSUCCESSFUL_LOGIN_MESSAGE).text