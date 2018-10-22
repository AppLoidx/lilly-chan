import comparer.comparer


class CommandManager:
    def __init__(self):
        self.COMMANDS = [["РАСПИСАНИЕ", "РАСПИСАНИЕ ЗАВТРА"],  # 0
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
                         ["СОЗДАЙ ОЧЕРЕДЬ"],  # 12
                         ["ОЧЕРЕДЬ","РЕДАКТИРОВАТЬ ОЧЕРЕДЬ"]    # 13
                         ]
        self.compare = comparer.Compare.compare

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
        if self.compare(command.split(" ")[0], self.COMMANDS[0]):
            command = command.split(" ")
            if len(command) > 1:
                if self.compare(command[1], ["ЗАВТРА"]):
                    return self.get_schedule("tomorrow")
            return self.get_schedule()

        # TODO: convert ask to file text
        # About assistant
        elif self.compare(command, self.COMMANDS[1]):
            return "Меня создал Артур. Сейчас я не сильно умею различать получаемые сообщения, но он пообещал " \
                   "мне в будущем расширить мои функции. Как-то он мне говорил, что я написана на питоне." \
                   "Не знаю, что это значит...но так сказал мой создатель."

        # Ответ на благодарность
        elif self.compare(command, self.COMMANDS[2]):
            return "Рада помочь!"

        # TODO: realize it
        # Авторизация супер пользователя
        elif self.compare(command, self.COMMANDS[3]):
            self.NEXT_INPUT = "admin_login"
            return "Введите логин и пароль отдельными сообщениями"

        # Отправление погоды сообщением
        elif self.compare(command, self.COMMANDS[6]):
            return self.parser.get_weather_today()

        # TODO: reformat couples with computer
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
            return self.get_breakfast_recipe()

        # TODO: reformat to input from file
        # Вывести документацию
        elif self.compare(command, self.COMMANDS[10]):
            return self.DOCUMENTATION

        # Задать вопрос про Java ООП
        elif self.compare(command, self.COMMANDS[11]):
            return self.java_questions_mode()

        elif self.compare(command, self.COMMANDS[12]):
            self.queue.new_queue()
            result = ""
            persons = self.queue.get_queue()
            for person_id in range(len(persons)):
                result += f"{str(person_id + 1)} {persons[person_id].get_name()} ({persons[person_id].get_id()})\n"
            return str(result)

        elif self.compare(command, self.COMMANDS[13]):
            self.NEXT_INPUT = "queue_edit_mode"
            self.im.set_next_method("queue_edit_mode")
            return self.queue_edit_mode(None)

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