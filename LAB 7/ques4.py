import numpy as np 

a=np.array([['Python', 'NumPy', 'Exercises'], 
            ['Python' ,'Pandas' ,'Exercises'],
            ['Python', 'Machine learning', 'Python']])

c=np.char.count(a,'Python')

print(c)
