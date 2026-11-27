
from pages.login_page import LoginPage


def test_successful_login(page):
    login = LoginPage(page)

    login.login("tomsmith", "SuperSecretPassword!")

    login.verify_successful_login()


def test_login_with_invalid_username(page):
    login = LoginPage(page)

    login.login("wronguser", "SuperSecretPassword!")

    login.verify_error_message("Your username is invalid!")


def test_login_with_invalid_password(page):
    login = LoginPage(page)

    login.login("tomsmith", "wrongpassword")

    login.verify_error_message("Your password is invalid!")
