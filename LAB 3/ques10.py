def conversion(b,n):
    tempn = n
    rem = []
    while n:
        rem.append(n % b)
        n //= b
    rem.reverse()
    num = ''.join(map(str, rem))
    print(f"({tempn})10 = ({num}){b}")

b = int(input("Enter base: "))
n = int(input(f"Enter number in decimal: "))
conversion(b,n)
