import pytest
from .pages.login_page import LoginPage
from .pages.main_page import MainPage


@pytest.fixture(scope="function", autouse=True)
def login_page(browser):
    return LoginPage(browser)


@pytest.fixture(scope="function", autouse=True)
def main_page(browser):
    return MainPage(browser)

@pytest.mark.need_review
def test_without_agree(login_page, main_page):
    login_page.load()
    login_page.set_username("forndldoka7+admin@gmail.com")
    login_page.set_password("1234567Zx!")
    login_page.submit()
    assert login_page.is_error_displayed()


@pytest.mark.need_review
def test_with_agree(login_page, main_page):
    login_page.load()
    login_page.set_username("forndldoka7+admin@gmail.com")
    login_page.set_password("1234567Zx!")
    login_page.agree_to_terms()
    login_page.submit()
    assert main_page.is_title_displayed()
