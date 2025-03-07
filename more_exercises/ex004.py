#Calculo IMC
altura = float(input('Digite a sua altura (cm): '))
peso = float(input('Digite o seu peso (kg): '))

imc = peso / altura **2

if imc < 18.5:
  resultado = 'MAGREZA'
elif imc >= 18.5 and imc < 24.9:
  resultado = 'NORMAL'
elif imc >= 25.0 and imc < 29.9:
  resultado = 'SOBREPESO'
elif imc >= 30.0 and imc < 39.9:
  resultado = 'OBESIDADE'
else:
  resultado = 'OBESIDADE GRAVE'

print(f'Seu IMC é {imc} ==> {resultado}')