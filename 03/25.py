a = int(input("a: "))
b = int(input("b: "))

for i in range(a):
    for j in range(b):
        if i==0 or i==(a-1) or j==0 or j==(b-1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()