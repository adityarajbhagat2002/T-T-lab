import numpy as np 
a=np.array(['python ' ,'php'], dtype= np.str_)
b=np.array(['java' , ' c++'],dtype= np.str_)

print("First array : ")
print(a)

print("Second array : ")
print(b)

newArray=np.char.add(a,b)

print("New Array : ")
print(newArray)

