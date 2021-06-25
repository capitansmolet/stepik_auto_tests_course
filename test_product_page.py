import pytest
from pages.product_page import ProductPage

PRODUCT_LINK = ("http://selenium1py.pythonanywhere.com/"
                "catalogue/the-shellcoders-handbook_209/?promo=newYear")

PRODUCT_BASE_LINK = ("http://selenium1py.pythonanywhere.com/"
                     "catalogue/coders-at-work_207")

urls = ([pytest.param(f"{PRODUCT_BASE_LINK}/?promo=offer{number}",
        marks=pytest.mark.xfail(number == 7, reason="bug"))
        for number in range(10)])


@pytest.mark.parametrize("link", urls)
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
