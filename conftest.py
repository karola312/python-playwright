import pytest
from playwright.sync_api import Page, Playwright
from typing import Dict
from _pytest.fixtures import SubRequest

@pytest.fixture(scope="function", autouse=True)
def goto(page: Page, base_url: str, request: SubRequest):
    if hasattr(request, "param"):
        page.context.add_cookies(
            [{"name": "session-username", "value": request.param, "url": base_url}]
        )
        page.goto("/inventory.html")
    else:
        page.goto("")


@pytest.fixture(scope="session", autouse=True)
def browser_type_launch_args(browser_type_launch_args: Dict, playwright: Playwright):
    playwright.selectors.set_test_id_attribute("data-test")
    return {**browser_type_launch_args, "args": ["--start-maximized"]}
