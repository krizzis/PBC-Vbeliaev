import pytest
from pbc.sel_grid.webdriver import WebDriver
from pbc.sel_grid import HOST_NAME, USER, PASSWORD
from pbc.sel_grid import SshClient


@pytest.fixture(scope="session")
def ssh_client():
    client = SshClient(HOST_NAME, USER, PASSWORD)
    yield client
    client.terminate()


@pytest.fixture(scope='function', autouse=True)
def tear_down(ssh_client, request):
    def fin():
        print ('cleaning my closet')
        ssh_client.execute("killall java")
        ssh_client.execute("rm -f *")
    request.addfinalizer(fin)


@pytest.fixture()
def firefox_driver():
    driver = WebDriver()
    yield driver
    driver.close_browser()
