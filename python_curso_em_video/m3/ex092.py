from datetime import datetime
dados = {}

dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 se não tiver): '))

if dados['ctps'] != 0:
  dados['contratacao'] = int(input('Ano de contratação: '))
  dados['salario'] = float(input('Salário: R$'))
  dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)

print('-='*30)

for k, v in dados.items():
  print(f'- {k} tem o valor {v}')