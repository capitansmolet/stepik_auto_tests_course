from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


with webdriver.Chrome() as browser:
    link = "http://suninjuly.github.io/math.html"
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    option1 = browser.find_element_by_css_selector("[id='robotCheckbox']")
    option1.click()

    option2 = browser.find_element_by_css_selector("[id='robotsRule']")
    option2.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(30)
