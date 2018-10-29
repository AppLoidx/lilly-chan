import bs4
import requests
import urllib.request
import time


class Parser:

    tm = time.localtime()

    def __init__(self):
        pass
    LAST_USER_NAME = None

    # TODO: Rewrite to class
    def get_user_name_from_vk_id(self, user_id):

        b = self.set_http("https://vk.com/id"+str(user_id))
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
        request = requests.get(http)
        bs = bs4.BeautifulSoup(request.text, "html.parser")

        return bs

    # TODO: Rewrite to class
    def get_weather_today(self, city: str = "санкт-петербург") -> list:

        http = "https://sinoptik.com.ru/погода-" + city
        b = self.set_http(http)

        p3 = b.select('.temperature .p3')
        weather1 = p3[0].getText()
        p4 = b.select('.temperature .p4')
        weather2 = p4[0].getText()
        p5 = b.select('.temperature .p5')
        weather3 = p5[0].getText()
        p6 = b.select('.temperature .p6')
        weather4 = p6[0].getText()

        result = ''
        result = result + ('Утром :' + weather1 + ' ' + weather2) + '\n'
        result = result + ('Днём :' + weather3 + ' ' + weather4) + '\n'
        temp = b.select('.rSide .description')
        weather = temp[0].getText()
        result = result + weather.strip()

        return result
