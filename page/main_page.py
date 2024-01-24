from page.base_page import BasePage
from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchElementException

import time

class ContactsPage(BasePage):
    def go_to_header_contacts(self):
        login_link = self.get_element_selector(".sbisru-Header__menu > li.sbisru-Header__menu-item-1 > a")
        login_link.click()

    def go_to_contacts_banner(self):
        logo_link = self.get_element_selector("#contacts_clients .sbisru-Contacts__logo-tensor > img")
        logo_link.click()

    def check_region(self):
        region = self.get_element_selector(".sbisru-Contacts__relative .sbis_ru-Region-Chooser__text").text
        assert region != None or region != "", "Поле регисон пустое либо неопределено"

    def go_to_region(self):
        region_link = self.get_element_selector(".sbisru-Contacts__relative .sbis_ru-Region-Chooser__text")
        region_link.click()

    def go_to_region_кamchatka_krai(self):
        region_кamchatka_krai = self.get_element_selector(".sbis_ru-Region-Panel__list [title='Камчатский край']")
        region_кamchatka_krai.click()

    def check_contacts_clients(self):
        SELECTOR = "[id='contacts_clients']  [data-qa='items-container']"
        try:
            self.get_element_selector(SELECTOR)
        except NoSuchElementException as e:
            print(f"Произошла ошибка: {e}.")

    #По ТЗ нужна Камчатка, имеет смысл переделать под pytest.mark.parametrize если потребуется больше городов
    def check_switch_to_кamchatka_krai(self):
        try:
            self.get_element_selector("[title='СБИС - Камчатка']")
        except NoSuchElementException as e:
            print(f"Произошла ошибка: {e}.")

        assert self.browser.current_url.find("kamchatskij-kraj"), "Адрес не камчатский край"


class AboutPage(BasePage):
    def check_of_link(self):
        assert self.browser.current_url == "https://tensor.ru/about", "Адрес страницы отличен от 'https://tensor.ru/about'"

    def check_of_size_photosc_hronology(self):
        size_photosc = self.browser.find_elements(By.CSS_SELECTOR,".tensor_ru-About__block3-image-wrapper")
        for x in size_photosc:
            assert x.size['height'] == size_photosc[0].size['height'] or x.size['width'] == size_photosc[0].size['width'], "Не все элементы страницы одного размера"


class MainPage(BasePage):

    def check_of_link(self):
        assert self.browser.current_url == "https://tensor.ru", "Адрес страницы отличен от 'https://tensor.ru'"

    def go_to_banner_more_details(self):
        time.sleep(1)
        moredetails_link = self.get_element_selector(".s-Grid-col--6 a.tensor_ru-link ")
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", moredetails_link)
        moredetails_link.click()

    def check_of_banner_strength_people(self):
        try:
            self.get_element_selector(".s-Grid-col.s-Grid-col--6 .tensor_ru-Index__card-title")
        except NoSuchElementException as e:
            print(f"Произошла ошибка: {e}.")

class DownloadPage(BasePage):
    def go_to_plugin_link(self):
        plugin_link = self.get_element_selector("[data - id ='plugin'] .controls-tabButton__overlay")
        plugin_link.click()

    def go_to_download_link(self):
        download_link = self.get_element_selector("[data-for='plugin'] .ws-SwitchableArea__item .sbis_ru-DownloadNew-loadLink__link")
        download_link.click()





