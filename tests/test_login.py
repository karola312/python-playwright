import pytest
from playwright.sync_api import Page, expect

from enums.User import User
from pages.login_page import LoginPage
from pages.components.header import Header

class TestLogin:

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.login_page = LoginPage(page)

    def test_correct_login(self, page: Page):
        # self.login_page.login(User.STANDARD_USER, "secret_sauce")
        # expect(Header(page).cart_button).to_be_enabled()
        pass
