#%%
def is_strictly_increasing_digits(n):
    if n<0 or not isinstance(n,int):
        return -1
    if 0<= n <=9:
        return True
    while n>9:
        last_digit= n % 10 
        n= n//10
        digit = n % 10 
        if digit >=last_digit :
            return False
        last_digit = digit
    return True
            
        
              
        
            
            
            
            

     
