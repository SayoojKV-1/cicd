
from playwright.sync_api import Page, expect


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

        self.username = page.locator("#username")
        self.password = page.locator("#password")
        self.login_button = page.locator("button[type='submit']")
        self.flash_message = page.locator("#flash")

    def enter_username(self, username):
        self.username.fill(username)

    def enter_password(self, password):
        self.password.fill(password)

    def click_login(self):
        self.login_button.click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def verify_successful_login(self):
        expect(self.page).to_have_url(
            "https://the-internet.herokuapp.com/secure"
        )

    def verify_error_message(self, message):
        expect(self.flash_message).to_contain_text(message)
