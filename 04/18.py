def sum_of_digits(n):
    sum = 0
    for i in n:
        sum += int(i)
    return sum
        
print(sum_of_digits("7182"))
