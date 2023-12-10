from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_BUTTON)
        login_link.click()

    def should_be_login_page(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_BUTTON), "Login link is not presented"
