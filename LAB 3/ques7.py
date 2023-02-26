def pattern_range(n):
    for i in range(1, n + 1):
        num = 1
        if i & 1:
            num = 1
        else:
            num = 0
        for j in range(1, i + 1):
            print(num, end=' ')
            num += 1
            num %= 2
        print('')
        
n=int(input("Enter a number:"))
pattern_range(n)