import pytest
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
def test_grid_numbers_of_session(firefox_driver):
    page = GridPage(firefox_driver)
    assert page.max_sessions() == 5
