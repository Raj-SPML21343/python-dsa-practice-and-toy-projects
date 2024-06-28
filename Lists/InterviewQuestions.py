#   Created by Elshad Karimov, Updated by Rajesh Berepalli
#   Basic Problems on Arrays/ Lists

#  Missing Number

import numpy as np
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
           51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]


def missing_number(arr, n):
    # Calculate the sum of first n natural numbers
    total = n * (n + 1) // 2

    # Calculate the sum of numbers in the array
    sum_arr = sum(arr)

    # Find the missing number by subtracting sum_arr from total
    missing = total - sum_arr

    return missing


print("Question 1: ")
print(f"missing number = {missing_number([1, 3, 2, 5, 6], 6)}")
#  Find Pairs
#  LeetCode 1 - Two Sum


def find_pairs(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                continue
            elif nums[i] + nums[j] == target:
                print(i, j)


print("Question 2:")
myList = [1, 2, 3, 2, 3, 4, 5, 6]
find_pairs(myList, 6)

# Leetcode answer


def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i


# Find a number
my_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                    12, 13, 14, 15, 16, 17, 18, 19, 20])


def find_number(array, number):
    flag = True
    for i in range(len(array)):
        if array[i] == number:
            print(i)
            flag = False
    if flag:
        print("Given Number is not found in array")


print("Question 3: ")
find_number(my_array, 21)

# Find max product of two integer


def max_product(arr):
    # Initialize two variables to store the two largest numbers
    max1, max2 = 0, 0  # O(1), constant time initialization

    # Iterate through the array
    for num in arr:  # O(n), where n is the length of the array
        # If the current number is greater than max1, update max1 and max2
        if num > max1:  # O(1), constant time comparison
            max2 = max1  # O(1), constant time assignment
            max1 = num  # O(1), constant time assignment
        # If the current number is greater than max2 but not max1, update max2
        elif num > max2:  # O(1), constant time comparison
            max2 = num  # O(1), constant time assignment

    # Return the product of the two largest numbers
    return max1 * max2  # O(1), constant time multiplication


print("Question 4: ")
arr = [1, 7, 3, 4, 9, 5]
print(max_product(arr))  # Output: 63 (9*7)

# findMaxProduct(myArray)


# Middle
def middle(lst):
    # Return a new list containing all elements from the original list, excluding the first and last elements
    return lst[1:-1]


my_list = [1, 2, 3, 4]
print("Question 5:")
print(middle(my_list))  # Output: [2, 3]

# 2D List


def diagonal_sum(matrix):
    # Initialize the sum to 0
    total = 0

    # Iterate through the rows of the matrix
    for i in range(len(matrix)):
        # Add the diagonal element to the total sum
        total += matrix[i][i]

    return total

# Best Score


def first_second(my_list):
    max1, max2 = float('-inf'), float('-inf')

    for num in my_list:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and num != max1:
            max2 = num

    return max1, max2


print("Question 7: ")
my_list = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]
print(first_second(my_list))  # Output: (90, 87)

# Duplicate Numbers


def remove_duplicates(lst):
    return list(set(lst))


print("Question 8:")
my_list = [1, 1, 2, 2, 3, 4, 5]
print(remove_duplicates(my_list))  # Output: [1, 2, 3, 4, 5]

# Pairs


def pair_sum(arr, target_sum):
    result = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                result.append(f"{arr[i]}+{arr[j]}")
    return result


arr = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
target_sum = 7
print("Question 9: ")
print(pair_sum(arr, target_sum))  # Output: ['2+5', '4+3', '3+4', '-2+9']

# Contains Duplicate


def contains_duplicates(nums):
    return len(nums) != len(set(nums))


# Example usage
print("Question 10: ")
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
print(contains_duplicates(nums))  # Output: True


# Permutation

def permuntation(list1, list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    return False


print("Question 11: ")
list1 = ['g', 'a', 'y', 'u']
list2 = ['y', 'u', 'g', 'a']
print(permuntation(list1, list2))

# Rotate Matrix


def rotate(matrix):

    # step1 : find Transpose of a matrix
    N = len(matrix)
    for i in range(N):
        for j in range(i, N):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # step2: change the columns s.t col 0 <-> col N-1, col 1 <-> col N-2, so on..
    for i in range(N):
        for j in range(N//2):
            matrix[i][j], matrix[i][-1-j] = matrix[i][-1-j], matrix[i][j]


print("Question 12: ")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate(matrix)
print(matrix)
