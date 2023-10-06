# A tuple is a sequence of immutable(!) Python objects. Tuples are sequences, just like lists
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"

# Empty tuple
tup4 = ()

# Tuple containing a single value
tup5 = (50,)

# Accessing Values in Tuples
print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])

# Updating Tuples
tup6 = (12, 34.56)
tup7 = ('abc', 'xyz')
# Following action is not valid for tuples because they are not mutable
# tup6[0] = 100;
# Using a list (which is mutable)
tup6 = list(tup6)
tup6[0] = 100
print(tuple(tup6))

# Deleting Tuple Elements
tup9 = ('C#', 'Python', 'Java', 'JavaScript')
# tuple = class for generating a tuple object
tup10 = tuple(item for item in tup9 if item != 'Java')
print(tup10)

# Basic Tuple operations
print("Length is: ", len((1, 2, 3)))  # length
print("Concatenation: ", (1, 2, 3) + (4, 5, 6))  # concatenation
print("Repetition: ", ('Hi!',) * 4)  # repetition
print("Membership: ", 3 in (1, 2, 3))  # membership
for x in (1, 2, 3):  # iteration
    print(x, end=' ')
