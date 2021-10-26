cm = float(input("Enter your height in cm: "))
kg = float(input("Enter your weight in kg: "))
bmi = round(kg/cm**2*10000, 2)
if bmi>18.5 and bmi<25:
    print(f"BMI: {bmi} Normal")
elif bmi>25:
    print(f"BMI: {bmi} You weight too much")
else:
    print(f"BMI: {bmi} You weight too low")
