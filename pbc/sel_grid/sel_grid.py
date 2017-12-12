from abc import ABCMeta, abstractmethod
from time import sleep

from pbc.sel_grid import GRID_JAR, GRID_LINK


class BaseGrid:
    __metaclass__ = ABCMeta

    @abstractmethod
    def download(self):
        pass

    @abstractmethod
    def start_hub(self):
        pass

    @abstractmethod
    def add_node(self):
        pass


class Grid(BaseGrid):
    def __init__(self, ssh_client):
        self._client = ssh_client

    def download(self):
        print 'Download Selenium Grid'
        self._client.execute('wget -O {file} {link}'.format(file=GRID_JAR, link=GRID_LINK))
        sleep(5)

    def start_hub(self):
        print 'Starting the hub'
        self._client.execute('java -jar {} -role hub >> log.txt 2>&1 &'.format(GRID_JAR))
        sleep(5)

    def add_node(self):
        print 'Adding the node'
        self._client.execute(
            'java -jar {} -role node  -hub http://localhost:4444/grid/register >> log.txt 2>&1 &'.format(GRID_JAR))
        sleep(5)

    def is_downloaded(self):
        if self._client.execute('find -name {}'.format(GRID_JAR)):
            print 'File has been downloaded already'
            return True
        else:
            return False


class StartGrid(BaseGrid):
    def __init__(self, grid):
        self._g = grid
        self._is_downloaded = grid.is_downloaded()

    def start_hub(self):
        self._g.start_hub()

    def download(self):
        if not self._is_downloaded:
            self._g.download()
        else:
            print ('Skip downloading')

    def add_node(self):
        self._g.add_node()
