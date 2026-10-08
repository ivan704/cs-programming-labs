code = input()

cut_1 = code[:3]
cut_2 = code[4:8]
cut_3 = code[9:13]
cut_4 = cut_3[::-1]

print(f'Категория: {cut_1}')
print(f'Год: {cut_2}')
print(f'Номер: {cut_3}')
print(f'Обратный номер: {cut_4}')
