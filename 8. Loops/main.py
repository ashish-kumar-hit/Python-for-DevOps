fruits = ["apple","mango","banana","orange","pomogranate"]

for i in fruits:
    print(i)

count = 0
while count <=3:
    print(count)
    count+=1

# break
for i in fruits:
    if i == "banana":
        break
    print(i)

# continue
for i in fruits:
    if i == "orange":
        continue
    print(i)

