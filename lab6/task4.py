n = int(input())

if n < 0:
    print("Ошибка")
else:
    if n == 0:
        count = 1
        total = 0
    else:
        count = 0
        total = 0
        while n > 0:
            digit = n % 10
            total += digit
            count += 1
            n //= 10
    
    print(f"Цифр: {count}")
    print(f"Сумма цифр: {total}")

    