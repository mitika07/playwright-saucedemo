import time
from playwright.sync_api import sync_playwright, expect, Page
import pytest
from Configs.configs import TestData
from locators.home_page_locators import HomePageLocators
from pages.home_page import HomePage
from pages.login_page import LoginPage

class TestHomePage:


    def test_home_page_header(self, page):
        home_page = HomePage(page)
        login_page = LoginPage(page)
        login_page.goto()
        login_page.login(TestData.USERNAME, TestData.PASSWORD)
        expect(home_page.products_title).to_be_visible()
        expect(home_page.sorting_filter).to_be_visible()

    def test_sorting_default_value(self, page):
        home_page = HomePage(page)
        login_page = LoginPage(page)
        login_page.goto()
        login_page.login(TestData.USERNAME, TestData.PASSWORD)
        expect(home_page.default_sorting).to_be_visible()

    @pytest.mark.parametrize("sorting_value", ["az", "za", "hilo", "lohi"])
    def test_sorting_dropdown_values(self, page, sorting_value):
        home_page = HomePage(page)
        login_page = LoginPage(page)
        home_page.goto()
        login_page.login(TestData.USERNAME, TestData.PASSWORD)
        home_page.click_on_sorting_filter()
        home_page.sorting_filter.select_option(sorting_value)
        expect(home_page.sorting_filter).to_have_value(sorting_value)
    
    @pytest.mark.parametrize("sorting_value", ["az", "za", "lohi", "hilo"])
    def test_sorting_func(self, page, sorting_value):
        home_page = HomePage(page)
        login_page = LoginPage(page)
        home_page.goto()
        login_page.login(TestData.USERNAME, TestData.PASSWORD)
        home_page.click_on_sorting_filter()
        home_page.sorting_filter.select_option(sorting_value)
        if sorting_value == "az":
            assert home_page.get_inventory_list(sort_by="name") == TestData.INVENTORY_NAME_LIST
        elif sorting_value == "za":
            assert home_page.get_inventory_list(sort_by="name") == sorted(TestData.INVENTORY_NAME_LIST, reverse=True)
        elif sorting_value == "lohi":
            assert home_page.get_inventory_list(sort_by="price") == TestData.INVENTORY_PRICE_LIST
        elif sorting_value == "hilo":
            assert home_page.get_inventory_list(sort_by="price") == sorted(TestData.INVENTORY_PRICE_LIST, reverse=True)
