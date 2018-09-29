import os

import ServerClient

sc = ServerClient.ServerClient('192.168.43.212', 9090)
print(sc.send(b'hello'))
