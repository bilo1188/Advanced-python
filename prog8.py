''' map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)'''

def addition(n):
    return n+n

number = (1,2,3,4)

result = map(addition,number)
print(list(result))


''' The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not. '''
#example 1
# function that filters vowels
def fun(variable):
    letter = ['a','e','i','o','u']
    if variable in letter:
        return True
    else:
        return False
# sequence 
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
# using filter function
filtered = filter(fun,sequence)

print(list(filtered))


#example 2

# a list contain
seq = [0,1,2,3,4,5,6,7,8]

# result contains odd numbers of the list
result  = filter(lambda x:x%2 !=0 ,seq)
print(list(result))
# result contains even numbers of the list
result  = filter(lambda x:x%2 ==0 ,seq)
print(list(result))


''' The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.This function is defined in “functools” module.'''
# python code to demonstrate working of reduce() 
  
# importing functools for reduce() 
from functools import reduce

def addition(a,b):
    return a+b

list_1= [1,2,3,4]

result = reduce(addition,list_1)
print(result)
