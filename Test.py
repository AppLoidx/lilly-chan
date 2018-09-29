import os

import ServerClient

sc = ServerClient.ServerClient('localhost', 9090)
print(sc.send(b'hello'))
