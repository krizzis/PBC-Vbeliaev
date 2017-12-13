from pbc.sel_grid import HOST_NAME


class GridPage:

    def __init__(self, firefox_driver):
        self._driver = firefox_driver
        firefox_driver.load_page('http://{}:4444/grid/console'.format(HOST_NAME))

    def max_sessions(self):
        return len(self._driver.find_element_by_selector('img[src$="firefox.png"]'))
