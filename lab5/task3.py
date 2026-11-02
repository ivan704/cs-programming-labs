n = int(input())
below_zero = 0
eq_zero = 0
above_zero = 0
for i in range(n):
    temp = float(input())
    if temp==0:
        eq_zero += 1
    elif temp<0:
        below_zero += 1
    else: above_zero += 1
print(f'Ниже нуля: {below_zero}')
print(f'Равны нулю: {eq_zero}')
print(f'Выше нуля: {above_zero}')
