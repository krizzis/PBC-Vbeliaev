from abc import ABCMeta, abstractmethod
from time import sleep

from pbc.sel_grid import GRID_NAME, GRID_LINK, NODE_NAME, NODE_LINK


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

    def download(self, filename, link):
        self._client.execute('wget -O {file} {link}'.format(file=filename, link=link))
        sleep(5)

    def start_hub(self):
        print 'Starting the hub'
        self._client.execute('rm log.txt')
        self._client.execute('java -jar {} -role hub >> log.txt 2>&1 &'.format(GRID_NAME))
        sleep(5)

    def add_node(self):
        print 'Adding the node'
        self._client.execute(
            'java -jar {} -role node -nodeConfig sg-node.json >> log.txt 2>&1 &'.format(GRID_NAME))
        sleep(5)

    def is_downloaded(self, target_file):
        if self._client.execute('find -name {}'.format(target_file)):
            print '{} has been downloaded already'.format(target_file)
            return True
        else:
            return False


class StartGrid(BaseGrid):
    def __init__(self, grid):
        self._g = grid

    def start_hub(self):
        self._g.start_hub()

    def download(self):
        if not self._g.is_downloaded(GRID_NAME):
            print("Download Selenium Grid")
            self._g.download(GRID_NAME, GRID_LINK)
        if not self._g.is_downloaded(NODE_NAME):
            print("Download node.json file")
            self._g.download(NODE_NAME, NODE_LINK)
        else:
            print ('Skip downloading')

    def add_node(self):
        self._g.add_node()
