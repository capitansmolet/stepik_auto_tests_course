import time
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_button_add_to_shopping(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_elements(By.CLASS_NAME, 'btn-add-to-basket')
    assert len(button) > 0, 'Button not found!'
