a=int(input("enter the first number : "))
b=int(input("enter the second number :"))

if a>b:
    smaller=b
else :
    smaller= a

for i in range(1,smaller+1):
    if((a%i==0 and b%i ==0)):
        hcf=i


print("H.C.F of the number is ", int(hcf))

