#Advanced List Slicing

list_1 = [1,33,2,4,5,6,7,33,4,56,78,99]

#no of elements 7-1 = 6
print(list_1[1:7])
#out:[33, 2, 4, 5, 6, 7]
print(list_1[:7:2])
#out:[1, 2, 5, 7]


print(list_1[:-3])
#out:[1, 33, 2, 4, 5, 6, 7, 33, 4]

print(list_1[::-1])
#out:[99, 78, 56, 4, 33, 7, 6, 5, 4, 2, 33, 1]

print(list_1[-3::-1])

'''
a[-1]    # last item in the array
a[-2:]   # last two items in the array
a[:-2]   # everything except the last two items
a[::-1]    # all items in the array, reversed
a[1::-1]   # the first two items, reversed
a[:-3:-1]  # the last two items, reversed
a[-3::-1]  # everything except the last two items, reversed
'''
