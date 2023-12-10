import pytest
from .pages.product_page import ProductPage

promos = ['offer0', 'offer1', 'offer2', 'offer3', 'offer4', 'offer5', 'offer6',
          pytest.param("offer5", marks=pytest.mark.xfail),
          'offer8', 'offer9']


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


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_login_page()


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
