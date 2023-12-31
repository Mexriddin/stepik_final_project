from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), \
            "Products item  is resented, but should not be"

    def should_be_text_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_THAT_EMPTY), \
            "Text indicating that the cart is empty is not present"