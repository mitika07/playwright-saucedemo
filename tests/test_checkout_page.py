import time
from playwright.sync_api import sync_playwright, expect, Page
import pytest
from test_configs.configs import TestData
from locators.home_page_locators import HomePageLocators
from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage


class TestCheckoutPage:

    @pytest.mark.parametrize(
        "first_name, last_name, postal_code, expected_error",
        [
            ("", "Doe", "12345", "Error: First Name is required"),        # Empty first name
            ("John", "", "12345", "Error: Last Name is required"),       # Empty last name
            ("John", "Doe", "", "Error: Postal Code is required"),         # Empty postal code
            ("", "", "", "Error: First Name is required"),
            ("John", "Doe", "12345", None),    # All fields filled (valid case)
        ]
    )
    def test_fill_checkout_form(self, page, first_name, last_name, postal_code, expected_error):
        checkout_page = CheckoutPage(page)
        login_page = LoginPage(page)
        home_page = HomePage(page)
        cart_page = CartPage(page)
        login_page.goto()
        login_page.login(TestData.USERNAME, TestData.PASSWORD)
        home_page.add_or_remove_from_cart(item_name="Sauce Labs Bike Light", action="add")
        home_page.go_to_cart()
        cart_page.checkout()
        checkout_page.enter_first_name(first_name)
        checkout_page.enter_last_name(last_name)
        checkout_page.enter_postal_code(postal_code)
        checkout_page.continue_checkout()
        if expected_error:
            checkout_page.get_error_message() == expected_error
            import time
            time.sleep(5)
        else:
            assert cart_page.get_cart_info() == [{'quantity': '1', 'name': 'Sauce Labs Bike Light'}]
        
    def test_cancel_checkout(self, page):
        checkout_page = CheckoutPage(page)
        login_page = LoginPage(page)
        home_page = HomePage(page)
        cart_page = CartPage(page)
        login_page.goto()
        login_page.login(TestData.USERNAME, TestData.PASSWORD)
        home_page.add_or_remove_from_cart(item_name="Sauce Labs Bike Light", action="add")
        home_page.go_to_cart()
        cart_page.checkout()
        checkout_page.fill_checkout_form()
        checkout_page.cancel_checkout()
        assert page.url == "https://www.saucedemo.com/cart.html"
    
    def test_checkout_overview(self, page):
        checkout_page = CheckoutPage(page)
        login_page = LoginPage(page)
        home_page = HomePage(page)
        cart_page = CartPage(page)
        login_page.goto()
        login_page.login(TestData.USERNAME, TestData.PASSWORD)
        home_page.add_or_remove_from_cart(item_name="Sauce Labs Bike Light", action="add")
        home_page.go_to_cart()
        cart_page.checkout()
        checkout_page.fill_checkout_form()
        checkout_page.continue_checkout()
        assert checkout_page.get_checkout_summary() == TestData.CHECKOUT_SUMMARY_BIKE_LIGHT
        assert cart_page.get_cart_info() == [{'quantity': '1', 'name': 'Sauce Labs Bike Light'}]

    def test_finish_checkout(self, page):
        checkout_page = CheckoutPage(page)
        login_page = LoginPage(page)
        home_page = HomePage(page)
        cart_page = CartPage(page)
        login_page.goto()
        login_page.login(TestData.USERNAME, TestData.PASSWORD)
        home_page.add_or_remove_from_cart(item_name="Sauce Labs Bike Light", action="add")
        home_page.go_to_cart()
        cart_page.checkout()
        checkout_page.fill_checkout_form()
        checkout_page.continue_checkout()
        checkout_page.finish_checkout_process()
        assert checkout_page.get_successful_checkout_message() == TestData.SUCCESSFUL_CHECKOUT_MESSAGE

    def test_back_home_button(self, page):
        checkout_page = CheckoutPage(page)
        login_page = LoginPage(page)
        home_page = HomePage(page)
        cart_page = CartPage(page)
        login_page.goto()
        login_page.login(TestData.USERNAME, TestData.PASSWORD)
        home_page.add_or_remove_from_cart(item_name="Sauce Labs Bike Light", action="add")
        home_page.go_to_cart()
        cart_page.checkout()
        checkout_page.fill_checkout_form()
        checkout_page.continue_checkout()
        checkout_page.finish_checkout_process()
        checkout_page.go_back_home()
        # assert page.url == "https://www.saucedemo.com/inventory.html"
        assert False