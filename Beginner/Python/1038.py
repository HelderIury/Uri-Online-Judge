num = input().split()

codigo = int(num[0])
qntd = int(num[1])

if (codigo == 1):
    total = float(4.00*qntd)
    print('Total: R$ {:.2f}'.format(total))

elif (codigo == 2):
    total = float(4.50*qntd)
    print('Total: R$ {:.2f}'.format(total))


elif (codigo == 3):
    total = float(5.00*qntd)
    print('Total: R$ {:.2f}'.format(total))


elif (codigo == 4):
    total = float(2.00*qntd)
    print('Total: R$ {:.2f}'.format(total))


elif (codigo == 5):
    total = float(1.50*qntd)
    print('Total: R$ {:.2f}'.format(total))




