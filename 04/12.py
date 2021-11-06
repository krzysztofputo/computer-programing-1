def sum(n):
    if n==1:
        return 1
    if n>1:
        return n+sum(n-1)

n=10
print(f"sum of {n} natural numbers is {sum(n)}")
