#WAP to reverse a List

n=int(input("enter the size :"))

oldlist=[]

for i in range(1,n+1):
    print("enter the elemts to inserted in the list")
    num=input()
    oldlist.append(num)

print("elements before reversing a list : " , oldlist ) 

oldlist.reverse()

print("elemets after reversing the list ",oldlist)

