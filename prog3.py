def studentmarks(*args):
    print('my name is' ,args[0],'my roll no is',args[1])
studentmarks('bilal',89)
def printmarks(**kwargs):
    for key,value in kwargs.items():
        print(key,value)
    
mark_list={"bilal":100 ,"ali":20,'xyx':30}    
       
printmarks(**mark_list)
