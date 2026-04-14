from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

from .base_screen import BaseScreen


class HomeScreen(BaseScreen):
    LOGIN_SCREEN_MODULE = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Login Screen")'
    )

    def open_login_screen(self):
        self.click(self.LOGIN_SCREEN_MODULE)