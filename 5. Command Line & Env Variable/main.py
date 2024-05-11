import sys, os

def addition(num1,num2):
    return num1 + num2

def subtract(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

num0 = sys.argv[1]
num1 = int(sys.argv[2])
num2 = int(sys.argv[3])

if num0 == "add":
    add = addition(num1,num2)
    print(add)

# To set env variable
# set password = "ashish" (Run in terminal)
password = os.getenv("password")
print(password)

