from pages.login_page import LoginPage

LOGIN_LINK = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"


def test_is_this_the_login_url(browser):
    login_page = LoginPage(browser, LOGIN_LINK)
    login_page.open()
    login_page.should_be_login_url()


def test_is_there_a_login_form(browser):
    login_page = LoginPage(browser, LOGIN_LINK)
    login_page.open()
    login_page.should_be_login_form()


def test_is_there_a_registration_form(browser):
    login_page = LoginPage(browser, LOGIN_LINK)
    login_page.open()
    login_page.should_be_register_form()

# команда для запуска теста
# pytest -v --tb=line --language=en test_login_page.py
