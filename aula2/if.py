n1 = 5
n2 = 6
n3 = 7
n4 = 8

soma = n1+n2+n3+n4
media = soma/4

print('IF 1')
if media >=7:
  print('Aprovado')
  print('esse print dentro do IF') # segue indentação
else:
  if media <= 5:
    print('Reprovado')
  else:
    print('Recuperação')

print('IF 2')
if media >=7: print('Aprovado')
elif media < 5: print('reprovado')
else: print('recuperação')

print('IF 3')
if media >=7: 
  print('Aprovado')
elif media < 5: 
  print('reprovado')
else: 
  print('recuperação')