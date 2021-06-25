from pages.login_page import LoginPage

LOGIN_LINK = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"


def test_should_be_login_page(browser):
    login_page = LoginPage(browser, LOGIN_LINK)
    login_page.open()
    login_page.should_be_login_page()

# команда для запуска теста
# pytest -v --tb=line --language=en test_login_page.py
