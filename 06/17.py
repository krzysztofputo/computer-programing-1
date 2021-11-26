a = [4,36,12,28,9,44,5]
b = [5,1,36]

for i in range(len(a)):
    if a[i] != b[0] and a[i] != b[1] and a[i] != b[2]:
        x = True
    else:
        x = False
    if x == True:
        print(a[i])