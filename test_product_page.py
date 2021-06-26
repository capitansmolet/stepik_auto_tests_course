import pytest

from pages.login_page import LoginPage
from pages.product_page import ProductPage

PRODUCT_LINK = ("http://selenium1py.pythonanywhere.com/"
                "catalogue/the-shellcoders-handbook_209/?promo=newYear")

PRODUCT_BASE_LINK = ("http://selenium1py.pythonanywhere.com/"
                     "catalogue/coders-at-work_207")

FROM_PRODUCT_TO_LOGIN_LINK = ("http://selenium1py.pythonanywhere.com/"
                              "en-gb/catalogue/the-city-and-the-stars_95/")

urls = ([pytest.param(f"{PRODUCT_BASE_LINK}/?promo=offer{number}",
        marks=pytest.mark.xfail(number == 7, reason="bug"))
        for number in range(10)])


@pytest.mark.parametrize("link", urls)
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()


@pytest.mark.xfail(reason="Negative check")
def test_guest_cant_see_success_message_after_adding_product_to_basket(
        browser):
    product_page = ProductPage(browser, PRODUCT_LINK)
    product_page.open()
    product_page.add_product()
    product_page.solve_quiz_and_get_code()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, PRODUCT_LINK)
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.xfail(reason="Negative check")
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, PRODUCT_LINK)
    product_page.open()
    product_page.add_product()
    product_page.solve_quiz_and_get_code()
    product_page.message_should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, FROM_PRODUCT_TO_LOGIN_LINK)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, FROM_PRODUCT_TO_LOGIN_LINK)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
