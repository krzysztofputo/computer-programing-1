def bubblesort(x):
    for i in range(len(x)):
        for j in range(0, len(x) - i - 1):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
    return x
a = [1,6,4,8,3,3,6,4,5,7]
print(bubblesort(a))