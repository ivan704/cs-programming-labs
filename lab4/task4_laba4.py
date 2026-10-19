len_a = int(input())
len_b = int(input())
len_c = int(input())

if (len_a<=0 or len_b<=0 or len_b<=0) or ((len_a+len_b)<=len_c or (len_b+len_c)<=len_a or (len_c+len_a)<=len_b):
    print('Треугольник не существует')
elif len_a == len_b == len_c:
    print('Равносторонний')
elif len_a == len_b or len_a == len_c or len_b==len_c:
    print('Равнобедренный')
else: print('Разносторонний')