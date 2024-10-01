input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]

output_set = set()

# Using loop for constructing output set
for var in input_list:
    if var % 2 == 0:
        output_set.add(var)

print("Output Set using for loop:", output_set)

# Using Set comprehensions
# for constructing output set

input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]

set_using_comp = {var for var in input_list if var % 2 == 0}

print("Output Set using set comprehensions:",
      set_using_comp)

# Consider the set with some integers
my_set = {12, 34, 56, 3, 45, 67, 89, 1, 6}
print("Actual set: ", my_set)

# Create set by filtering greater than 25 using set comprehension
set_comprehension = {i for i in my_set if i > 25}
print("New Set: ", set_comprehension)

# Union of two sets
set_1 = {'Python', 'Java', 'C++', 'Kotlin'}
print(type(set_1))
set_2 = {'C#', 'Java', 'C++'}
set_union = set_1.union(set_2)
print("Union operation: ", set_union)

# Make a list out of the set
list_union = list(set_union)
print("Union operation: ", list_union)

# Turn the list into a dictionary with a dictionary comprehension
dict_union = {index: element for index, element in enumerate(list_union)}
print("Union operation: ", dict_union)
