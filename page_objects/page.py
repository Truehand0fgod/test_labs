from page_objects.element import BasePageElement
from page_objects.locators import MainPageLocators, ResultsPageLocators


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def find_element(self, *locator):
        return self.driver.find_element(*locator)


class MainPage(BasePage):
    def get_header_text(self):
        element = self.find_element(*MainPageLocators.PAGE_HEADER)
        return element.text

    def click_submit_button(self):
        element = self.find_element(*MainPageLocators.SUBMIT_BUTTON)
        element.click()

    def fill_input_x(self, data):
        element = self.find_element(*MainPageLocators.X_INPUT)
        element.send_keys(data)

    def fill_input_n(self, data):
        element = self.find_element(*MainPageLocators.N_INPUT)
        element.send_keys(data)


class ResultsPage(MainPage):
    def get_result(self):
        element = self.find_element(*ResultsPageLocators.RESULT)
        return element.text
