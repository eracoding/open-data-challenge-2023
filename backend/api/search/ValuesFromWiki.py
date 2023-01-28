from api.search import SearchText
from core.models import Category, WikiKeys


class ValuesFromWiki:
    def __init__(self):
        self.search = SearchText()

    def _findKeysForSearchInWiki(self):
        all_category = Category.objects.all()
        search_in_wiki_keys = []
        for item in all_category:
            keys = self.search.getKeys(item.category)
            db_keys = WikiKeys.objects.filter(key__in=keys).all()
            keys = [key for key in keys if key not in db_keys]
            search_in_wiki_keys += keys
        return search_in_wiki_keys

    def resultValueFromWiki(self):
        wiki_keys = self._findKeysForSearchInWiki()
        values = []
        for item in wiki_keys:
            values.append(self.search.getValues(item))
        return values
