import operator
import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from behave import step
from selenium.webdriver.support.wait import WebDriverWait

from features import utils


@step('Открыли сайт Гугл "{site}"')
def open(context, site):
    context.driver.get(site)


@step('Ввели "{val}" в поле "{inp}"')
def enter_value_in_search(context, val, inp):
    select = utils.get_loc(inp)
    element = WebDriverWait(context.driver, 10).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, select)))
    element.send_keys(val)
    element.send_keys(Keys.ENTER)


@step('Проверил что ссылок "{amount}"')
def check_links(context, amount):
    sing, value = amount.split()
    value = int(value)
    sing_map = {
        '>': operator.gt,
        '<': operator.lt,
        '=': operator.eq,
    }
    func = sing_map[sing]
    select = utils.get_loc('элементы поиска')
    elements = WebDriverWait(context.driver, 10).until(
        ec.presence_of_all_elements_located((By.CSS_SELECTOR, select)))

    print(func(len(elements), value), len(elements), value)
    print('\33[1m\33[40m')
    assert func(len(elements), value), f'количество записей не соответствует ожиданию \033[0m'