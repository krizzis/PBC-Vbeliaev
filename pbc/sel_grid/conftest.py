import pytest
from pbc.sel_grid.webdriver import WebDriver
from pbc.sel_grid import HOST_NAME, USER, PASSWORD
from pbc.sel_grid import SshClient


@pytest.fixture(scope="session")
def ssh_client():
    client = SshClient(HOST_NAME, USER, PASSWORD)
    yield client
    client.execute("killall java")
    client.terminate()


@pytest.fixture()
def firefox_driver():
    driver = WebDriver()
    driver.load_page('http://{}:4444/grid/console'.format(HOST_NAME))
    yield driver
    driver.close_browser()
