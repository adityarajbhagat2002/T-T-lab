def func(num):
    
    sum=0
    n=0
    a=num
    while  num!=0:
        n=num%10
        sum=sum+n 
        num=num/10
    print("the sum of digits of a ", a, " is" , int(sum))

num = int(input("enter a number :"))
func(num)

