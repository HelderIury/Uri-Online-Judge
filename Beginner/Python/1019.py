n = int(input())

horas = int(n/3600)
minut = int(n/60)%60
seg = int(n%60)
print('{}:{}:{}'.format(horas,minut,seg))



