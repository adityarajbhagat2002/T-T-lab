# WAP TO REMOVE ALL THE MULTIPLES OF 2 IN A LIST

lst=[]
num= int(input("enter the  size of list :"))
for i in range(1,num+1):
    n=int(input("enter the elements in the list :"))
    lst.append(n)

for ele in lst:
    if ele % 2==0:
        lst.remove(ele)

print(" new list after removing all the multiple of two ", lst)


