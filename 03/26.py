pin="0805"

for i in range(1,4):
    guess = input("Enter the PIN code: ")
    if guess!=pin:
        print("Incorrect...")
        if i==3:
            print("Sorry, your payment card has been blocked.")    
    else:
        print("Welcome!")        
    