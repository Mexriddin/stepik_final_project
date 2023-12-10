import pytest

from .pages.basket_page import BasketPage
from .pages.main_page import MainPage


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_should_see_login_link_on_main_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        main_page = MainPage(browser=browser, url=link)
        main_page.open()
        main_page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_main_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "https://selenium1py.pythonanywhere.com"
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.go_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_text_empty_basket()