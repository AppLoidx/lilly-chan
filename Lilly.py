from Parser import Parser
import os
import ServerClient

class Lilly:

    sc = ServerClient.ServerClient('192.168.43.212', 9090)
    WELCOME_MSG_SEND = False
    SUPER_USER = True

    COMMANDS = [["РАСПИСАНИЕ"],
                ["ТВОЙ СОЗДАТЕЛЬ", "КТО ТЫ?"],
                ["СПАСИБО", "THX", "THANKS", "THANK YOU", " СПАСИБКИ", "СПС"],
                ["ADMIN"],
                ["ЗАПУСТИ МУЗЫКУ", "MUSIC"],
                ["ОТКРОЙ ВК", "VK"],
                ["ПОГОДА"],
                ["HELIOS"]
                ]

    NEXT_INPUT = "get_command"

    UNKNOWN_COMMANDS = 0

    def __init__(self):
        self.parser = Parser()

    def get_welcome_msg(self, user_id):
        if self.parser.LAST_USER_NAME is None:
            user_name = self.parser.get_user_name_from_vk_id(user_id)
        else:
            user_name = self.parser.LAST_USER_NAME
        self.WELCOME_MSG_SEND = True
        return "Привет, " + user_name.split()[0] + "!"

    def get_command(self, command):

            # Расписание
            if self.compare(command, self.COMMANDS[0]):
                n_day = self.parser.get_day_now()
                return self.parser.get_schedule_from_file("sh.txt", "Пятница", "нечет")

            # About assistant
            elif self.compare(command, self.COMMANDS[1]):
                return "Меня создал Артур. Сейчас я не сильно умею различать получаемые сообщения, но он пообещал " \
                       "мне в будущем расширить мои функции. Как-то он мне говорил, что я написана на питоне." \
                       "Не знаю, что это значит...но так сказал мой создатель."

            # Ответ на благодарность
            elif self.compare(command, self.COMMANDS[2]):
                return "Рада помочь!"

            # Авторизация супер пользователя
            elif self.compare(command, self.COMMANDS[3]):
                self.NEXT_INPUT = "admin_login"
                return "Введите логин и пароль отдельными сообщениями"

            # Запуск музыки на комп
            elif self.compare(command, self.COMMANDS[4]):
                os.system("start https://www.youtube.com/watch?v=sU9tUAOyExE&list=LL2HkMitR__lenKqpzpjE14g&index=4&t=0s")
                return "Запускаю музыку..."

            # Запуск ВК на комп
            elif self.compare(command, self.COMMANDS[5]):
                print(self.sc.send(b"launchVK"))
                return "Запускаю ВК на компьютер"

            # Отправление погоды сообщением
            elif self.compare(command, self.COMMANDS[6]):
                return self.parser.get_weather_today()

            # Открытие helios...
            elif self.compare(command, self.COMMANDS[7]):
                print(self.sc.send(b"launchHelios"))
                return "Запускаю Helios"
            # Команда не распознана
            else:
                self.UNKNOWN_COMMANDS += 1

                if self.UNKNOWN_COMMANDS == 1:
                    return "Извините, но такой команды я пока не знаю." \
                           "Пожалуйста, напишите моему создателю, чтобы он его добавил..."
                elif self.UNKNOWN_COMMANDS == 2:
                    return "Такой команды я тоже не знаю... Простите..."
                elif self.UNKNOWN_COMMANDS == 3:
                    return "Может вы как-то неправильно пишете команду?"
                elif self.UNKNOWN_COMMANDS == 4:
                    return "Не могу распознать команду!"
                else:
                    return "Я не знаю такой команды."


    def update_screen(self, input_value):

        if self.NEXT_INPUT == "get_command":
            self.get_command(input_value)

        if self.NEXT_INPUT == "admin_login":
            self.admin_login(input_value)
            self.NEXT_INPUT = "admin_pwd"

        if self.NEXT_INPUT == "admin_pwd":
            self.admin_pwd(input_value)
            self.NEXT_INPUT = "get_command"

    def admin_login(self, login):
        self.NEXT_INPUT = "admin_pwd"

    def admin_pwd(self, pwd):
        if pwd == "123":
            self.SUPER_USER = True

    @staticmethod
    def compare(name: str, array: list, upper: bool = True) -> object:
        """
        Сравнивает значение переданного слова со значениями массива. Так же учитваются возможные опечатки,
        но только позиционно. То есть каждая позиция проверяется с соответвующей.

        :param name: проверяемое слово
        :param array: массив, где хранятся возможные значения слова
        :param upper: если истина, то не обращает внимания на регистр, иначе различает
        :return: если хотя бы одно значение с массива совпадает со словом, возращает True, иначе False
        """
        if upper:
            name = name.upper()

        for i in array:
            k = 0  # считывание разницы в символах (посимвольно, позиционно)
            if len(i) > len(name):
                for j in range(len(name)):
                    if name[j] == i[j]:
                        pass
                    else:
                        k = k + 1
            else:
                for j in range(len(i)):
                    if i[j] == name[j]:
                        pass
                    else:
                        k = k + 1

            k = k + abs(len(i) - len(name))  # добавление разницы в недостающих символах

            # Обработка возможной опечатки
            if 7 > len(name) > 4 and k < 3:
                return True
            elif 7 <= len(name) < 12 and k < 5:
                return True
            elif len(name) > 11 and k < 7:
                return True
            elif len(name) <= 4 and k < 1:
                return True

        return False
