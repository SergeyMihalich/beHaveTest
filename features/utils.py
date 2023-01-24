from features.locators import google_loc

locator = {
    **google_loc
}


def get_loc(loc_name):
    select = locator.get(loc_name)
    if not select:
        raise Warning(f'+++ Поле {loc_name} не найдено +++')
    return select
