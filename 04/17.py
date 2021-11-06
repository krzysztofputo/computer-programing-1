word = "You never get a second chance to make first impression"
letter = input("Type letter: ")

counter=0

for i in word:
    if i == letter:
        counter+=1
print(counter)
