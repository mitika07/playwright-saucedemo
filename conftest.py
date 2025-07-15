# conftest.py
import pytest
import logging
from playwright.sync_api import sync_playwright, Page
from datetime import datetime
import os
from test_configs.configs import TestData
from locators.login_page_locators import LoginPageLocators


def setup_logger():
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

    logger = logging.getLogger("test_logger")
    logger.setLevel(logging.INFO)

    # Avoid duplicate handlers
    if not any(isinstance(h, logging.FileHandler) for h in logger.handlers):
        file_handler = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger

logger = setup_logger()

@pytest.fixture(scope="class", autouse=True)
def page():
    """Lanches browser for each test case and quits it after test completion"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        yield page
        browser.close()


def login(page: Page, username=TestData.USERNAME, password=TestData.PASSWORD):
    page.goto("https://www.saucedemo.com/")
    page.fill(LoginPageLocators.USERNAME_INPUT, username)
    page.fill(LoginPageLocators.PASSWORD_INPUT, password)
    page.click(LoginPageLocators.LOGIN_BUTTON)
    page.wait_for_url("https://www.saucedemo.com/inventory.html")  # adjust target URL after login
    logger.info(f"Logged in, current URL: {page.url}")
    assert "inventory.html" in page.url, "Login failed, not on inventory page"


    
def _clear_cart(page: Page):
    remove_buttons = page.locator("text=Remove")
    while remove_buttons.count() > 0:
        logger.info("🗑 Removing an item from cart")
        remove_buttons.nth(0).click()
        page.wait_for_timeout(300)
    logger.info("✅ Cart is empty")


@pytest.fixture(scope="function", autouse=True)
def cleanup_cart(page: Page):
    logger.info("🚿 Cleaning cart before test")
    login(page)
    _clear_cart(page)
    yield
    logger.info("🚿 Cleaning cart after test")
    login(page)
    _clear_cart(page)
