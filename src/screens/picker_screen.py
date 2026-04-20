from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By


from .base_screen import BaseScreen

class PickerScreen(BaseScreen):
    PICKER_SCREEN_TITLE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Pick a date to learn more about it")')
    MONTH_PICKER_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "monthPicker")
    DAY_PICKER_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "dayPicker")
    LEARN_MORE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "learnMore")

    def is_open(self):
        return self.find(self.PICKER_SCREEN_TITLE)

    def open_month_picker(self):
        self.click(self.MONTH_PICKER_BUTTON)

    def open_day_picker(self):
        self.click(self.DAY_PICKER_BUTTON)

    def pick_day(self, expected_day):
        self.click((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{expected_day}")'))

    def pick_month(self, expected_month):
        self.click((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{expected_month}")'))
