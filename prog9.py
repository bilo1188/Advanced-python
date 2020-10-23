'''
lambda argument : manipulate(arg)
'''
#simple add function

def add(a,b):
    x = a+b
    return x

print(add(2,3))

#using lambda

y = lambda  a,b :a+b
print(y(30,20))
