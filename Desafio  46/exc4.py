# Implemente uma função chamada calcular_fatorial que recebe um número
#  inteiro positivo como parâmetro e retorna o fatorial desse número.

def calcular_fatorial(n):
    resultado = 1
    for i in range (1, n + 1):
        resultado *= i 
        # Equivale a resultado = resultado * i
    return resultado



resultado = calcular_fatorial(5)
print(resultado)  # Saída: 120

