n = int(input())


cem = int(n/100)
cinq = int(n%100/50)
vint = int(n%100%50/20)
dez = int(n%100%50%20/10)
cinc = int(n%100%50%20%10/5)
dois = int(n%100%50%20%10%5/2)
um = int(n%100%50%20%10%5%2)

print(n)
print('{} nota(s) de R$ 100,00'.format(cem))
print('{} nota(s) de R$ 50,00'.format(cinq))
print('{} nota(s) de R$ 20,00'.format(vint))
print('{} nota(s) de R$ 10,00'.format(dez))
print('{} nota(s) de R$ 5,00'.format(cinc))
print('{} nota(s) de R$ 2,00'.format(dois))
print('{} nota(s) de R$ 1,00'.format(um))


