import re

x = "_ability_"

repl = '( |\n|—|\.|\,)'
searchterm = re.sub('(_)', repl, x)
text = "this ability\nbut—ability is\nability is something\nthis is my ability. But\n how about ability.\n Every ability, is\nand ability\n to"
finds = re.finditer(searchterm, text, flags=re.IGNORECASE)
matchset = set()
for find in finds:
    matchset.add(find.group())
print(matchset)
for match in matchset:
    if '\n' in match:
        replacement = ''
        for component in match.split('\n'):
            if component=='':
                replacement = replacement+'\n'
            else:
                replacement = replacement + "<span style=\"background-color:yellow\">"+component+"</span>"
        print(repr(match))
        print(repr(replacement))
    else:
        replacement = "<span style=\"background-color:yellow\">"+match+"</span>"
    text = re.sub(match, replacement, text)
# print(text)
