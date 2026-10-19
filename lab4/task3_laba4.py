X = float(input())
Y = float(input())
if X == 0 and Y ==0:
    print('Начало координат')
elif X == 0:
    print('Ось Y')
elif Y == 0:
    print('Ось X')
elif X>0 and Y>0:
    print('I четверть')
elif X<0 and Y>0:
    print('II четверть')
elif X<0 and Y<0:
    print('III четверть')
else: print('IV четверть')
