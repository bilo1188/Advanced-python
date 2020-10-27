a = ['india','pak','usa','africa']

#normal method
i=0

for item in a:
    i = i + 1
    
    if i % 2== 0:
        
        
        print(item)
    
    
#by use enumerate function

for i , item in enumerate(a):
    if (i+1)%2==0:
        print(i,item)
        
