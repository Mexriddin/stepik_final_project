from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    main_page = MainPage(browser, link)
    main_page.open()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "https://selenium1py.pythonanywhere.com"
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.go_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_text_empty_basket()