time_all = int(input())
hour = time_all//3600
min = (time_all%360)//60
sec = time_all%60
print(f'{hour:02d}:{min:02d}:{sec:02d}')
