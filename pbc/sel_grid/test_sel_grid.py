import pytest
from pbc.sel_grid.sel_grid import Grid,StartGrid


@pytest.mark.smoke
def test_grid_install_smoke(ssh_client):
    grid = StartGrid(Grid(ssh_client))
    grid.download()
    grid.start_hub()
    grid.add_node()
    assert len(ssh_client.execute('pgrep java')) == 2
    assert not ssh_client.execute('less log.txt | egrep -i "error|exception"')



