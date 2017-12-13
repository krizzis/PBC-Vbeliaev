from selenium import webdriver


class WebDriver:

    def __init__(self):
        self._driver = webdriver.Firefox()

    def load_page(self, url):
        self._driver.get(url)

    def close_browser(self):
        self._driver.quit()

    def find_element_by_selector(self, selector):
        return self._driver.find_elements_by_css_selector(selector)
