import re
text = "The quick brown fox"

# findall
pattern = r'brown'
search = re.search(pattern, text)
if search:
    print("Pattern Found:", search.group())
else:
    print("Pattern not found")

# match (Checks the match with first letter)
pattern = r'quick'
match = re.match(pattern, text)
if match:
    print("Match Found:", match.group())
else:
    print("No Match Found")

# replace
replacement = "red"
new_txt = re.sub(pattern,replacement,text)
print(new_txt)

# search
serach = re.search(pattern,text)
if search:
    print("Found:",search.group())
else:
    print("Not Found")

# split
text = "apple, banana, orange, grapes"
pattern = r','
split = re.split(pattern, text)
print(split)