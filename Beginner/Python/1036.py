num = input().split()

a = float(num[0])
b = float(num[1])
c = float(num[2])

delta = (b**2) - (4*a*c)

if (delta >= 0) and (a>0):
    x1 = (-b + (delta**0.5))/(2.0*a)
    x2 = (-b - (delta**0.5))/(2.0*a)

    print("R1 = {:.5f}".format(x1))
    print('R2 = {:.5f}'.format(x2))

else:
    print('Impossivel calcular')
    
