from selenium.webdriver.common.by import By


class HomePageLocators(object):
    LOGO = (By.ID, 'gh-logo')
    SEARCH_BAR = (By.ID, 'gh-ac')
    SEARCH_BUTTON = (By.ID, 'gh-btn')


class SearchPageLocators(object):
    PRICE_NAV = (By.ID, 'srp-river-main')
    select_size_10 = (By.CSS_SELECTOR, "input[aria-label='10']")
    search_brand = (By.CSS_SELECTOR, ".x-searchable-list__textbox__aspect-Brand")
    select_puma = (By.CSS_SELECTOR, "input[aria-label='PUMA']")
    results_number = (By.CSS_SELECTOR, ".srp-controls__count-heading")
    sort_button = (By.CSS_SELECTOR, "button[aria-controls='w7']")
    check_lowest_first = (By.CSS_SELECTOR, "ul[class='srp-sort__menu'] > li:nth-child(4)")
    items_name = (By.CSS_SELECTOR, ".s-item__title")
    items_price = (By.CSS_SELECTOR, ".s-item__price")
