class TestData:
    """Test Data"""
    USERNAME = "standard_user"
    EMPTY_STRING = ""
    INVALID_CRED = "invalid"
    PASSWORD = "secret_sauce"
    USERNAME_OR_PASSWORD_REQUIRED_ERROR = "Epic sadface: {} is required"
    INVALID_USERNAME_OR_PASSWORD_ERROR = "Epic sadface: Username and password do not match any user in this service"
    INVENTORY_NAME_LIST = ['Sauce Labs Backpack', 'Sauce Labs Bike Light', 'Sauce Labs Bolt T-Shirt', 'Sauce Labs Fleece Jacket', 'Sauce Labs Onesie', 'Test.allTheThings() T-Shirt (Red)']
    # DESC_INVENTORY_NAME_LIST = ['Test.allTheThings() T-Shirt (Red)', 'Sauce Labs Onesie', 'Sauce Labs Fleece Jacket', 'Sauce Labs Bolt T-Shirt', 'Sauce Labs Bike Light', 'Sauce Labs Backpack']
    INVENTORY_PRICE_LIST = [7.99, 9.99, 15.99, 15.99, 29.99, 49.99]
    # DESC_INVENTORY_PRICE_LIST = [49.99, 29.99, 15.99, 15.99, 9.99, 7.99]
    CART_INFO = [{'quantity': '{}', 'name': '{}'}]
    FIRST_NAME = "John"
    LAST_NAME = "Doe"
    POSTAL_CODE = "12345"
    CHECKOUT_SUMMARY_BIKE_LIGHT = ['Payment Information:', 'SauceCard #31337', 'Shipping Information:', 'Free Pony Express Delivery!', 'Price Total', 'Item total: $9.99', 'Tax: $0.80', 'Total: $10.79']
    SUCCESSFUL_CHECKOUT_MESSAGE = "Thank you for your order! Your order has been dispatched, and will arrive just as fast as the pony can get there!"
