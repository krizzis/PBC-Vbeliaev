from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pbc.sel_page import MAIN_PAGE


class MainPage:

    def __init__(self, driver):
        # type: (WebDriver) -> None
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 10)

    def open_page(self):
        self._driver.get(MAIN_PAGE)
        return self

    def print_screen(self, name):
        self._driver.save_screenshot(name)
        return self

    def search_text(self, value):
        _search_bar = self._wait.until(
            expected_conditions.presence_of_element_located((By.NAME, "q")))

        _search_bar.clear()
        _search_bar.send_keys(value)
        _search_bar.send_keys(Keys.RETURN)

        self._wait.until(
            expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, "list-recent-events"))
        )

        return self

    def get_title(self):
        return self._driver.title

    def search_result(self):
        res = []
        sr = self._driver.find_elements_by_css_selector(".list-recent-events p")
        for r in sr:
            res.append(r.text)
        return res
