from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

from .base_screen import BaseScreen


class HomeScreen(BaseScreen):
    LOGIN_SCREEN_MODULE = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Login Screen")'
    )

    ECHO_SCREEN_MODULE = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Echo Box")'
    )

    PICKER_SCREEN_MODULE = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Picker Demo")'
    )

    def open_login_screen(self):
        self.click(self.LOGIN_SCREEN_MODULE)

    def open_echo_screen(self):
        self.click(self.ECHO_SCREEN_MODULE)

    def open_picker_screen(self):
        self.click(self.PICKER_SCREEN_MODULE)