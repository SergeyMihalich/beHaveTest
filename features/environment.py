from selenium import webdriver
from locators import google_loc


def before_teg(context, tag): ...


def before_all(context):
    context.driver = webdriver.Chrome()
    context.locators = google_loc

def before_feature(context, feature): ...


def before_scenario(context, scenario): ...


def before_step(context, step): ...


def after_all(context): ...


def after_feature(context, feature): ...


def after_scenario(context, scenario): ...


def after_step(context, step): ...
