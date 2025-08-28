i = 0
n1 = 2
continuar = True

while continuar:
  n = int(input('Qual tabuada: '))

  for i in range(1,11): 
    print(f'{n} x {i} = {n*i}')
      
  continuar = input('Deseja continuar (s/n)')
  continuar = True if continuar == 's' else False
  
  '''
  if continuar == 's':
    continuar = True
  elif continuar =='S':
    continuar = True
  else:
    continuar = False  
  '''


'''
  while i < 11:
  # print('2 x', i,'=', n1*i)
  # print('2 x {} = {}'.format(i,n1*i))
  print(f'2 x {i} = {n1*i}')
  i = i+2

  continuar = input('Deseja continuar (s/n)')
  continuar = True if continuar == 's' or 'S' else False
'''

