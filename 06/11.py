def compare(array1, array2):
    if len(array1) == len(array2):
        for i in range(len(array1)):
            if not array1[i] == array2[i]:
                return False
        return True
    else:
        return False
    
array1 = [1,3]
array2 = [1,2,3]

print(compare(array1, array2))