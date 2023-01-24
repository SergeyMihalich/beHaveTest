import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


url = 'http://google.ru'
driver = webdriver.Chrome()


def get_search_field():
    element = driver.find_element_by_css_selector('.gLFyf')
    element.send_keys('что такое хорошо и что такое плохо')
    element.send_keys(Keys.ENTER)

    assert element


def get_text(element):
    text = element.get_property("textContent")
    return text


def get_elements():
    elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.TzHB6b.cLjAic.K7khPe')))

    txt = list(map(lambda element: get_text(element), elements))

    print(txt)
    return txt


def main():
    driver.get(url)
    get_search_field()
    get_elements()

    time.sleep(10)
    driver.quit()


if __name__ == '__main__':
    main()
