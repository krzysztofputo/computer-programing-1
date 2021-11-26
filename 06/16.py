a = [12,6,4,9,3]
def star(x):
    print(f'{x}: ', end='')
    for i in range(x):
        print('*', end='')
    print()
        
for i in range(len(a)):
    star(a[i])