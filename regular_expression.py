import re

str1 = "Hello, World!"
pattern = r"Hello"
if re.match(pattern, str1):
    print("Match found")
else:
    print("Match not found")