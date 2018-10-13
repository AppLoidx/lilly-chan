from random import random

from GetQuestionOfJava import GetQuestionOfJava
from GetRecipe import GetRecipe
from Parser import Parser
import ServerClient


class Lilly:
    # Мобильная версия отличается тем, что команды выполниемые на компьютере посылает их через сокеты
    mobileVersion = True
    # Вопросы про Java OOP
    get_question_of_java = GetQuestionOfJava()
    # IP - адресс соединения  с компьютером
    sc = ServerClient.ServerClient('192.168.43.212', 9090)
    # Приветственное сообщение было отправлено во время сеанса
    WELCOME_MSG_SEND = False
    # Режим суперпользователя
    SUPER_USER = True
    # Рецептов просмотрено во время сеанса
    RECIPE_WATCHED = 0

    # Исполняемые команды. Команды в одном массиве однотипные
    COMMANDS = [["РАСПИСАНИЕ"],  # 0
                ["ТВОЙ СОЗДАТЕЛЬ", "КТО ТЫ?"],  # 1
                ["СПАСИБО", "THX", "THANKS", "THANK YOU", " СПАСИБКИ", "СПС"],  # 2
                ["ADMIN"],  # 3
                ["ЗАПУСТИ МУЗЫКУ", "MUSIC"],  # 4
                ["ОТКРОЙ ВК", "VK"],  # 5
                ["ПОГОДА"],  # 6
                ["HELIOS"],  # 7
                ["ПРИВЕТ", "ЗДАРОВА"],  # 8
                ["ЗАВТРАК", "ЧТО ПРИГОТОВИТЬ НА ЗАВТРАК", "ЕДА НА ЗАВТРАК"],  # 9
                ["HELP", "ПОМОЩЬ"],  # 10
                ["JAVA OOP", "ВОПРОС ПРО JAVA OOP", "ЗАДАЙ ВОПРОС ПРО JAVA"],  # 11
                ]

    # Различные вариации ответа на неопознанную команду
    IDONTKNOW_COMMANS = ["Не могу распознать",
                         "Прости, но я тебя не понимаю...",
                         "Что это за слово? Меня ему еще не учили...",
                         "Попробуй написать это по-другому, может тогда я смогу распознать его!",
                         "Не знаю... Прости..."]

    # Исполняемая команда, по умолчанию get_command
    # Может меняться в методе update_screen()
    NEXT_INPUT = "get_command"

    # Используется для ответа не неопознанные команды
    UNKNOWN_COMMANDS = 0

    def __init__(self):

        # Для парсинга сайтов
        self.parser = Parser()

    def get_welcome_msg(self, user_id: any) -> str:

        """ Возвращает приветственное сообщение с именем пользователя
        @:param user_id - id пользователя которому присылается сообщение
        @:return "Привет + $ИМЯ_ПОЛЬЗОВАТЕЛЯ" """

        if self.parser.LAST_USER_NAME is None:
            user_name = self.parser.get_user_name_from_vk_id(user_id)
        else:
            user_name = self.parser.LAST_USER_NAME
        self.WELCOME_MSG_SEND = True
        return "Привет, " + user_name.split()[0] + "!"

    def get_command(self, command):

        """
        Получает команду, затем обрабатывает её со списоком команд используя метод compare
        и выполняет соответветсвующую команду

        Если команда должна выполниться на компьютере, то через сокеты передает команду на сервер компьютера.
        Перед применением необходимо, чтобы компьютер и телефон были в одной вай-фай сети и получить значение
        IP-адреса через ipconfig.

        :param command: команда переданная польщователем
        :return: Возвращает текст, который следует вывести в сообщении
        """

        # Расписание
        if self.compare(command, self.COMMANDS[0]):
            n_day = self.parser.get_day_now()
            return "Сегодня : " + n_day + "\n" + self.parser.get_schedule_from_file("sh.txt", "Пятница", "нечет")

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

        # Отправление погоды сообщением
        elif self.compare(command, self.COMMANDS[6]):
            return self.parser.get_weather_today()

        # Запуск музыки на комп
        elif self.compare(command, self.COMMANDS[4]):
            print(self.sc.send(b"launchYoutubeMusic"))
            return "Запускаю музыку..."

        # Запуск ВК на комп
        elif self.compare(command, self.COMMANDS[5]):
            print(self.sc.send(b"launchVK"))
            return "Запускаю ВК на компьютер"

        # Открытие helios...
        elif self.compare(command, self.COMMANDS[7]):
            print(self.sc.send(b"launchHelios"))
            return "Запускаю Helios"

        # Повторное приветствие
        elif self.compare(command, self.COMMANDS[8]):
            return "Привет))"

        # Рецепт завтрака
        elif self.compare(command, self.COMMANDS[9]):
            self.RECIPE_WATCHED = 0
            return self.print_breakfast_recipe()

        # Вывести документацию
        elif self.compare(command, self.COMMANDS[10]):
            return self.DOCUMENTATION

        # Задать вопрос про Java ООП
        elif self.compare(command, self.COMMANDS[11]):
            return self.java_questions_mode()

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
                return self.IDONTKNOW_COMMANS[random.randint(0, len(self.IDONTKNOW_COMMANS))]

    def java_questions_mode(self, command="@#"):    # @# - если это первый вызов

        """ Переходит в режим вопросов по теме Java. Имеет свои команды взаимодействия."""

        # Следующий ввод перенаправляем в этот метод
        self.NEXT_INPUT = "java_questions_mode"

        if command == "@#":
            return ("Теперь я в режиме вопросов :)\n"
                    "Доступные команды:\n"
                    "вопрос - случайный вопрос\n"
                    "вопрос <номер> - вопрос по номеру\n"
                    "ответ - ответ на предыдущий вопрос, если я знаю))\n"
                    "закончить - выйти из режима вопросов((\n"
                    "очистить - очистить историю вопросов\n"
                    "хелп - вывести доступные команды\n")

        elif command.upper() == "ВОПРОС":
            return self.get_question_of_java.get_question()[1]

        elif command.upper().split(" ")[0] == "ВОПРОС" and len(command) > 7:
            try:
                return self.get_question_of_java.get_question(int(command.split(" ")[1]) - 2)[1]
            except IndexError:
                return "Простите, не нашла такого вопроса... Задайте другой параметр"
        elif self.compare(command.upper(), ["ОТВЕТ"]):
            return self.get_question_of_java.get_question(self.get_question_of_java.get_last_question())[2]

        elif self.compare(command.upper(), ["ОЧИСТИТЬ"]):
            self.get_question_of_java.reset_wasted_questions()
            return "История очистена!"

        elif self.compare(command.upper(), ["ХЕЛП"]):
            return ("Доступные команды:\n"
                    "вопрос - случайный вопрос\n"
                    "вопрос <номер> - вопрос по номеру\n"
                    "ответ - ответ на предыдущий вопрос, если я знаю))\n"
                    "закончить - выйти из режима вопросов((\n"
                    "очистить - очистить историю вопросов\n"
                    "хелп - вывести доступные команды\n")

        elif self.compare(command.upper(), ["ЗАКОНЧИТЬ"]):
            self.NEXT_INPUT = "get_command"
            return "Режим вопросов закончен"
        else:
            return "Не поняла вашего ответа, пожалуйста повторите"

    def print_breakfast_recipe(self, amount: int = 0) -> str:

        """
        Парсит рецепты с раздела завтрак с помощью класс GetRecipe из файла GetRecipe.py

        :param amount: количество рецептов, которое нужно вывести
        :return: рецепты
        """

        gr = GetRecipe()
        recipes = gr.get_breakfast()
        if amount == 0:

            self.NEXT_INPUT = "print_breakfast_recipe"
            return "Введите количество рецептов которое нужно вывести (Максимум: 6 )"
        else:
            try:
                amount = int(amount)
            except ValueError:
                self.NEXT_INPUT = "print_breakfast_recipe"
                return "Я не смогла распознать ваше число. Пожалуйста введите целое число."

            if amount < 1:
                return "Эмм... Не шутите со мной пожалуйста! Введите еще раз. Только сейчас по нормальному!"
            elif amount > 6:
                return "Ммм... я не смогу вывести столько рецептов, простите. Может какое-нибудь число поменьше?))"
            else:
                ret = ""
                temp = 0  # Counter
                for i in range(amount):
                    ret += "Название: " + recipes[self.RECIPE_WATCHED + amount - i][0] + \
                           "\n Ссылка: " + recipes[self.RECIPE_WATCHED + amount - i][1]
                    ret += "\n---------------\n"
                    temp += 1

                self.NEXT_INPUT = "breakfast_more_check"
                self.RECIPE_WATCHED += temp
                return "Вот что я нашла: \n" + ret

    def update_screen(self, input_value):

        """
        Метод для управления выполнением других методов. С помощью параметра NEXT_INPUT вызывает соответствующий
        метод. Это нужно, чтобы делать повторный ввод или вызвать определенную последовательность команд
        :param input_value: вводмое значение пользователся, которое передстся определенному методу.
        :return: возвращает метод, определенный в параметре NEXT_INPUT
        """

        print(self.NEXT_INPUT)

        if self.NEXT_INPUT == "java_questions_mode":
            return self.java_questions_mode(input_value)

        if self.NEXT_INPUT == "get_command":
            return self.get_command(input_value)

        if self.NEXT_INPUT == "admin_login":
            self.NEXT_INPUT = "admin_pwd"
            return self.admin_login(input_value)

        if self.NEXT_INPUT == "admin_pwd":
            self.NEXT_INPUT = "get_command"
            return self.admin_pwd(input_value)

        if self.NEXT_INPUT == "print_breakfast_recipe":
            return self.print_breakfast_recipe(input_value)

        if self.NEXT_INPUT == "breakfast_more_check":
            if self.compare(input_value.upper(), ["ЕЩЕ"]):
                return self.print_breakfast_recipe()
            else:
                self.NEXT_INPUT = "get_command"
                return self.get_command(input_value)

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

    DOCUMENTATION = """
    РАСПИСАНИЕ - еще в разработке
    ПОГОДА - показывает погоду
    ЗАВТРАК - показывает рецепты блюд на завтрак
        - после команды ЗАВТРАК можно ввести "еще", чтобы посмотреть еще несколько рецпетов
    ЗАДАЙ ВОПРОС ПРО JAVA - задает вопросы по теме языка программирования Java
    """
