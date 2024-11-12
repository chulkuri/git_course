n=int(input("enter any number greater than 2: "))
count=0
for i in range(2,n):
    if n%i==0:
        count+=1
        break
if count>0:
    print("the given number is not prime")
else:
    print("the given number is prime")
