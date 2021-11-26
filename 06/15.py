a = ['blue', 'red', 'yellow']
with open('a.txt', 'w') as file:
    for i in a:
        file.write(i)
        file.write("\n")
