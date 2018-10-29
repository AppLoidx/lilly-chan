import random
from parser_m.date import Date
from group_queue.person import Person
from group_queue.history import History


class Queue:

    def __init__(self):
        self._queue_list = self._set_group_list()
        self._GROUP_LIST = self._queue_list

        # Номер текущей очереди
        self._queue_value = 0

        # Работа с историей
        self.history = History()

        # Для работы со временем
        self.date = Date()

    @staticmethod
    def _set_group_list():
        """
        Получает список группы из файла groupList.txt или groupListWindow.txt в зависимости от кодировки
        :return: сгенерированный список группы с элементами Person
        """
        filename = "group_queue/groupList.txt"

        file = open(filename, "r", encoding="UTF-8")
        group_list = []
        while True:

            f = file.readline().split()
            if not f:
                break

            group_list.append(Person(f[0], f"{f[1]} {f[2]}"))

        return group_list

    def new_queue(self, group_list: list=None) -> None:
        """
        Создание новой очереди, начиная с рандомно выбранного человека
        :param group_list: список группы с классами  Person
        :return: None
        """
        if group_list is None:
            group_list = self._queue_list
        self._queue_list = self._create_queue(random.randint(0, 27), group_list)

        self.history.write("Создана новая очередь")

    @staticmethod
    def _create_queue(start_person_id: int, group_list: list) -> list:
        """
        Создает очередь с человека заданного по индексу
        :param start_person_id: индекс человека с которого начинается очередь
        :param group_list: список людей занимающих очередь
        :return: массив с очередью
        """
        queue = []
        for i in range(len(group_list)):
            index = i + start_person_id - 1

            # При переполнении
            if index >= len(group_list):
                index -= len(group_list)

            queue.append(group_list[index])

        return queue

    def person_passed(self) -> None:
        """
        Вызывается когда кто-то прошел очередь. Инициализирует сдвиг очереди
        :return: None
        """
        self._queue_list[self._queue_value].set_passed(True)
        self._queue_value += 1

        # При переполнении
        if self._queue_value == len(self._queue_list):
            self._queue_value -= len(self._queue_list)

        self.history.write(f"{self._queue_list[self._queue_value].get_id()}"
                           f" {self._queue_list[self._queue_value].get_name()}"
                           f" прошел очередь в {self.date.get_time()}")

    def get_last_person_in_queue(self) -> Person:
        """

        :return: Предыдущий в очереди
        """
        # TODO: Rewrite for the queue with re-turn (Add new boolean variable)
        if self._queue_value == 0:
            return Person("0", "None")
        else:
            return self._queue_list[self._queue_value - 1]

    def get_current_person_in_queue(self) -> Person:
        """

        :return: Текущий в очереди
        """
        return self._queue_list[self._queue_value]

    def get_next_person_in_queue(self) -> Person:
        """

        :return: Следующий в очереди
        """
        if self._queue_value == len(self._queue_list) - 1:
            return self._queue_list[0].get_name()
        else:
            return self._queue_list[self._queue_value + 1]

    def get_queue(self) -> list:
        """
        Получение списка очереди
        :return: список очереди, элементы которой типа Person
        """
        return self._queue_list

    def get_person_queue_position(self, person_id: str) -> int:
        """
        Возвращает текущую позицию в очереди по номеру в списке
        :param person_id: номер в списке
        :return: номер в очереди. 0 - если не найден в очереди
        """
        for i in range(len(self._queue_list)):
            if self._queue_list[i].get_id() == person_id:
                return i + 1
        return 0

    def delete_person(self, person_id: str):
        """
        Удаление персонажа с очереди
        :param person_id: номер ИСУ
        :return: None
        """
        person_position = self.get_person_queue_position(person_id) - 1
        del self._queue_list[person_position]
        self.history.write(f"{self._queue_list[person_position].get_name()} удален из очереди в {self.date.get_time()}")

    def add_person(self, person_id: str, position: int=-1):

        new_queue_list = []

        if position == -1:
            for person in self._GROUP_LIST:
                if person.get_id() == person_id:
                    self._queue_list.append(person)

                    self.history.write(f"В конец очереди добавлен {person.get_name()} в {self.date.get_time()}")

        elif position == len(self._queue_list) + 1:
            for person in self._GROUP_LIST:
                if person.get_id() == person_id:
                    self._queue_list.append(person)
                    self.history.write(f"В позицию {position}"
                                       f" добавлен {person.get_name()} в"
                                       f" {self.date.get_time()}")

        else:
            for i in range(len(self._queue_list)):
                if i + 1 == position:
                    for person in self._GROUP_LIST:
                        if person.get_id() == person_id:
                            new_queue_list.append(person)
                            self.history.write(f"В позицию {position}"
                                               f" добавлен {person.get_name()} в"
                                               f" {self.date.get_time()}")

                new_queue_list.append(self._queue_list[i])

            self._queue_list = new_queue_list

    def swap(self, person1_id: str, person2_id: str):
        """
        Меняет местами двух людей
        :param person1_id: номер ИСУ первого
        :param person2_id: номер ИСУ второго
        :return: None
        """
        for index1 in range(len(self._queue_list)):
            if self._queue_list[index1].get_id() == person1_id:

                for index2 in range(len(self._queue_list)):
                    if self._queue_list[index2].get_id() == person2_id:
                        temp = self._queue_list[index1]
                        self._queue_list[index1] = self._queue_list[index2]
                        self._queue_list[index2] = temp

                        self.history.write(f"Поменялись местами: "
                                           f"{self._queue_list[index1].get_name()} <-> "
                                           f"{self._queue_list[index2].get_name()}"
                                           f" в {self.date.get_time()}")

                        return

    def test(self):
        self.new_queue()
        return self.get_queue()
