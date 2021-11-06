import mymath

y = mymath.generate_number()
print("Enter one digit number:")
x = int(mymath.read_number())
if x == y:
    print("You won!")
else:
    print("You lost!")
