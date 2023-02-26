def pattern_range(n):
    for i in range(1, n + 1):
        num = chr(ord('A') + i - 1)
        for j in range(1, i + 1):
            print(f'{num}', end=' ')
            num = chr(ord(num) - 1)
        print('')
    
n = int(input("Enter n: "))
pattern_range(n)