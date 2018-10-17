import bs4
import requests

from ArrayEditor import ArrayEditor
from Parse.Parser import Parser


class Schedule(Parser):

    week_days_dict = {"monday": 0,
                      "tuesday": 1,
                      "wednesday": 2,
                      "thursday": 3,
                      "friday": 4,
                      "saturday": 5,
                      "sunday": 6}

    def __init__(self, group_name: str):
        super().__init__()
        _SCHEDULE_PAGE_PARITY =\
            f"http://www.ifmo.ru/ru/schedule/0/{group_name}/1/raspisanie_zanyatiy_{group_name}.htm"
        _SCHEDULE_PAGE_NOT_PARITY = \
            f"http://www.ifmo.ru/ru/schedule/0/{group_name}/2/raspisanie_zanyatiy_{group_name}.htm"

        self.PARITY_SCH = bs4.BeautifulSoup(requests.get(_SCHEDULE_PAGE_PARITY).text, "html.parser")
        self.NOT_PARITY_SCH = bs4.BeautifulSoup(requests.get(_SCHEDULE_PAGE_NOT_PARITY).text, "html.parser")


    def test(self):
        times = []
        pairs = []
        for i in self.PARITY_SCH.select(".time"):
            times.append(self.clean_all_tag_from_str(str(i)))

        for j in self.PARITY_SCH.select(".lesson"):
                pairs.append(self.clean_all_tag_from_str(str(j)))

        print(times)
        print(pairs)