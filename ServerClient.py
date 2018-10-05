import socket


class ServerClient:
    """
    Для передачи данных на компьютер с помощью сокетов
    """
    def __init__(self, server_address, server_port):
        self.serverAddress = server_address     # ip-адресс
        self.serverPort = server_port           # порт

    def send(self, data):
        """
        Обмен данными с удаленным устройством
        :param data: отправляемая информация
        :return: ответ на отправленную информацию
        """
        sock = socket.socket()
        sock.connect((self.serverAddress, self.serverPort))
        sock.send(data)                     # отправление информации

        returned_data = sock.recv(1024)     # получение информации
        sock.close()

        return returned_data
