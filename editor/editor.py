class ArrayEdit():

    @staticmethod
    def clean_tag_from_str(string_line):
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

    @staticmethod
    def clean_spaces_from_array(array: list):
        result = []
        for i in array:
            if ArrayEdit.clean_tag_from_str(str(i)) != "":
                result.append(i)

        return result
