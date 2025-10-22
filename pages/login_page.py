from .base_page import BasePage
from .locators import BasePageLocators
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



class LoginPage(BasePage):

    def register_new_user(self, email, password):

        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()

        input_email = self.browser.find_element(By.CSS_SELECTOR, "[type=email][name=registration-email]")
        input_email.send_keys(email)

        input_password = self.browser.find_element(By.CSS_SELECTOR, "[type=password][name=registration-password1]")
        input_password.send_keys(password)

        input_password_confirm = self.browser.find_element(By.CSS_SELECTOR, "[type=password][name=registration-password2]")
        input_password_confirm.send_keys(password)

        register_button = WebDriverWait(self.browser, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "[type=submit][value=Register]")))
        register_button.click()

        assert self.should_be_authorized(), 'User registration was not successful'

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

        return LoginPage


    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, f"Expected 'login' in UTL, but got {self.browser.current_url}"


    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"


    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"