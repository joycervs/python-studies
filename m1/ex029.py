velocidade = float(input('Qual é a velocidade atual do carro? '))

if velocidade > 80:
  multa = (velocidade - 80) * 7.00
  print('\033[1;31mMULTADO! Você excedeu o limite permitido que é de 80Km/h')
  print(f'Você vai pagar uma multa de R${multa:.2f}\033[m')
print('Tenha um bom dia! Dirija com segurança!')