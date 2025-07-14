from locators.home_page_locators import HomePageLocators
from playwright.sync_api import Page

from playwright.sync_api import TimeoutError
class HomePage:
    """Login page methods"""
    def __init__(self, page: Page):
        self.page = page
        self.inventory_list = page.locator(HomePageLocators.HOME_PAGE_LANDING_INVENTORY)
        self.products_title = page.locator(HomePageLocators.HOME_PAGE_TITLE)
        self.sorting_filter = page.locator(HomePageLocators.SORTING_FILTER)
        self.default_sorting = page.locator(HomePageLocators.DEFAULT_SORTING)
        self.inventory_item_name = self.inventory_list.locator(HomePageLocators.INVENTORY_ITEM_PROPERTY.format("name"))
        self.inventory_item_price = self.inventory_list.locator(HomePageLocators.INVENTORY_ITEM_PROPERTY.format("price"))
        self.inventory_item = self.inventory_list.locator(HomePageLocators.INVENTORY_ITEM)
        self.add_to_cart_btn = page.locator(HomePageLocators.ADD_TO_CART_BUTTON)
        self.cart_link = page.locator(HomePageLocators.CART_LINK)

    def goto(self):
        self.page.goto("https://www.saucedemo.com/")
    
    def click_on_sorting_filter(self):
        self.sorting_filter.click()

    def get_total_inventory_count(self, inventory):
        if inventory == "name":
            inventory_count = self.inventory_item_name.count()
        elif inventory == "price":
            inventory_count = self.inventory_item_price.count()
        else:
            raise ValueError("Inventory parameter should be name or price")
        return inventory_count

    def get_inventory_list(self, sort_by: str):
        item_list = []
        inventory_list = []
        if sort_by == "price":
            item_list = self.inventory_item_price.all()
        else:
            item_list = self.inventory_item_name.all()
        for each_item in item_list:
            value = each_item.text_content()
            final_value = value.replace('$', '')
            inventory_list.append(final_value)
            if sort_by == "price":
                inventory_list = [float(price) for price in inventory_list]
        # if sort == "asc":
        #     inventory_list.sort()
        # else:
        #     inventory_list.sort(reverse=True)
        print(inventory_list)
        return inventory_list

    def add_or_remove_from_cart(self, item_name, action):
        product_card = self.inventory_item.filter(has=self.page.get_by_text(item_name))
        print("===============")
        print("!!!!!!!!!!!!!!!")
        print(f"action: {action}")
        if action.lower() == "add":
            product_btn = product_card.get_by_role("button", name="Add to cart")
            product_btn.click()
        elif action.lower() == "remove":
            product_btn = product_card.get_by_role("button", name="Remove")
            product_btn.click()
        else:
            raise ValueError("Invalid action. Action should be 'add' or 'remove'")
    
    def get_product_card_button_text(self, item_name):
        product_card = self.inventory_item.filter(has=self.page.get_by_text(item_name))
        if product_card.get_by_role("button", name="Remove"):
            return "Remove"
        elif product_card.get_by_role("button", name="Add to cart"):
            return "Add to cart"
        else:
            return False

    def get_current_cart_item_numbers(self):
        cart_value = self.cart_link.text_content()
        if cart_value:
            cart_items = int(cart_value)
            return cart_items
        else:
            return None

    def go_to_cart(self):
        self.cart_link.click()
