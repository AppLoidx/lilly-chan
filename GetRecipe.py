import bs4
import requests

from Parser import Parser


class GetRecipe(Parser):

    _BREAKFAST_HTTP = "https://www.russianfood.com/recipes/bytype/?fid=926"
    _LUNCH_HTTP = "https://www.russianfood.com/recipes/bytype/?fid=927"
    _SUPPER_HTTP = "https://www.russianfood.com/recipes/bytype/?fid=928"

    def get_breakfast(self):
        result = [0]
        self.set_http(self._BREAKFAST_HTTP)
        a = self.b.findAll(attrs={"class": "title"})
        for i in range(len(a)):
            temp = str(a[i])
            if i > 2 & i < 70:
                try:
                    name = self.clean_tag_from_str(str(a[i]).split("\n")[1])
                    http = "https://www.russianfood.com/" + ''.join(list(temp.split("\n")[1])[9:39])
                    result.append([name, http])
                except IndexError:
                    pass
        return result

    def clean_tag_from_str(self, stringLine):
        result = ""
        not_skip = True
        for i in list(stringLine):
            if not_skip:
                if i == "<":
                    not_skip = False
                else:
                    result += i
            else:
                if i == ">":
                    not_skip = True
        return result
