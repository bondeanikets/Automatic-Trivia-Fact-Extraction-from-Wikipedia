import wiki_parser

if __name__ == "__main__":
    wiki_parser = wiki_parser.WikiParser()
    wiki_parser.getEntityTokens("Barack Obama")
    wiki_parser.getEntityforCategory("Category:Writers from Chicago")
    print(wiki_parser.getCategoryForEntity("Lionel Messi"))

