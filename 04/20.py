def power(x, n):
    res = 0
    if n > 0:
        res += x*power(x,n-1)
    if n == 0:
        return 1
    return res
    
print(power(5, 3))
