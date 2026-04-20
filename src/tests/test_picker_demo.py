from screens import HomeScreen, PickerScreen


class TestPickerScreen:
    def test_open_picker_screen(self, driver):
        home_screen = HomeScreen(driver)
        picker_screen = PickerScreen(driver)
        home_screen.open_picker_screen()
        assert picker_screen.is_open()

    def test_pick_some_dates(self, driver):
        home_screen = HomeScreen(driver)
        picker_screen = PickerScreen(driver)
        home_screen.open_picker_screen()
        picker_screen.open_month_picker()
        picker_screen.pick_month("February")
        picker_screen.open_day_picker()
        picker_screen.pick_day("7")
        picker_screen.go_back()