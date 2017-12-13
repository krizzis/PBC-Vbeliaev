class GridPage:

    def __init__(self, firefox_driver):
        self._driver = firefox_driver

    def max_sessions(self):
        return len(self._driver.find_element_by_selector('img[src$="firefox.png"]'))
