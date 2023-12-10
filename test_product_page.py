import pytest
import time
from .pages.locators import BasePageLocators
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage



@pytest.mark.login
class TestLoginFromProductPage():
    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.go_to_login_page()




class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, request):
        login_page = LoginPage(browser, "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/")
        login_page.open()
        login_page.register_new_user(str(time.time()) + '@fakemail.org', '123455678')
        login_page.is_element_present(*BasePageLocators.USER_ICON)

    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
        product_page.open()
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser,
                                   f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
        product_page.open()
        product_page.add_to_cart()
        product_page.should_be_message_add_to_basket()
        product_page.should_be_name_in_message_add_basket()
        product_page.should_be_price_in_message_add_basket()


promos = ['offer0', 'offer1', 'offer2', 'offer3', 'offer4', 'offer5', 'offer6',
          pytest.param("offer5", marks=pytest.mark.xfail),
          'offer8', 'offer9']


@pytest.mark.need_review
@pytest.mark.parametrize('promo', promos)
def test_guest_can_add_product_to_basket(browser, promo):
    product_page = ProductPage(browser,
                               f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={promo}')
    product_page.open()
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_message_add_to_basket()
    product_page.should_be_name_in_message_add_basket()
    product_page.should_be_price_in_message_add_basket()


@pytest.mark.xfail(reason="Not finished it's a feature")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    product_page.open()
    product_page.add_to_cart()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.xfail(reason="Not finished it's a feature")
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    product_page.open()
    product_page.add_to_cart()
    product_page.should_be_disappear_message()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    product_page = ProductPage(browser, "https://selenium1py.pythonanywhere.com")
    product_page.open()
    product_page.go_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_text_empty_basket()
