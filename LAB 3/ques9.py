def pattern_range(n):
    for i in range(1, n + 1):
        if i & 1 == 0:
            num = i
            for j in range(1, i + 1):
                print(num, end=' ')
                num -= 1
        else:
            num = 1
            for j in range(1, i + 1):
                print(num, end=' ')
                num += 1
        print('')
    
n = int(input("Enter n: "))
pattern_range(n)
