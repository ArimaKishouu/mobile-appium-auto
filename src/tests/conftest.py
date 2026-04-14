from pathlib import Path

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

APPIUM_URL = "http://127.0.0.1:4723"

@pytest.fixture()
def driver():
    app_path = Path(__file__).resolve().parent.parent.parent / "apps" / "TheApp.apk"
    assert app_path.exists(), f"APK not found at {app_path}"

    options = UiAutomator2Options().load_capabilities(
        {
            "platformName": "Android",
            "udid": "emulator-5554",
            "automationName": "UiAutomator2",
            "deviceName": "Android Emulator",
            "app": str(app_path),
            "appPackage": "com.appiumpro.the_app",
            "appActivity": "com.appiumpro.the_app.MainActivity",
            "appWaitActivity": "*",
            "appWaitDuration": 60000,
            "autoGrantPermissions": True,
        }
    )

    driver = webdriver.Remote(APPIUM_URL, options=options)
    yield driver
    driver.quit()


