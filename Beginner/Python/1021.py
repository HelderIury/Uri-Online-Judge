n = float(input())
decimal = n - int(n)
decimal_int = int(decimal*100)


#NOTAS:
cem = int(n/100)
cinq = int(n%100/50)
vint = int(n%100%50/20)
dez = int(n%100%50%20/10)
cinc = int(n%100%50%20%10/5)
dois = int(n%100%50%20%10%5/2)
um = int(n%100%50%20%10%5%2)

#MOEDAS:
cinqcent = int(decimal_int%100/50)
vintcent = int(decimal_int%100%50/25)
dezcent = int(decimal_int%100%50%25/10)
cincent = int(decimal_int%100%50%25%10/5)
umcent = int(decimal_int%100%50%25%10%5)

print('NOTAS:')

print('{} nota(s) de R$ 100.00'.format(cem))
print('{} nota(s) de R$ 50.00'.format(cinq))
print('{} nota(s) de R$ 20.00'.format(vint))
print('{} nota(s) de R$ 10.00'.format(dez))
print('{} nota(s) de R$ 5.00'.format(cinc))
print('{} nota(s) de R$ 2.00'.format(dois))

print('MOEDAS:')

print('{} moeda(s) de R$ 1.00'.format(um))
print('{} moeda(s) de R$ 0.50'.format(cinqcent))
print('{} moeda(s) de R$ 0.25'.format(vintcent))
print('{} moeda(s) de R$ 0.10'.format(dezcent))
print('{} moeda(s) de R$ 0.05'.format(cincent))
print('{} moeda(s) de R$ 0.01'.format(umcent))






