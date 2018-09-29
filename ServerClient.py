import socket


class ServerClient:

    def __init__(self, server_address, server_port):
        self.serverAddress = server_address
        self.serverPort = server_port

    def send(self, data):
        sock = socket.socket()
        sock.connect((self.serverAddress, self.serverPort))
        sock.send(data)

        returned_data = sock.recv(1024)
        sock.close()

        return returned_data
