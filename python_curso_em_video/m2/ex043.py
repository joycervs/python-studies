peso = float(input('Digite o seu peso (Kg): '))
altura = float(input('Digite sua altura (m): '))
imc = peso / (altura ** 2)

print(f'O IMC dessa pessoa é de {imc:.1f}')

if imc < 18.5:
  print('Você está ABAIXO do peso ideal.')
elif imc >= 18.5 and imc < 25:
  print('Você está no peso ideal.')
elif imc > 25 and imc <= 30:
  print('Você está em SOBREPESO')
elif imc > 30 and imc <= 40:
  print('Você está em OBESIDADE, cuidado!')
else : #imc >= 40
  print('Você está em OBESIDADE MÓRBIDA, cuidado!')

