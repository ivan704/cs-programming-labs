n = int(input())

odd_count = 0
for i in range(n):
    C = 1
    for j in range(i + 1): 
        if j > 0:
            C = C * (i - j + 1) // j   
        print(C, end='')
        if j < i:
            print(' ', end='')
        if C % 2 == 1:
            odd_count += 1
    print()
print(f"Нечетных элементов: {odd_count}")