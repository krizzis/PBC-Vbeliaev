import pytest
import requests

from pbc.sel_grid import HOST_NAME
from pbc.sel_grid.sel_grid import Grid, StartGrid
from pbc.sel_grid.page import GridPage


@pytest.mark.smoke
@pytest.mark.selenium
def test_grid_install_smoke(ssh_client):
    grid = StartGrid(Grid(ssh_client))
    grid.download()
    grid.start_hub()
    grid.add_node()
    assert len(ssh_client.execute('pgrep java')) == 2
    assert not ssh_client.execute('less log.txt | egrep -i "error|exception"')


@pytest.mark.selenium
def test_grid_numbers_of_session(ssh_client, firefox_driver):
    grid = StartGrid(Grid(ssh_client))
    grid.download()
    grid.start_hub()
    grid.add_node()
    page = GridPage(firefox_driver)
    assert page.max_sessions() == 5


@pytest.mark.http
def test_grid_session_count_http(ssh_client):
    grid = StartGrid(Grid(ssh_client))
    grid.download()
    grid.start_hub()
    grid.add_node()
    response = requests.get('http://{}:4444/grid/console'.format(HOST_NAME))
    assert response.content.count('browserName=firefox') == 5
