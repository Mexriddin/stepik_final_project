from selenium.webdriver import Keys

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        add_to_cart_button.click()

    def should_be_message_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_ADD_TO_BASKET_MESSAGE), \
            "Not message that the product has been added to the cart"

    def should_be_name_in_message_add_basket(self):
        expect_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        actual_name = self.browser.find_element(*ProductPageLocators.PRODUCT_MESSAGE_NAME).text
        assert expect_name == actual_name, \
            f"The product name in the message '{actual_name}' does not match the product you actually '{expect_name}' added."

    def should_be_price_in_message_add_basket(self):
        expect_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        actual_price = self.browser.find_element(*ProductPageLocators.PRODUCT_MESSAGE_PRICE).text
        assert expect_price in actual_price, \
            f"The product price in the message '{actual_price}' does not match the product you actually '{actual_price}' added."

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_ADD_TO_BASKET_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappear_message(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_ADD_TO_BASKET_MESSAGE), \
            "Success message is not disappear, but should be disappeared"