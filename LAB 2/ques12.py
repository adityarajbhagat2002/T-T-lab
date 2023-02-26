# WAP to print the series as 1 2 7 15 31 ........, where n is given by user.
n = int(input("Enter n: "))
print("n terms of the series: ", end='')
for num in range(n):
    print(f"{2 ** num}", end=' ')
