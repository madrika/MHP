import re

str = "hello world"

#Check if the string starts with 'hello':

x = re.findall("^hello", str)
if (x):
  print("Yes, the string starts with 'hello'")
else:
  print("No match")