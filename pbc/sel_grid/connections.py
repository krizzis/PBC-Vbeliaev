import paramiko


class SshClient:
    def __init__(self, host_name, usr, psw):
        self._usr = usr
        self._psw = psw
        self.host_name = host_name

        self.client = self._client_connect()

    def _client_connect(self):
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
            client.connect(self.host_name, username=self._usr, password=self._psw, timeout=20)
        finally:
            print 'Successfully connected to {host} as {usr}'.format(host=self.host_name, usr=self._usr)
            return client

    def execute(self, command):
        stdin, stdout, stderr = self.client.exec_command(command)
        return stdout.read().splitlines()

    def terminate(self):
        self.client.close()

