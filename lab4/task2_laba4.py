price = float(input())
ago = int(input())

if 0<=ago<=5:
    print(f'Стоимость: {(price*0):.2f} руб')
elif 6<=ago<=17:
    print(f'Стоимость: {(price/2):.2f} руб')
elif 18<=ago<=59:
     print(f'Стоимость: {(price):.2f} руб')
elif 60<=ago<=120:
     print(f'Стоимость: {(float(price)*0.7):.2f} руб')
else: print('Ошибка')