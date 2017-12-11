import pytest
from pbc.sel_grid import HOST_NAME, USER, PASSWORD
from pbc.sel_grid import SshClient


@pytest.fixture(scope="session")
def ssh_client():
    client = SshClient(HOST_NAME, USER, PASSWORD)
    yield client
    client.execute("killall java")
    client.terminate()
