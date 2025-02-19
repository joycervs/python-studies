def manual(cmd):
   help(cmd)

def titulo(msg):
    tam = len(msg) + 4
    print('=' * tam)
    print(f'  {msg}')
    print('=' * tam)

comando = ''

while True:
  titulo('SISTEMA DE AJUDA PyHelp')
  comando = str(input('Função ou Biblioteca > ')).strip()
  if comando.upper() == 'FIM':
    break
  else:
    manual(comando)
titulo('ATÉ LOGO!')
