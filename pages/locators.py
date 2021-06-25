from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_MESSAGE = (By.CSS_SELECTOR,
                       "#messages > div > div strong")
    PRODUCT_COST = (By.CSS_SELECTOR, ".product_main p.price_color")
    COST_MESSAGE = (By.CSS_SELECTOR,
                    "#messages > div:nth-child(3) > div > p > strong")
