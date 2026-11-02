namb = 0
k = 0
while True:
    n = input()
    if n != "stop":
        k += 1
        namb += int(n)
        mean_value = namb/k
    else: break
print(f'Покупок: {k}')
print(f'Общая стоимость: {namb} руб')
print(f'Средняя стоимость: {mean_value:.2f} руб')