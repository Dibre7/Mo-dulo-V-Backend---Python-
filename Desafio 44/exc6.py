# Faça um programa em que o usuário digita um número inteiro 
# e o programa exibe todos os números ímpares do 1 até o valor inserido.

valor = int(input("Digite um valor inteiro que você queira ver todos os número ímpares até ele: "))

for i in range(1, valor+1, 2):
    print(i)