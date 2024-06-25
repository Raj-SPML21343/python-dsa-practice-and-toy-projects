import numpy as np
import array

# creating an arary
my_array = array.array('i')
# print(my_array)
my_array = array.array('i', [10, 2, 3, 10])
print(my_array)

np_array = np.array([], dtype=int)
# print(np_array)
np_array = np.array([1, 2, 3, 'q', 1.0])
# print(np_array)

# Inserting into an array
# print(my_array)
my_array.insert(0, 6)   # syntax: array.insert(index, value)
print(my_array)

# Array Traversal


def traverse_array(array):
    for ele in array:
        print(ele, ele + 10)


traverse_array(my_array)

# Access array elements


def access_array_elements(array, index):
    if index >= len(array):
        print("pls provide the index less than length of the array")
    else:
        print(array[index])


access_array_elements(my_array, 0)

# Searching for an element in an array


def linear_search(array, tar):
    for i, ele in enumerate(array):
        if ele == tar:
            return i, array[i]
    return None


print(linear_search(my_array, 10))

# Delete/ Remove an element from an array
my_array.remove(10)
print(my_array)
