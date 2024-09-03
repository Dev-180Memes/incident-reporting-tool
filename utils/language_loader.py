import json
import os


class LanguageLoader:
    def __init__(self, language="en"):
        self.language = language
        self.translations = self.load_language()

    def load_language(self):
        locale_path = os.path.join("locales", f"{self.language}.json")
        with open(locale_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def get_translation(self, key):
        return self.translations.get(key, key)
