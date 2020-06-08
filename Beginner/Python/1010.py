peca1 = input().split()
codigo1 = peca1[0]
numero1 = int(peca1[1])
valor1 = float(peca1[2])

peca2 = input().split()
codigo2 = peca2[0]
numero2 = int(peca2[1])
valor2 = float(peca2[2])

total = float((numero1*valor1) + (numero2*valor2))

print('VALOR A PAGAR: R$ {:.2f}'.format(total))

