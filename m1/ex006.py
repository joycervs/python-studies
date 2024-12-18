# Dobro, triplo e raiz quadrada de um número

n = int(input('Digite um número: '));
dobro = n * 2;
triplo = n * 3;
raiz = n ** (1/2);
print('O dobro de {} é {}. \nO triplo é {}. \nA raiz quadrada é igual a {:.2f}'.format(n, dobro, triplo, raiz));


# Forma mais resumida:
# n = int(input('Digite um número: '));
# print('O dobro de {} é {}.\nO triplo é {}.\nA raiz quadrada é igual a {:.2f}'.format(n, (n*2), (n*3), (n**(1/2))));

# n**(1/2) ou pow(n,(1,2))