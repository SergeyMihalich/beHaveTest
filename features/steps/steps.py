from behave import step



@step ('Открыли сайт Гугл "{site}"')
def open(context, site):
    context.driver.get(site)
