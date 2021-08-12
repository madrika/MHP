import re

search = re.findall("^(.+)@(.+)\.(info|com|net|org)$","""fariborz@gmai.com
fallahzadeh@yahoo.com
test@123.best
ali@techone24.org""",re.MULTILINE)

for src in search:
    print(src[1]+"."+src[2])