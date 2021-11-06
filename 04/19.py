def is_in_range(n):
    x = 1
    y = 100
    if x <= n <= y:
        return True
    else:
        return False
    

n = int(input("Type a number: "))
print(is_in_range(n))
