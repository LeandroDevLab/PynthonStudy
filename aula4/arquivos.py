# lidar com arquivos

# w -> (Write) apaga tudo e sobreescreve
# a+ -> (append) adiciona
# r -> (Read)
arquivo = open('pessoas.txt', 'a+')
arquivo.write('Leandro\n')
arquivo.write('Oliota\n')

#fechando o arquivo
arquivo.close()

# abre, evita esquecer o fechamento e já faz o tratamento
with open('pessoas.txt', 'r+') as arquivoLeitura:
  for linha in arquivoLeitura:
    print(linha)