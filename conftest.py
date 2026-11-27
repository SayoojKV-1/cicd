
import pytest
from playwright.sync_api import Page


@pytest.fixture(autouse=True)
def open_login_page(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
