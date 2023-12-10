from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    LOOK_BASKET = (By.XPATH, "//span/a[contains(@href, '/basket')]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_INPUT = (By.NAME, "registration-email")
    REGISTER_PASSWORD_INPUT = (By.NAME, "registration-password1")
    REGISTER_PASSWORD_CONFIRM_INPUT = (By.NAME, "registration-password2")
    REGISTER_BUTTON = (By.NAME, 'registration_submit')




class BasketPageLocators:
    TEXT_THAT_EMPTY = (By.CSS_SELECTOR, "#content_inner>p")
    BASKET_ITEM = (By.CLASS_NAME, 'basket-items')


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_ADD_TO_BASKET_MESSAGE = (By.XPATH, "//div[contains(@class, 'alert-success')]")
    PRODUCT_MESSAGE_NAME = (By.XPATH, "(//div[contains(@class, 'alert')]/strong)[1]")
    PRODUCT_MESSAGE_PRICE = (By.CSS_SELECTOR, "div.alertinner >p>strong")
