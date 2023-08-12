# from https://www.geeksforgeeks.org/comprehensions-in-python/
# Constructing output list WITHOUT using List comprehensions
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]

output_list = []

# Using loop for constructing output list
for var in input_list:
    if var % 2 == 0:
        output_list.append(var)

print("Output List using for loop:", output_list)

# Using List comprehensions for constructing output list

input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]

list_using_comp = [var for var in input_list if var % 2 == 0]

print("Output List using list comprehensions:",
      list_using_comp)

# Constructing output list using list comprehension
list_using_comp = [var ** 2 for var in range(1, 10)]

print("Output List using list comprehension:",
      list_using_comp)

# Computing the numbers less than 100, which are divisible by 2 and 5 both
list_using_comp = [x for x in range(100) if x % 2 == 0 if x % 5 == 0]
print("Output List using list comprehension:", list_using_comp)

# Computing prime numbers up to 100
list_using_comp = [x for x in range(2, 100) if all(x % y for y in range(2, x // 2))]
print("Output List using list comprehension:", list_using_comp)
