num = 1
q = 0
suma = 0
mean = 0
while num!=0:
    num = int(input("Enter number: "))
    if num == 0:
        break
    q+=1
    suma += num
mean = suma/q
print(f"RESULT: Quantity={q}, Sum={suma}, Mean={mean}")