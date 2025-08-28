# não preciso criar uma variável para cada número
numeros = [10, 20,30, 17]
carros = ['Pálio', 'Gol', 'Virtus', 'Ká', 'Onix']

numeros.sort(reverse=True) # Ordena invertido
print(numeros)
# Saída: [9, 8, 5, 2, 1]

# igual JavaScript
print(numeros)
print(numeros[1])

print(len(carros))
carros.append('Kombi') # adicionar no final
carros.insert(1, 'Uno')  # Adiciona 'Uno' na posição 1
carros.remove('Gol')
carros.pop(1)  # Remove o item na posição 1 ('Uno')

outros_carros = ['Voyage', 'Celta']
carros.extend(outros_carros)
print(carros)
# Saída: ['Gol', 'Corsa', 'Uno', 'Kombi']

del carros[3]
print(carros)

carros = sorted(carros) # ordenou na mesma variável
print(carros)

print()
print('Fazendo um for de carros:')
for i in range(0,len(carros)):
  print(carros[i])

print()
print('Fazendo um for de carros:')
for carro in carros:
  print(carro)