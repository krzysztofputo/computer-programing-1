array = [6,8,3,1,0,5,7]
def a(x):
    num = 0
    for i in range(len(array)):
        if array[i] > x:
            num += 1
    print(num)
a(int(input()))
            