import math
number=int(input("number:"))
for i in range(2,int(math.sqrt(number))):
    if number%2==0:
        print("not prime")
        break
else:
    print("prime")
