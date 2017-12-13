import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import WebDriver

from pbc.sel_grid import SshClient, HOST_NAME, USER, PASSWORD
from pbc.sel_grid.sel_grid import StartGrid, Grid


@pytest.fixture(scope="session")
def ssh_client():
    client = SshClient(HOST_NAME, USER, PASSWORD)
    grid = StartGrid(Grid(client))
    grid.download()
    grid.start_hub()
    grid.add_node()
    yield client
    client.execute("killall java")
    client.execute("rm -f *")
    client.terminate()


@pytest.fixture(scope="function")
def web_driver():
    # type: () -> WebDriver

    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Remote(
        command_executor='http://192.168.33.10:4444/wd/hub',
        desired_capabilities={'browserName': 'firefox'},
        options=options)
    yield driver
    driver.quit()
