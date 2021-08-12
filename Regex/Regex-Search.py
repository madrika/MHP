import re
search = re.search("Hello World","Hello World")
start = search.start()
end = search.end()
print("{} match starts at {} end at {}".format(search.group(),start,end))

#For Test Regex https://regex101.com/
