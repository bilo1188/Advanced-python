'''
List Comprehension,
Dictionary Comprehension
And Generator Comprehension

'''
#list without comprehension

list_1 = [1,2,33,44,56,676,45,23,23]
divide_by_3 = []
print('list without comprehension')
for item in list_1:
    if item % 3 == 0:
        divide_by_3.append(item)
        print(item)

#List Comprehension

print('List Comprehension',[item for item in list_1 if item %3==0])      

'''//////////////Dictionary Comprehension/////////'''

dict_1 = {'a' : 10,'b' : 20 , 'A' : 5}
print('dic Comprehension',{k.lower():dict_1.get(k.lower(),0)+dict_1.get(k.upper(),0) for k in dict_1.keys()})

#set Comprehension

square = {x**2 for x in [1,2,2,3,3,4,44,5,55,5]}

print(square)

#Generator Comprehension

gen = (i for i in range(50) if i%3==0)
for item in gen:
    print(item)
 #we can also print out like this one by one
#print(gen.__next__())
