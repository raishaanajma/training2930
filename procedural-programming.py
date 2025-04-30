mylist = [1, 2, 3] 
  
# modularization is done by  
# functional approach 
def sum_the_list(mylist): 
    res = 0
    for val in mylist: 
        res += val 
    return res 
  
print(sum_the_list(mylist)) 