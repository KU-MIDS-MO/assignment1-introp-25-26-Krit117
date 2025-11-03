#%%
def count_digits_greater_than(n, t):
    if not isinstance (t,int) or not isinstance (n,int) or n<0  or t<0 or t>9:
        return -1
    count=0
    for i in str(n):
        if int(i)>t:
           count= count + 1
    return count
    
           
        
    