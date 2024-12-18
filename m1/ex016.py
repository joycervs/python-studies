from math import trunc

real = float(input("Digite um valor: "))
inteiro = trunc(real)
print("O número {} tem a parte inteira {}".format(real, inteiro))

# Outra forma de fazer:
# real = float(input("Digite um valor: "))
# print("O número {} tem a parte inteira {}".format(real, int(inteiro)))