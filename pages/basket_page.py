from .base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):

    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_ADDED_TEXT), 'The basket is not empty'


    def basket_is_emtpy_message_presented(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), "The basket is empty message is not present"