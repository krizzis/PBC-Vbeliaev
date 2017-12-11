import pytest
import paramiko
import time


@pytest.fixture(scope="session")
def selenium_grid_start():

    ip = '192.168.33.10'
    usr = 'vagrant'
    psw = 'vagrant'
    selenium = 'selenium-server-standalone-3.8.0.jar'

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect(ip, username=usr, password=psw)

    stdin, stdout, stderr = client.exec_command('find -name {}'.format(selenium))
    filein = stdout.readlines()

    if not filein:
        client.exec_command('wget -O {} https://goo.gl/SVuU9X'.format(selenium))
        time.sleep(3)
    client.exec_command('java -jar {} -role hub >> log.txt 2>&1 &'.format(selenium))
    time.sleep(3)
    client.exec_command('java -jar {} -role node  -hub http://localhost:4444/grid/register >> log.txt 2>&1 &'
                        .format(selenium))
    time.sleep(3)

    stdin, stdout, stderr = client.exec_command('pgrep java')
    java_processes = stdout.readlines()

    yield list(java_processes)

    client.exec_command('killall java')  # kill processes
    client.close()
