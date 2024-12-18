#Descobrir o sucessor e antecessor do número digitado:

n = int(input('Digite um número: '));
sucessor = n + 1;
antecessor = n - 1;
print('O sucessor de {} é {} e o antecessor é {}'.format(n, sucessor, antecessor));


# Outra forma de fazer:
# n = int(input('Digite um número: '));
# print('O sucessor de {} é {} e o antecessor é {}'.format(n, (n+1), (n-1)));