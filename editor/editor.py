class Edit:

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
            if Edit.clean_tag_from_str(str(i)) != "":
                result.append(i)

        return result

    @staticmethod
    def clean_str_from_symbol(string, open_symbol, close_symbol=None, clean_content=True):
        append = True
        res = ""
        for letter in list(string):
            if letter == open_symbol:
                append = False

            if append:
                res += letter
            else:
                if not clean_content:
                    append = True

            if letter == close_symbol:
                append = True

        return res
