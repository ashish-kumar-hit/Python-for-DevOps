# Attribute Error
If Something is not part of in-build function then it will through error
result = "Hello"
print(length(result)) # Here length is not partof in-build function replace it with len

# Function Call
print(result.upper)
Here you are not calling the function that's why you will only get adress of this result.

# Name Error
If you won't define the variable type
a = EC2
print(a)