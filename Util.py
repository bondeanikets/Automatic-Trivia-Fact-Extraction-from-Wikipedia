import os
import wikipedia as wiki

#Utility Function to Load the GlobalIDF Function
def getglobalfreqdict(filename):
    indexdict = {}
    if os.path.exists(filename):
        if not os.path.getsize(filename)> 0:
            return None
        with open(filename) as f:
            data = f.readlines()
            for line in data:
                val = line.split()
                if len(val) == 2:
                    indexdict[val[0]] = float(val[1])
        return indexdict
    else:
        print("File Doesn't Exist")

def searchWiki(query_term):
    wiki.set_lang("en")
    search_result = wiki.search(query=query_term)
    if len(search_result):
        return search_result[0]
    else:
        print("No search Results found")
