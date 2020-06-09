num = input().split()

a = int(num[0])
b = int(num[1])
c = int(num[2])

maior_ab = (a+b + abs(a-b))/2

maior = int((maior_ab + c + abs(maior_ab-c))/2)

print('{} eh o maior'.format(maior))
