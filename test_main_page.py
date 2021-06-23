from pages.main_page import MainPage
MAIN_LINK = "http://selenium1py.pythonanywhere.com/"


def go_to_login_page(browser):
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()


def test_guest_can_go_to_login_page(browser):
    # инициализируем Page Object,
    # передаем в конструктор экземпляр драйвера и url адрес
    page = MainPage(browser, MAIN_LINK)
    # открываем страницу
    page.open()
    # выполняем метод страницы — переходим на страницу логина
    page.go_to_login_page()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, MAIN_LINK)
    page.open()
    page.should_be_login_link()

# команда для запуска теста
# pytest -v --tb=line --language=en test_main_page.py
