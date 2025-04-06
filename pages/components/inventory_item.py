from playwright.sync_api import Page, Locator

class InventoryItem:

    name: str
    price: str
    item: Locator

    def __init__(self, item: Locator):
        self.item = item
        add_to_cart_button_xpath = "//*[contains(@data-test,'add-to-cart')]"
        self.add_to_cart_button = item.locator(add_to_cart_button_xpath)
        self.name = item.get_by_test_id("inventory-item-name").text_content()
        self.price = item.get_by_test_id("inventory-item-price").text_content()

    def add_item_to_cart(self):
        self.add_to_cart_button.click()

    def get_remove_button(self):
        remove_button_xpath = "//button[contains(@data-test,'remove')]"
        return self.item.locator(remove_button_xpath)
