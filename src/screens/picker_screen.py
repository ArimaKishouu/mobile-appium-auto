from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_screen import BaseScreen

class PickerScreen(BaseScreen):
    PICKER_SCREEN_TITLE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Pick a date to learn more about it")')
    MONTH_PICKER_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "monthPicker")
    DAY_PICKER_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "dayPicker")
    LEARN_MORE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "learnMore")
    MONTH_PICKER_LIST = (By.ID, "com.appiumpro.the_app:id/select_dialog_listview")
    DAY_PICKER_LIST = (By.ID, "com.appiumpro.the_app:id/select_dialog_listview")

    def is_open(self):
        return self.find(self.PICKER_SCREEN_TITLE)

    def open_month_picker(self):
        self.click(self.MONTH_PICKER_BUTTON)

    def open_day_picker(self):
        self.click(self.DAY_PICKER_BUTTON)

    def pick_month(self, expected_month):
        self.click(expected_month)

    def pick_day(self, expected_day):
        self.click(expected_day)

    def get_month_date(self, locator, expected_month):
        locator_1 = (AppiumBy.ANDROID_UIAUTOMATOR, expected_month)
        return WebDriverWait(
            self.driver, 10
        ).until(
            EC.visibility_of_element_located(locator)
        )

    def get_day_date(self, locator, expected_date):
        locator_1 = (AppiumBy.ANDROID_UIAUTOMATOR, expected_date)
        return WebDriverWait(
            self.driver, 10
        ).until(
            EC.visibility_of_element_located(locator)
        )