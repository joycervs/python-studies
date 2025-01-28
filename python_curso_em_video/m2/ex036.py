valorCasa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o salário do comprador? R$'))
anos = int(input('Quantos anos de financiamento? '))

prestacao = valorCasa / (anos * 12)
minimo = salario * 0.30

print(f'\nPara pagar uma casa de R${valorCasa:.2f} em {anos} anos a prestação será de R$ {prestacao:.2f}')

if prestacao <= minimo:
  print('\nEmpréstimo APROVADO')
else:
  print('\nEmpréstimo NÃO APROVADO')