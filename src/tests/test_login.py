from screens import LoginScreen, HomeScreen

import pytest

@pytest.mark.smoke
class TestLoginScreen:
    def test_open_login_screen(self, driver):
        home_screen = HomeScreen(driver)
        login_screen = LoginScreen(driver)
        home_screen.open_login_screen()
        assert login_screen.is_open()

    def test_successful_login(self, driver):
        home_screen = HomeScreen(driver)
        login_screen = LoginScreen(driver)
        home_screen.open_login_screen()
        login_screen.enter_username("alice")
        login_screen.enter_password("mypassword")
        login_screen.tap_login()
        assert login_screen.is_successful_login()

    @pytest.mark.parametrize(
        "username,password", [
            ('alice', 'adad'),
            ('alice', '2344242'),
            ('alalala', 'ulululu')
        ],
        ids=
        [
            "gavno1",
            "gavno2",
            "gavno3",
        ]
    )
    def test_unsuccessful_login(self, driver, username, password):
        home_screen = HomeScreen(driver)
        login_screen = LoginScreen(driver)
        home_screen.open_login_screen()
        login_screen.enter_username(username)
        login_screen.enter_password(password)
        login_screen.tap_login()
        assert login_screen.is_unsuccessful_login()










