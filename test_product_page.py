import time
import pytest
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.product_page import ProductPage



@pytest.mark.act_with_registration
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com"

        login_page = LoginPage(browser, link)
        login_page.open()

        email = str(time.time()) + "@fmail.com"

        login_page.register_new_user(email, "Sam190789")

        self.browser = browser

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

        page = ProductPage(browser, link)
        page.open()

        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

        page = ProductPage(browser, link)
        page.open()

        page.add_product_to_basket()


def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

    page = ProductPage(browser, link)
    page.open()

    page.add_product_to_basket()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

    page = ProductPage(browser, link)
    page.open()

    page.add_product_to_basket()

    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

    page = ProductPage(browser, link)
    page.open()

    page.should_not_be_success_message()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

    page = BasketPage(browser, link)
    page.open()

    page.go_to_basket()

    page.basket_is_empty()
    page.basket_is_emtpy_message_presented()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

    page = ProductPage(browser, link)
    page.open()

    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

    page = ProductPage(browser, link)
    page.open()

    page.go_to_login_page()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

    page = ProductPage(browser, link)
    page.open()

    page.add_product_to_basket()

    page.should_disappear()


