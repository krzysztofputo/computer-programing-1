n = int(input("Type number: "))
x=0
if n>1:
    for i in range(1,n+1):
        if n%i==0:
            x+=1
    if x==2:
        print(f"{n} is Prime number")
