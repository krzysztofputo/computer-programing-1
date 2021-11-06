from datetime import datetime

month = int(input("Type a number 1-12: "))
if month >=1 and month <=12:
    x = datetime(2021, month, 1)
    print(x.strftime("%B"))
