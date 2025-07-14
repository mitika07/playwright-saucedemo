from locators.cart_page_locators import CartPageLocators

class CartPage:
    """Login page methods"""
    def __init__(self, page):
        self.page = page
        self.cart_list = self.page.locator(CartPageLocators.CART_LIST)
        self.cart_items = self.page.locator(f"{CartPageLocators.CART_LIST} {CartPageLocators.CART_ITEM}")
        self.continue_shopping_btn = self.page.locator(CartPageLocators.CONTINUE_SHOPPING)
        self.checkout_btn = self.page.locator(CartPageLocators.CHECKOUT_BTN)
    
    def get_cart_info(self):
        total_cart_items = self.cart_items.count()
        items = []
        for each in range(total_cart_items):
            item = self.cart_items.nth(each)
            quantity = item.locator(".cart_quantity").inner_text()
            item_name = item.locator(".inventory_item_name").inner_text()
            items.append({"quantity": quantity, "name": item_name})
        print(items)
        return items

    def remove_from_cart(self, item_name):
        item = self.cart_items.filter(has=self.page.get_by_text(item_name))
        remove_btn = item.get_by_role("button", name="Remove")
        remove_btn.click()
    
    def continue_shopping(self):
        self.continue_shopping_btn.click()
    
    def checkout(self):
        self.checkout_btn.click()
