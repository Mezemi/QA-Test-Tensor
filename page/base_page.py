from selenium.webdriver.common.by import By


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    # def get_element_selector(self, time, param):
    #     ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
    #     return WebDriverWait(self.browser, time, ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located((By.CSS_SELECTOR, param)))

    def switch_to_browser(self, Namber):
        self.browser.switch_to.window(self.browser.window_handles[Namber])

    def get_element_selector(self, SELECTOR):
        return self.browser.find_element(By.CSS_SELECTOR, SELECTOR)
