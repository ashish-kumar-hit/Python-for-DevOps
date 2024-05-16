my_dict = {"name": "Ashish", "Education": "B Tech", "Age": 24}
print(my_dict["Age"])

# Add or modify element
my_dict["Age"] = 25
print(my_dict["Age"])

# Remove element
del my_dict["Education"]
print(my_dict)

# Check Key existance
if "Age" in my_dict:
    print("Available")

# Iterating throgh key, value element
my_dict = {"name": "Ashish", "Education": "B Tech", "Age": 24}
for key, value in my_dict.items():
    print(key, value)