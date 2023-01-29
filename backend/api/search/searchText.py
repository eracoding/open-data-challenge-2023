import os
import re
import time
import json
import requests
import random

from backend.settings import BASE_DIR
import wikipedia


class SearchText:
    # REG_EX = "(src=\"//avatars[\w.?=&;,://-]*\")"
    # KEY_SEARCH = "https://yandex.ru/images/search?from=tabbar&text="
    KEY_SEARCH = "https://uz.wikipedia.org/w/rest.php/v1/search/page?limit=1&q="
    VALUE_SEARCH = "https://uz.wikipedia.org/w/rest.php/v1/page/"

    def getKeys(self, search):
        print(search)
        res = wikipedia.search(search)
        if len(res) > 0:
            return [res[0]]
        return []

    def getValues(self, category):
        print("CHECK ID {}".format(category))
        print(category)
        wikipedia.set_lang("uz")
        content = wikipedia.page(title=category).content
        content = re.sub("===(.*?)===", "", content)
        content = re.sub("==(.*?)==", "", content)

        content = content.replace("=", '')
        content = content.replace("ʻ", "'")
        content = content.replace("ʼ", "'")
        content = content.replace("„", "")
        content = content.replace("“", "")
        content = content.replace(".", "\n")
        return content
