from locators.checkout_page_locators import CheckoutPageLocators
from Configs.configs import TestData


class CheckoutPage:


    def __init__(self, page):
        self.page = page
        self.first_name = page.locator(CheckoutPageLocators.FIRST_NAME)
        self.last_name = page.locator(CheckoutPageLocators.LAST_NAME)
        self.postal_code = page.locator(CheckoutPageLocators.POSTAL_CODE)
        self.cancel_btn = page.locator(CheckoutPageLocators.CANCEL_BTN)
        self.checkout_btn = page.locator(CheckoutPageLocators.CHECKOUT_BTN)
        self.page_title = page.locator(CheckoutPageLocators.PAGE_TITLE)
        self.error_message = self.page.locator(CheckoutPageLocators.ERROR_MESSAGE)
        self.summary_elements = page.locator(CheckoutPageLocators.SUMMARY_ELEMENTS)
        self.finish_checkout = page.locator(CheckoutPageLocators.FINISH_CHECKOUT)
        self.back_home = page.locator(CheckoutPageLocators.BACK_HOME)
        self.successful_checkout_header = page.locator(CheckoutPageLocators.SUCCESSFUL_CHECKOUT_HEADER)
        self.successful_checkout_text = page.locator(CheckoutPageLocators.SUCCESSFUL_CHECKOUT_TEXT)

    
    def enter_first_name(self, first_name):
        self.first_name.fill(first_name)

    def enter_last_name(self, last_name):
        self.last_name.fill(last_name)
    
    def enter_postal_code(self, postal_code):
        self.postal_code.fill(postal_code)
    
    def cancel_checkout(self):
        self.cancel_btn.click()
    
    def continue_checkout(self):
        self.checkout_btn.click()
    
    def get_page_title(self):
        return self.page_title.text_content()

    def get_error_message(self):
        error = self.error_message.text_content()
        return error
    
    def fill_checkout_form(self):
        self.enter_first_name(TestData.FIRST_NAME)
        self.enter_last_name(TestData.LAST_NAME)
        self.enter_postal_code(TestData.POSTAL_CODE)
    
    def get_checkout_summary(self):
        texts = []
        count = self.summary_elements.count()
        for i in range(count):
            text = self.summary_elements.nth(i).inner_text()
            texts.append(text.strip())
        print(texts)
        return texts
    
    def finish_checkout_process(self):
        self.finish_checkout.click()
    
    def get_successful_checkout_message(self):
        header = self.successful_checkout_header.inner_text()
        text = self.successful_checkout_text.inner_text()
        message = header + " " + text
        print(message)
        return message

    def go_back_home(self):
        self.finish_checkout.click()
