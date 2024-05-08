# Concatenation
str1 = "hello"
str2 = "world"
result = str1 + " " + str2
print(result)

# length
print(len(result))

# Upper & Lower Case
print("UpperCase:", result.upper)
print("LowerCAse:", result.lower())

# Replace
text = " Python is  / Awesome "
print(text.replace("Awesome", "Great"))

# Split
print(text.split()) # If you won't provide anything in split then buy default it will consider space
print(text.split('/'))

# Strip
print(text.strip()) # Removes extra spaces from front and back

# Sub-string
text = "python is great"
sub = "is"
if sub in text:
    print(sub, ": THIS SUB-STRING FOUND IN TEXT")