import json

pessoas = [
  {'nome': 'Leandro', 'telefone': '09834-3453', 'endereço': 'ABC'},
  {'nome': 'Maria', 'telefone': '1234-3553', 'endereço': 'KJH'},
  {'nome': 'João', 'telefone': '4567-4563', 'endereço': 'JUS'}
]

# json.dump -> escrever um objeto Python (como um dicionário ou uma lista) em um arquivo
with open('pessoas.json', 'w') as arquivo:
  json.dump(pessoas, arquivo, indent=2)


# json.load() -> lê o arquivo e converte de volta para objeto em python
'''
# Abre o arquivo para leitura ('r')
with open('dados.json', 'r') as arquivo_json:
    # Converte o conteúdo do arquivo para um objeto Python
    dados_lidos = json.load(arquivo_json)
'''