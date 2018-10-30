import requests
from config import yandex_translate_api


# TODO: Написать документацию
class Translate:

    _key = yandex_translate_api

    def translate(self, text, lang, to_lang=None):
        if to_lang is not None:
            lang = f"{lang}-{to_lang}"
        main_url = "https://translate.yandex.net/api/v1.5/tr.json/translate"
        response = requests.get(f"{main_url}?"
                                f"key={self._key}&"
                                f"lang={lang}&"
                                f"text={text}")

        return response.json()

    def lang_identify(self, text, hint="ru,en"):
        main_url = "https://translate.yandex.net/api/v1.5/tr.json/detect"
        response = requests.get(f"{main_url}?"
                                f"key={self._key}&"
                                f"hint={hint}&"
                                f"text={text}")

        return response.json()['lang']

    def translate_ru_en(self, text):
        if self.lang_identify(text) == "ru":
            to_lang = "en"
            from_lang = "ru"
        else:
            to_lang = "ru"
            from_lang = "en"

        return self.translate(text, from_lang, to_lang)['text'][0]

    def translate_to_ru(self, text, hint=None):
        if hint is None:
            hint = "ru,en"
        from_lang = self.lang_identify(text, hint)

        return self.translate(text, from_lang, "ru")

    def translate_to(self, text, to_lang, base_lang_hint=None):
        if base_lang_hint is None:
            base_lang_hint = "ru,en"
        from_lang = self.lang_identify(text, base_lang_hint)

        return self.translate(text, from_lang, to_lang)['text'][0]


