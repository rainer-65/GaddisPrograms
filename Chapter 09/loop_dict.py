# Dictionary with children and their ages

person = {"David": 12, "John": 8, "Jill": 7}

# Printing keys
for name in person.keys():
    print(f'Name: {name}')

# Printing values
for age in person.values():
    print(f'Age: {age}')

# Printing keys and values
for name, age in person.items():
    print(f'Name: {name}, Age: {age}')

# Alternative using enumerate (i = index)
for i, (name, value) in enumerate(person.items()):
    print(f'Index: {i}, Name: {name}, Age: {value}')
