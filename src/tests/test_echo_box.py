from screens import HomeScreen, EchoScreen
from core import generators

import pytest

@pytest.mark.smoke
class TestEchoScreen:
    def test_open_echo_screen(self, driver):
        home_screen = HomeScreen(driver)
        echo_screen = EchoScreen(driver)
        home_screen.open_echo_screen()
        assert echo_screen.is_open()

    def test_send_message(self, driver):
        message = generators.generate_random_message()
        home_screen = HomeScreen(driver)
        echo_screen = EchoScreen(driver)
        home_screen.open_echo_screen()
        echo_screen.input_message(message)
        echo_screen.save_message()
        assert echo_screen.get_saved_message_text(message) == message
