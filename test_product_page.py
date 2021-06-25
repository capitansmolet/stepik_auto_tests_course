from pages.product_page import ProductPage

PRODUCT_LINK = ("http://selenium1py.pythonanywhere.com/"
                "catalogue/the-shellcoders-handbook_209/?promo=newYear")


def test_guest_can_add_product_to_basket(browser):
    product_page = ProductPage(browser, PRODUCT_LINK)
    product_page.open()
    product_page.add_product_to_basket()
