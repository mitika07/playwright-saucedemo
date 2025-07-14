from playwright.sync_api import sync_playwright, expect, Page
import pytest
from Configs.configs import TestData
from locators.login_page_locators import LoginPageLocators
from pages.home_page import HomePage
from pages.login_page import LoginPage

class TestLoginPage:

    @pytest.mark.parametrize("username,password,expected_error", [
        (TestData.EMPTY_STRING, TestData.PASSWORD, TestData.USERNAME_OR_PASSWORD_REQUIRED_ERROR.format("Username")),
        (TestData.EMPTY_STRING, TestData.EMPTY_STRING, TestData.USERNAME_OR_PASSWORD_REQUIRED_ERROR.format("Username")),
        (TestData.USERNAME, TestData.EMPTY_STRING, TestData.USERNAME_OR_PASSWORD_REQUIRED_ERROR.format("Password")),
        (TestData.INVALID_CRED, TestData.PASSWORD, TestData.INVALID_USERNAME_OR_PASSWORD_ERROR),
        (TestData.USERNAME, TestData.INVALID_CRED, TestData.INVALID_USERNAME_OR_PASSWORD_ERROR)
    ])
    def test_invalid_logins(self, page, username, password, expected_error):
        login_page = LoginPage(page)
        login_page.goto()
        login_page.login(username, password)
        expect(login_page.login_error).to_be_visible()
        expect(login_page.login_error).to_have_text(expected_error)

    def test_close_error_message(self, page):
        login_page = LoginPage(page)
        login_page.goto()
        login_page.login(TestData.INVALID_CRED, TestData.INVALID_CRED)
        expect(login_page.error_close_button).to_be_visible()
        login_page.close_error_message()
        expect(login_page.login_error).not_to_be_visible()

    def test_valid_login(self, page):
        home_page = HomePage(page)
        login_page = LoginPage(page)
        home_page.goto()
        login_page.login(TestData.USERNAME, TestData.PASSWORD)
        expect(home_page.inventory_list).to_be_visible()


# To run the function
# test_browser()
