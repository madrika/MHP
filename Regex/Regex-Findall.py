import re

search = re.findall("Line[0-9]",""""Line1
Line2
Line3
Line4""")
for src in search:
    print("{}".format(src))
    
