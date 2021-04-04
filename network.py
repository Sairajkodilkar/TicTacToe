import socket
import sys

class MsgHandle:

    def _recvmsg(self, socket, size = 1024):

        while(1):
            try:
                encodedmsg = socket.recv(size)
            except system.TimeoutException:
                continue
            return encodedmsg.decode()

    def _sendmsg(self, socket, msg):
        encodedmsg = msg.encode('utf-8')
        socket.send(encodedmsg)

class Server(MsgHandle):

    def __init__(self, port = 8080):
        self.port = port
        self.s = socket.socket()

    def connect(self, num = 1):
        self.s.bind(('', self.port))
        self.s.listen(num)
        self.c, self.addr = self.s.accept()
        return self.addr

    def recvmsg(self, size = 1024):
        return self._recvmsg(self.c, size)

    def sendmsg(self, msg):
        self._sendmsg(self.c, msg)

    def close(self):
        self.s.close()


class Client(MsgHandle):

    def __init__(self, port, hostname):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = port
        self.hostname = hostname

    def connect(self):
        try:
            host_ip = socket.gethostbyname(self.hostname)
        except socket.gaierror:
            print("Cant resolve hostname")
            s.close
            sys.exit(1)

        self.s.connect((host_ip, self.port))

    def recvmsg(self, size = 1024):
        return self._recvmsg(self.s, size)

    def sendmsg(self, msg):
        self._sendmsg(self.s, msg)

    def close(self):
        self.s.close()

        





