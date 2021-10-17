
def alphabet(value):
    count_upper = 0
    count_lower = 0    
    for i in value:
        if i.isupper() == True:
            count_upper += 1
        elif i.islower() == True:
            count_lower +=1 
    print('No of upper case charecter :',count_upper)                
    print('No of lower case charecter :',count_lower)
    
str = 'The quick Brow Fox'
result = alphabet(str)
print(result) 
