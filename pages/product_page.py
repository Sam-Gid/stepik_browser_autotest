import math
from pages.base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException




class ProductPage(BasePage):

    def add_product_to_basket(self):

        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text


        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

        def solve_quiz_and_get_code():
            alert = self.browser.switch_to.alert
            x = alert.text.split(" ")[2]
            answer = str(math.log(abs((12 * math.sin(float(x))))))
            alert.send_keys(answer)
            alert.accept()
            try:
                alert = self.browser.switch_to.alert
                alert_text = alert.text
                print(f"Your code: {alert_text}")
                alert.accept()
            except NoAlertPresentException:
                print("No second alert presented")

        def check_product_exist(name, price):

            added_book_name = self.browser.find_element(*ProductPageLocators.ADDED_BOOK_NAME).text
            added_book_price = self.browser.find_element(*ProductPageLocators.ADDED_BOOK_PRICE).text

            assert (
                        name == added_book_name and price == added_book_price), "Product was not added to the basket"

        solve_quiz_and_get_code()
        check_product_exist(book_name, book_price)


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESSFULLY_ADDED_MESSAGE), \
            "Success message is presented, but should not be"


    def should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESSFULLY_ADDED_MESSAGE), "Success message is presented, but should disappear"