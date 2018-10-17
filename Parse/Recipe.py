from Parse.Parser import Parser


class Recipe(Parser):
    """ Парсим рецепты с сайта russianfood.com """

    _BREAKFAST_HTTP = "https://www.russianfood.com/recipes/bytype/?fid=926"  # рецепты на завтрак
    _LUNCH_HTTP = "https://www.russianfood.com/recipes/bytype/?fid=927"  # на обед
    _SUPPER_HTTP = "https://www.russianfood.com/recipes/bytype/?fid=928"  # на ужин

    def get_breakfast(self, food_type="breakfast"):

        """
        Получение рецепта для завтрака
        :param food_type задается тип еды нижним регистром
            breakfast
            lunch
            supper
        :return: возвращает рецепты
        """

        result = [0]
        if food_type == "breakfast":
            self.set_http(self._BREAKFAST_HTTP)
        elif food_type == "lunch":
            self.set_http(self._LUNCH_HTTP)
        else:
            self.set_http(self._SUPPER_HTTP)

        a = self.b.findAll(attrs={"class": "title"})
        for i in range(len(a)):
            temp = str(a[i])
            if i > 2 & i < 70:
                try:
                    name = self.clean_all_tag_from_str(str(a[i]).split("\n")[1])
                    http = "https://www.russianfood.com/" + ''.join(list(temp.split("\n")[1])[9:39])
                    result.append([name, http])
                except IndexError:
                    pass
        return result
