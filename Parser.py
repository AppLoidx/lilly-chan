import bs4
import requests
import time


class Parser:

    tm = time.localtime()

    def __init__(self):
        self.s = None
        self.b = None

    LAST_USER_NAME = None

    def get_user_name_from_vk_id(self, user_id):

        s = requests.get("https://vk.com/id"+str(user_id))
        b = bs4.BeautifulSoup(s.text, "html.parser")

        user_name = self.clean_tag_from_str(b.findAll("title")[0])

        self.LAST_USER_NAME = user_name
        return user_name

    @staticmethod
    def clean_tag_from_str(string):

        s = ""
        for char in string:
            s += char
        return s

    @staticmethod
    def clean_all_tag_from_str(string_line):

        """
        Очистка строки stringLine от тэгов и их содержимых
        :param string_line: Очищаемая строка
        :return: очищенная строка
        """

        result = ""
        not_skip = True
        for i in list(string_line):
            if not_skip:
                if i == "<":
                    not_skip = False
                else:
                    result += i
            else:
                if i == ">":
                    not_skip = True
        return result

    def set_http(self, http: str):
        self.s = requests.get(http)
        self.b = bs4.BeautifulSoup(self.s.text, "html.parser")

    def get_weather_today(self, city: str = "санкт-петербург") -> list:

        http = "https://sinoptik.com.ru/погода-" + city
        self.set_http(http)

        p3 = self.b.select('.temperature .p3')
        weather1 = p3[0].getText()
        p4 = self.b.select('.temperature .p4')
        weather2 = p4[0].getText()
        p5 = self.b.select('.temperature .p5')
        weather3 = p5[0].getText()
        p6 = self.b.select('.temperature .p6')
        weather4 = p6[0].getText()

        result = ''
        result = result + ('Утром :' + weather1 + ' ' + weather2) + '\n'
        result = result + ('Днём :' + weather3 + ' ' + weather4) + '\n'
        temp = self.b.select('.rSide .description')
        weather = temp[0].getText()
        result = result + weather.strip()

        return result

    @staticmethod
    def get_schedule_from_file(filename, day, week):

        f = open(filename, 'r')
        group_name = f.readline()
        _DAY, _TIME, _WEEK, _AUD, _DIS, _TEACHER = f.readline().split()
        temp = "."
        result = group_name + "\nРасписание на " + day + ":\n\n"
        while (temp[0] != "end"):
            temp = f.readline().split()
            if temp[0] == day and (temp[2] == week or temp[2] == "все"):
                result += _TIME + ": " + temp[1] + "\n" \
                          + _AUD + ": " + temp[3] + "\n" \
                          + _DIS + ": " + temp[4] + "\n" \
                          + _TEACHER + ": " + temp[5]
                result += "\n" + "-----\n"
        return result

    def get_date(self) -> str:

        """Возвращает дату в формате [(день).(месяц).(год)]"""

        return str(self.tm.tm_mday) + "." + str(self.tm.tm_mon) + "." + str(self.tm.tm_year)

    def get_time(self) -> str:

        """Возвращает время в формате [(часы) : (минуты)]"""

        return str(self.tm.tm_hour)+" : "+str(self.tm.tm_min)

    def get_day_now(self) -> str:

        return str(self.tm.tm_mday)