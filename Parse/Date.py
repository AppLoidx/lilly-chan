from Parse.Parser import Parser


class Date(Parser):
    MONTH = {"ОКТЯБРЬ": 10, "НОЯБРЬ": 11, "ДЕКАБРЬ": 12}

    def __init__(self):

        super().__init__()
        self.set_http("https://my-calend.ru/date-and-time-today")
        self._date = self.clean_all_tag_from_str(self.b.select(".page")[0].findAll("h2")[0]).split(",")
        self._day_of_week = self._date[1]

    def get_date(self):
        return self._date[0] + self._date[1]

    def get_day_of_week(self):
        return self._date[1]

    def get_time(self):
        return self.clean_all_tag_from_str(str(self.b.select(".page")[0].findAll("h2")[1]))

