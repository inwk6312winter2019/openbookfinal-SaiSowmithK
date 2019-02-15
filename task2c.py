
from collections import Counter
def corm(file):
    d = {"chrome":0,"Firefox":0}
    opened_file = open(file, 'r')
    content = opened_file.readlines()
    content = [x.strip() for x in content]
            if "Chrome" in i:
            d["chrome"] = d["chrome"] + 1 
            if "Firefox"|| "Mozilla" in i:
            d["Firefox"] = d["Firefox"] + 1  
    opened_file.close()
    return d
print(corm("access.log"))
