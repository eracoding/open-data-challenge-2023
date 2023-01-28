import os
import re
import time
import json
import requests
import random

from backend.settings import BASE_DIR


class SearchText:
    # REG_EX = "(src=\"//avatars[\w.?=&;,://-]*\")"
    # KEY_SEARCH = "https://yandex.ru/images/search?from=tabbar&text="
    KEY_SEARCH = "https://uz.wikipedia.org/w/rest.php/v1/search/page?limit=3&q="
    VALUE_SEARCH = "https://uz.wikipedia.org/w/rest.php/v1/page/"

    def getKeys(self, search):
        req = requests.get(self.KEY_SEARCH + search)
        text = req.text
        data = json.load(text)
        data = [el['key'] for el in data['pages']]
        return data

    def getValues(self, category):
        req = requests.get(self.VALUE_SEARCH + category)
        data = json.loads(req.text)['source']
        if data[0] == '{':
            data = data[data.find('}') + 2:]
        data = re.sub(r"[\[!@#$\]|/{}'\n\xa0]", '', data)
        data = re.sub(r"<[^>]*>", '', data)
        data = re.sub(r'http\S+', '', data)
        data = data[:data.find('==')]
        return data
