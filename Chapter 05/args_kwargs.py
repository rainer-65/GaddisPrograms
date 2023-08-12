# Source: https://www.freecodecamp.org/news/args-and-kwargs-in-python/ (adapted)
# How to Use *args in Python
# *args allows us to pass a variable number of non-keyword arguments to a Python function
def add(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total


print(add(2, 3))
print(add(2, 3, 5))
print(add(ord('c'), ord('d')))
print(add(2, 3, 5, 7))
print(add(2, 3, 5, 7, 9))
print(add(2.6, 3.7, 5.2))


# How to Use **kwargs in Python
# **kwargs allows us to pass a variable number of keyword arguments to a Python function

def total_fruits(**fruits):
    total = 0
    print(type(fruits))  # Type Dictionary
    for amount in fruits.values():
        total += amount
    return total


print(total_fruits(banana=5, mango=7, apple=8))
print(total_fruits(banana=5, mango=7, apple=8, oranges=10))
print(total_fruits(banana=5, mango=7))
