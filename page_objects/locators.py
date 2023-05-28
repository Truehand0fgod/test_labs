from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    SUBMIT_BUTTON = (By.ID, 'submit')
    X_INPUT = (By.ID, 'x')
    N_INPUT = (By.ID, 'n')
    PAGE_HEADER = (By.TAG_NAME, 'h1')
    PAGE_TITLE = (By.TAG_NAME, 'title')

class ResultsPageLocators(MainPageLocators):
    RESULT = (By.ID, 'result')