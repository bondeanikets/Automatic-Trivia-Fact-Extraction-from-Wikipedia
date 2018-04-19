import pywikibot
import wiki2plain
import re
import random
from nltk.stem.porter import *
from nltk.corpus import stopwords

class WikiParser:
    def __init__(self):
        print("Making the Instance of Wiki parser.")
        self.site = pywikibot.Site('en', 'wikipedia')
        self.cache_stem = {}
        self.stemmer = PorterStemmer()
        self.stop_words = set(stopwords.words('english'))
        self.k = 50

    def getEntityTokens(self, wiki_entity):
        site = pywikibot.Site('en', 'wikipedia')
        page = pywikibot.Page(site, wiki_entity)  #here we just crawl for the new entry
        text = page.text
        wiki2plain_instance = wiki2plain.Wiki2Plain(text)  #make the text to plain text
        text = wiki2plain_instance.text
        text = text.lower()  #convert all the text to lower case. Case folding
        current_tokens = filter(None, re.split('\W+', text))  #get the tokens now
        current_tokens = [word for word in current_tokens if not word in self.stop_words]
        token_freq_map = {}
        for token in current_tokens:
            token = self.cacheInStem(token)
            if token not in token_freq_map:
                token_freq_map[token] = 1.0
            else:
                token_freq_map[token] += 1.0
        return token_freq_map

    def getCategoryForEntity(self, wiki_entity):
        site = pywikibot.Site('en', 'wikipedia')
        page = pywikibot.Page(site, wiki_entity)
        cat_values = page.categories()
        cat_list = list(cat_values)
        cat_names = []
        for cat in cat_list:
            if not cat.isHiddenCategory():
                cat_names.append(cat.title())
        return cat_names



    def getEntityforCategory(self, category):
        site = pywikibot.Site('en', 'wikipedia')
        catdata = pywikibot.Category(site, title=category)
        entities = catdata.articles()
        return self.getRefinedEntity(entities)

    def cacheInStem(self, token):
        if token not in self.cache_stem:
            self.cache_stem[token] = self.stemmer.stem(token)
        return self.cache_stem[token]

    def getRefinedEntity(self, entities):
        refinedEntity = []
        list_entities = list(entities)
        if len(list_entities) <= self.k:
            for entity in entities:
                refinedEntity.append(entity.title())
            return refinedEntity
        else:
            range_entity = range(0, len(list_entities))
            list_sample = random.sample(range_entity, self.k)
            for i in range(0, self.k):
                refinedEntity.append(list_entities[list_sample[i]].title())
            return refinedEntity


