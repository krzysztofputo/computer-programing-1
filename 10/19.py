class Nums():
    
    def __init__(self, numbers):
        self.numbers= numbers
        
    def greatest(self):
        max = self.numbers[0]
        for i in self.numbers:
            if int(i) > int(max):
                max = i
        print(max)
    def smallest(self):
        min = self.numbers[0]
        for i in self.numbers:
            if int(i) < int(min):
                min = i
        print(min)

    def median(self):
        self.numbers.sort()
        l = len(self.numbers)
        
        if l%2==0:
            median1 = self.numbers[l//2]
            median2 = self.numbers[l//2 - 1]
            median = (int(median1) + int(median2))/2
        else:
           median = self.numbers[l//2]
        print(f"median is {median}")
            

    def mean(self):
        i=0
        suma=0
        for n in self.numbers:
            i+=1
            suma+=int(n)
        res = suma/i
        print(res)
        
x = input("Napisz liczby po spacji: ")
n = x.split(' ')
nums = Nums(n)
nums.median()
print(nums.numbers)
nums.greatest()
nums.smallest()
nums.mean()