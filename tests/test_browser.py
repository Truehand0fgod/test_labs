import page_objects.page as page
from page_objects.locators import MainPageLocators, ResultsPageLocators


class TestMyPow():
    def test_title_matches(self, browser):
        main_page = page.MainPage(browser)
        assert main_page.get_title() == 'This Is Test App Title'

    def test_header_matches(self, browser):
        main_page = page.MainPage(browser)
        assert main_page.get_header_text() == 'This Is Test App Head'

    def test_input_x_exists(self, browser):
        main_page = page.MainPage(browser)
        element = main_page.find_element(*MainPageLocators.X_INPUT)
        assert element is not None

    def test_input_n_exists(self, browser):
        main_page = page.MainPage(browser)
        element = main_page.find_element(*MainPageLocators.N_INPUT)
        assert element is not None

    def test_input_submit_button_exists(self, browser):
        main_page = page.MainPage(browser)
        element = main_page.find_element(*MainPageLocators.SUBMIT_BUTTON)
        assert element is not None

    def test_mypow_correct_data(self, browser):
        main_page = page.MainPage(browser)
        main_page.fill_input_x(9.31)
        main_page.fill_input_n(3)
        main_page.click_submit_button()
        results_page = page.ResultsPage(browser)
        assert results_page.get_result() == '806.9544910000001'

    def test_mypow_wrong_data(self, browser):
        main_page = page.MainPage(browser)
        main_page.fill_input_x(110)
        main_page.fill_input_n(2)
        main_page.click_submit_button()
        results_page = page.ResultsPage(browser)
        assert results_page.get_result() == 'Incorrect data, try again'

