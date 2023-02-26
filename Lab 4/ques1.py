#WAP to print the odd and even numbers upto a given range


num= int(input("enter the number :"))

listODD=[]
listEVEN=[]

for i in range(1,num+1):
    if i%2==0:
        listEVEN.append(i)
    else:
        listODD.append(i) 

print("odd numebers : " ,listODD)
print("even number : " , listEVEN)



