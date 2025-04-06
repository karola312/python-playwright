from playwright.sync_api import Page, Locator

class Header:
    cart_button: Locator
    cart_items_quantity_span: Locator

    def __init__(self, page: Page):
        self.page = page
        self.cart_button = page.get_by_test_id("shopping-cart-link")
        self.cart_items_quantity_span = page.get_by_test_id("shopping-cart-badge")
