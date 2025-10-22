from pages.locators import BasePageLocators, BasketPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as ec





class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(1)



    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True


    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False


    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True


    def go_to_login_page(self):
        from .login_page import LoginPage

        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

        return LoginPage(browser=self.browser, url=self.browser.current_url)


    def go_to_basket(self):
        self.browser.find_element(*BasePageLocators.BASKET_BUTTON).click()


    def open(self):
        self.browser.get(self.url)


    def should_be_authorized(self):
        try:
            WebDriverWait(self.browser, 10).until(ec.visibility_of_element_located(BasePageLocators.USER_ICON))
            return True
        except TimeoutException:
            assert False, 'User is not authorized'


    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"