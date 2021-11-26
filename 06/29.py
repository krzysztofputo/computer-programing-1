def a(x, y):
    z = False
    for d in x:
        if d in y:
            z = True
        else:
            z = False
            break
    return z
array1 = [1, 2, 3]
array2 = [3, 2, 1, 4]
print(a(array1, array2))
 