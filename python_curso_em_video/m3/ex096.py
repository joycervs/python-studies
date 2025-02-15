def calculo_area(largura, comprimento):
  cal = largura * comprimento
  print(f'A área de um terreno {largura:.1f}x{comprimento:.1f} é de {cal:.1f}m²')


print('Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
calculo_area(l,c)