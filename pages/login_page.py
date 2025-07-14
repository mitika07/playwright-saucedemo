from locators.login_page_locators import LoginPageLocators

class LoginPage:
    """Login page methods"""
    def __init__(self, page):
        self.page = page
        self.username_input = page.locator(LoginPageLocators.USERNAME_INPUT)
        self.password_input = page.locator(LoginPageLocators.PASSWORD_INPUT)
        self.login_button = page.locator(LoginPageLocators.LOGIN_BUTTON)
        self.login_error = page.locator(LoginPageLocators.LOGIN_ERROR)
        self.error_close_button = page.locator(LoginPageLocators.ERROR_CLOSE_BUTTON)
        

    def goto(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def close_error_message(self):
        self.error_close_button.click()