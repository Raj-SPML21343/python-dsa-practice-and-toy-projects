print("welcome DSA course")


def sum_n(n):
    if n <= 0:
        return 0
    num = n + sum_n(n-1)
    return num


# x = sum_n(3)
# print(x)

# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]
# list3 = list1 + list2
# print(list3)
# s = [-1, 1, 2, 3]
# new_list = [i*2 if i > 0 else i * 10 for i in s]
# print(new_list)
# print(type(s))


# a = [1, 2, 3, 4, 5]
# print(a[3:0:-1])
# fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
# fruit_list2 = fruit_list1
# fruit_list3 = fruit_list1[:]

# fruit_list2[0] = 'Guava'
# fruit_list3[1] = 'Kiwi'
# # print(fruit_list1)
# sum = 0
# for ls in (fruit_list1, fruit_list2, fruit_list3):
#     print(ls)
#     if ls[0] == 'Guava':
#         sum += 1
#     if ls[1] == 'Kiwi':
#         sum += 20

# print(sum)

def f(val, my_list):
    val += 1000
    my_list.append(4)


num = 10
print(type(num))
my_list = [1, 2, 3]
print(num, my_list)
f(num, my_list)
print(num, my_list)
