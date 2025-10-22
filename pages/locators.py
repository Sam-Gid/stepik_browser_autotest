from selenium.webdriver.common.by import By



class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_invalid")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
    PRODUCT_ADDED_TEXT = (By.CSS_SELECTOR, ".row > h2")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, ".btn[value='Log In']")
    REGISTER_FORM = (By.CSS_SELECTOR, ".btn[value='Register']")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-lg.btn-primary")
    BOOK_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".price_color")
    ADDED_BOOK_NAME = (By.CSS_SELECTOR, ".alertinner strong")
    ADDED_BOOK_PRICE = (By.CSS_SELECTOR, "#messages .alertinner > p > strong")
    SUCCESSFULLY_ADDED_MESSAGE = (By.CSS_SELECTOR, ".alertinner")


