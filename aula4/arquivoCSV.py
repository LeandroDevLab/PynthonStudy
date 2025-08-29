import csv

carros = [
  ['VW', 'Virtus', '2017'],
  ['VW', 'Gol', '1999'],
  ['Fiat', 'Pálio', '2002'],
]

# para o LibreOffice não precisou do newline e do delimiter
with open('carros.csv', 'w', newline='') as arquivo:
  fileCSV = csv.writer(arquivo, delimiter=';')

  fileCSV.writerow(['Marca', 'Modelo', 'Ano'])
  fileCSV.writerows(carros)