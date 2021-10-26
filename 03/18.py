amount = int(input("Enter the amount in PLN: "))
zl5 = amount//5
reszta = amount%5
zl2 = reszta//2
reszta = reszta%2
zl1 = reszta//1

print(f"The amount of PLN {amount} in coins:\n5 zł - {zl5}\n2 zł - {zl2}\n1 zł - {zl1}")
