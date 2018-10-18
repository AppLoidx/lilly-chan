from parser.parser import Parser


class Date(Parser):
    MONTH = {"ОКТЯБРЬ": 10, "НОЯБРЬ": 11, "ДЕКАБРЬ": 12}

    def __init__(self):

        super().__init__()
        self.b = self.set_http("https://my-calend.ru/date-and-time-today")
        self._date = self.clean_all_tag_from_str(self.b.select(".page")[0].findAll("h2")[0]).split(",")
        self._day_of_week = self._date[1]

    def get_date(self):
        return self._date[0] + self._date[1]

    def get_day_of_week(self):
        return self._date[1]

    def get_time(self):
        self.b = self.set_http("https://my-calend.ru/date-and-time-today")
        return self.clean_all_tag_from_str(str(self.b.select(".page")[0].findAll("h2")[1])).split()[1]

    def get_week_parity(self):
        b_site = self.set_http("http://www.ifmo.ru/ru/schedule/0/P3112/raspisanie_zanyatiy_P3112.htm")

        return self.clean_all_tag_from_str(b_site.select(".schedule-week")[0].find("strong"))
