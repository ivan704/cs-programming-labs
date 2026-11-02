a = int(input())
b = int(input())
summ = 0
mult = 1
if a<=b:
    for namb in range(a,b+1):
        summ += namb
        mult =  mult*namb
print(f'Сумма: {summ}')
print(f'Произведение {mult}')