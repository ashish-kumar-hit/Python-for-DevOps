import re
text = "The quick brown fox"

# findall
pattern = r'brown'
search = re.search(pattern, text)

if search:
    print("Pattern Found:", search.group())
else:
    print("Pattern not found")

# match

# replace


# search


# split
