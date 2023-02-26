set1 = set(map(int, input('Enter elements in first set: ').split())) 
set2 = set(map(int, input('Enter elements in first set: ').split())) 
ans = set([]) 
for i in set1: 
    ans.add(i) 
for i in set2: 
    ans.add(i) 
print(f'Union of {set1} and {set2} => {ans}')