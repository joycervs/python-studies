from time import sleep
opcao = 0
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
while opcao != 5:
  print('''
          [ 1 ] somar
          [ 2 ] multiplicar
          [ 3 ] maior
          [ 4 ] novos números
          [ 5 ] sair do programa
          ''')
  opcao = int(input('>>>>> Qual é a sua opção? '))
  
  if opcao == 1:
    soma = n1 + n2
    print(f'A soma entre {n1} e {n2} é {soma}')
  elif opcao == 2:
    produto = n1 * n2
    print(f'A multiplicação entre {n1} e {n2} é {produto}')
  elif opcao == 3:
    if n1 > n2:
      maior = n1
    else:
      maior = n2
    print(f'Entre {n1} e {n2} o maior é {maior}')
  elif opcao == 4:
    print('Informe os números novamente:')
    n1 = int(input('Primeiro valor: '))
    n2 = int(input('Segundo valor: '))
  elif opcao == 5:
    print('Finalizando...')
  else:
    print('Opção inválida. Tente novamente')
  print('-=-' * 10)
  sleep(2)
print('Fim do programa. Volte sempre!')