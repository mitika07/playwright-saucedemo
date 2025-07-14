import time
from playwright.sync_api import sync_playwright, expect, Page
import pytest
from test_configs.configs import TestData
from locators.home_page_locators import HomePageLocators
from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.login_page import LoginPage

class TestAddToCart:

    def test_product_add_to_cart(self, page):
        home_page = HomePage(page)
        login_page = LoginPage(page)
        login_page.goto()
        login_page.login(TestData.USERNAME, TestData.PASSWORD)
        home_page.add_or_remove_from_cart(item_name="Sauce Labs Bike Light", action="add")
        assert home_page.get_current_cart_item_numbers() == 1

    def test_cart_items(self, page):
        home_page = HomePage(page)
        login_page = LoginPage(page)
        cart_page = CartPage(page)
        login_page.goto()
        login_page.login(TestData.USERNAME, TestData.PASSWORD)
        home_page.add_or_remove_from_cart(item_name="Sauce Labs Bike Light", action="add")
        home_page.add_or_remove_from_cart(item_name="Sauce Labs Backpack", action="add")
        home_page.go_to_cart()
        assert cart_page.get_cart_info() == [{'quantity': '1', 'name': 'Sauce Labs Bike Light'}, {'quantity': '1', 'name': 'Sauce Labs Backpack'}]
        

    def test_cart_number_update(self, page):
        home_page = HomePage(page)
        login_page = LoginPage(page)
        login_page.goto()
        login_page.login(TestData.USERNAME, TestData.PASSWORD)
        home_page.add_or_remove_from_cart(item_name="Sauce Labs Bike Light", action="add")
        home_page.add_or_remove_from_cart(item_name="Sauce Labs Backpack", action="add")
        assert home_page.get_current_cart_item_numbers() == 2
    
    def test_add_to_cart_button_change_to_remove_after_clicked(self, page):
        home_page = HomePage(page)
        login_page = LoginPage(page)
        login_page.goto()
        login_page.login(TestData.USERNAME, TestData.PASSWORD)
        home_page.add_or_remove_from_cart(item_name="Sauce Labs Bike Light", action="add")
        assert home_page.get_product_card_button_text(item_name="Sauce Labs Bike Light") == "Remove"
        
    def test_cart_number_update_after_remove(self, page):
        home_page = HomePage(page)
        login_page = LoginPage(page)
        cart_page = CartPage(page)
        login_page.goto()
        login_page.login(TestData.USERNAME, TestData.PASSWORD)
        home_page.add_or_remove_from_cart(item_name="Sauce Labs Bike Light", action="add")
        home_page.add_or_remove_from_cart(item_name="Sauce Labs Backpack", action="add")
        home_page.add_or_remove_from_cart(item_name="Sauce Labs Backpack", action="remove")
        assert home_page.get_current_cart_item_numbers() == 1
        home_page.go_to_cart()
        assert cart_page.get_cart_info() == [{'quantity': '1', 'name': 'Sauce Labs Bike Light'}]

    def test_remove_item_from_cart_page(self, page):
        home_page = HomePage(page)
        login_page = LoginPage(page)
        cart_page = CartPage(page)
        login_page.goto()
        login_page.login(TestData.USERNAME, TestData.PASSWORD)
        home_page.add_or_remove_from_cart(item_name="Sauce Labs Backpack", action="add")
        home_page.go_to_cart()
        cart_page.remove_from_cart(item_name="Sauce Labs Backpack")
        assert cart_page.get_cart_info() == []
        cart_page.continue_shopping()
        assert home_page.get_current_cart_item_numbers() == None
