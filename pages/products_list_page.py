from playwright.sync_api import Page, expect
from .components.header import Header
from .components.inventory_item import InventoryItem

class ProductsListPage:

    header: Header

    def __init__(self, page: Page):
        self.page = page
        self.header = Header(page)
        self.inventory_items = page.get_by_test_id("inventory-item")

    def goto(self):
        self.page.goto("/inventory.html")

    def get_first_inventory_item(self):
        expect(self.inventory_items.first).to_be_visible()
        return InventoryItem(self.inventory_items.first)
