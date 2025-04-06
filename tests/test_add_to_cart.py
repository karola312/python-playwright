import pytest
from playwright.sync_api import Page, expect
from enums.User import User
from pages.products_list_page import ProductsListPage

class TestAddToCart:  

    @pytest.mark.parametrize(
        "goto", [User.STANDARD_USER], indirect=True
    )
    def test_add_single_item_to_cart(self, page:Page):
        self.products_list_page = ProductsListPage(page)
        first_inventory_item = self.products_list_page.get_first_inventory_item()
        first_inventory_item.add_item_to_cart()
        cart_inventory_quantity = (
            self.products_list_page.header.cart_items_quantity_span
        )
        expect(cart_inventory_quantity).to_have_text("1")
        expect(first_inventory_item.get_remove_button()).to_be_enabled()
