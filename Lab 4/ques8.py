# WAP TO FIND A DIFFERENCE BETWEEN MAX AND MIN IN A SET

set1 = set(map(int, input('Enter elements of set: ').split())) 
print(f'Difference between max and min element = {list(set1)[-1] - list(set1)[0]}')

