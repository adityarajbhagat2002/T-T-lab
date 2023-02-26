def func(num):
    r=0
    s=0
    while num !=0:
        n=num%10
        r=r*10+n
        num //=10
    
    print("the reverse of a number is : ", int(r))

num = int(input("enter a number :"))
func(num)