n = int(input("Enter n: "))
print("n terms of the series: ", end='')
for num in range(n):
    print(f"{2 ** num}", end=' ')
