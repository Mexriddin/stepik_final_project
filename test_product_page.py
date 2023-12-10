import pytest
from .pages.product_page import ProductPage

promos = ['offer0', 'offer1', 'offer2', 'offer3', 'offer4', 'offer5', 'offer6',
          pytest.param("offer5", marks=pytest.mark.xfail),
          'offer8', 'offer9']


@pytest.mark.parametrize('promo', promos)
def test_guest_can_add_product_to_basket(browser, promo):
    product_page = ProductPage(browser, f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={promo}')
    product_page.open()
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_message_add_to_basket()
    product_page.should_be_name_in_message_add_basket()
    product_page.should_be_price_in_message_add_basket()
