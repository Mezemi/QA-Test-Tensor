from page.main_page import ContactsPage
from page.main_page import AboutPage
from page.main_page import MainPage

import pytest
link = "https://sbis.ru/"

@pytest.mark.photos_chronologies
def test_photos_chronologies_identical_height_width(browser):
    browser.implicitly_wait(10)

    page = ContactsPage(browser, link)
    page.open()
    page.go_to_header_contacts()
    page.go_to_contacts_banner()
    page.switch_to_browser(1)

    page = MainPage(browser, link)
    page.check_of_banner_strength_people()
    page.go_to_banner_more_details()

    page = AboutPage(browser, link)
    page.check_of_link()
    page.check_of_size_photosc_hronology()

@pytest.mark.region
def test_region(browser):
    browser.implicitly_wait(10)

    page = ContactsPage(browser, link)
    page.open()
    page.go_to_header_contacts()
    page.check_region()
    page.check_contacts_clients()
    page.go_to_region()
    page.go_to_region_кamchatka_krai()
    page.check_switch_to_кamchatka_krai()

