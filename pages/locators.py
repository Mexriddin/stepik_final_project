from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_ADD_TO_BASKET_MESSAGE = (By.XPATH, "//div[contains(@class, 'alert-success')]")
    PRODUCT_MESSAGE_NAME = (By.XPATH, "(//div[contains(@class, 'alert')]/strong)[1]")
    PRODUCT_MESSAGE_PRICE = (By.CSS_SELECTOR, "div.alertinner >p>strong")
