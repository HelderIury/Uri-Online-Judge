dias = int(input())

ano = int(dias/365)
mes = int(dias%365/30)
dia = int(dias%365%30)

print('{} ano(s)'.format(ano))
print('{} mes(es)'.format(mes))
print('{} dia(s)'.format(dia))