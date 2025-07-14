class LoginPageLocators:
    """Login page locators"""
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = 'input:has-text("Login")'
    LOGIN_ERROR = "css=h3[data-test='error']"
    ERROR_CLOSE_BUTTON = "css=.error-button"
