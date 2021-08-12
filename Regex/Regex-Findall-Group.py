import re

search = re.findall("^(919|912|911)([0-9]{7})$","""9121234567
9111234567
9191234567
""",re.MULTILINE)
for src in search:
    print(src[0]+src[1])