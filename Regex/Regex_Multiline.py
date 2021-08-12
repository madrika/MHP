import re

search = re.search("^Line[0-9].+",""""absdc Line1 asdfrd
asdfrd Line2 asdfr 
Line3 alsdfgtf""",re.MULTILINE)
print(search.group())


