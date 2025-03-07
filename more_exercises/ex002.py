# Calcula quantidade necessária de latas de tinta
rend = int(input('Qual o rendimento da lata? '))
altura = int(input('Qual a altura da parede? '))
largura = int(input('Qual a largura da parede? '))

def calcula_tinta():
  area = altura * largura
  total = area / rend
  print(f'Você precisa de {total} latas de tinta')

calcula_tinta()