distanse = float(input())
fuel_km = float(input())
price = float(input())

fuel_lost = (distanse/100)*fuel_km
fuel_price = price*fuel_lost

print(f'Топливо: {fuel_lost:.2f} л')
print(f'Стоимость: {fuel_price:.2f} руб')
