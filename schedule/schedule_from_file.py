from schedule.day import Day


class ScheduleFromFile:

    @staticmethod
    def get_schedule_from_file(filename, day, week_parity):
        """
        :param filename: путь к файлу с расписанием .
        Формат файла:
            (1 строка - Заголовок расписания, возвращается как первая строка
            2 строка - указание названий столбцов (необязательно, но строка должна быть)
            С третьего начинаются дни с парами в формате:
            <День недели> <Время> <четность недели> <аудитория> <предмет> <преподаватель>

        :param day: день недели - среда, вторник и тд в именительном падеже т.к. идет абсолютное сравнивание
        :param week_parity: четность недели: четная, нечетная либо 0 - четная или 1 - нечетная
        :return: Возвращает отформатированное расписание
        """
        if week_parity.upper() == "ЧЕТНАЯ" or str(week_parity) == "0":
            week = "чет"
        elif week_parity.upper() == "НЕЧЕТНАЯ" or str(week_parity) == "1":
            week = "нечет"
        else:
            return "Не правильно введана четность недели. Простите! Возможно, это ошибка программы..." \
                   "Пожалуйста, сообщите моему создателю."

        f = open(filename, 'r', encoding="UTF-8")
        group_name = f.readline()
        _DAY, _TIME, _WEEK, _AUD, _DIS, _TEACHER = f.readline().split()
        temp = "."
        result = group_name + f"\nРасписание: \nДень: {day}\nНеделя : {week_parity}\n\n"

        while temp[0] != "end":
            temp = f.readline().split()
            if temp[0].upper() == day.upper() and (temp[2] == week or temp[2] == "все"):
                result += _TIME + ": " + temp[1] + "\n" \
                          + _AUD + ": " + temp[3] + "\n" \
                          + _DIS + ": " + temp[4] + "\n" \
                          + _TEACHER + ": " + temp[5]

                result += "\n" + "-----\n"

        return result

    def get_schedule(self, next_day_value: int = 0):
        """

        :param next_day_value: number of days to skip
        :return: formatted schedule
        """

        # Файлы с разными кодрировками
        sh_filename = "schedule/sh.txt"

        day = Day()
        today_day, week_parity = day.get_day_parity(next_day_value)

        return self.get_schedule_from_file(sh_filename, today_day, week_parity)