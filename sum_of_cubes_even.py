#%%
def sum_of_cubes_even(n):
    if n <0 or type (n) != int:
        return -1
    if n> 2000:
        print ("Warning")
    agregate= 0
    for x in range(0, n+1, 2):
      agregate += x**3
      print (agregate)
    return float(agregate)