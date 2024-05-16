# AttributeError
If Something is not part of in-build function then it will through error
result = "Hello"
print(length(result)) # Here length is not partof in-build function replace it with len

# Function Call
print(result.upper)
Here you are not calling the function that's why you will only get adress of this result.

# NameError
If you won't define the variable type
a = EC2
print(a)

# ValueError
If you are trying to unpack two values then you need to provide the combination of two values from your variable

my_dict = {"name": "Ashish", "Education": "B Tech", "Age": 24}
for key, value in my_dict:
    print(key, value)

# TypeError
Builtin_functions or methods are not iterable
This error will come when you forget to call function

my_dict = {"name": "Ashish", "Education": "B Tech", "Age": 24}
for key, value in my_dict.items:
    print(key, value)

# JSON decode Error
It means the data is not convertable to Json, check wheather you are fetching data from right url(I mean right API)