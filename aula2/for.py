i = 0
n1 = 2

#já incrementa de 1 em 1
for i in range(1,11): 
  # print('2 x', i,'=', n1*i)
  # print('2 x {} = {}'.format(i,n1*i))
  print(f'2 x {i} = {n1*i}')

#        range(start, stop, step)
for j in range(1,11,2):
  print(f'2x{j}= {n1*j}')

# A contagem começa em 10, vai até 0 (exclusivo) e o passo é -1
for k in range(10, 0, -1):
  print(k)