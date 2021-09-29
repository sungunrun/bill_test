import re

x = "_ability_"
repl = '( |\n|—|\.|\,)'
searchterm = re.sub('(_)', repl, x)
text = "this ability\nbut—ability is\nability is something\nthis is my ability. But\n how about ability.\n Every ability, is\n"
finds = re.finditer(searchterm, text, flags=re.IGNORECASE)
matchset = set()
for find in finds:
    matchset.add(find.group())
for match in matchset:
    text = re.sub(match, "<span>"+match+"</span>", text)
print(text)
