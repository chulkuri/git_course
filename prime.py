n=int(input("enter any integer"))
for i in range(2,n):
    if n%i==0:
        print("given number is not prime")
    else:
        print("given number is prime")