# Faça um programa que calcule a área de um quadrado/retângulo.

# Função Calculando
def calcular_area_quadrado(largura, altura):
    area = largura * altura
    return area


# Pegando medidas do quadrado/retângulo
largura = int(input("Digite a medida da largura em m²:"))
altura = int(input("Digite a medida da altura em m²:"))

# Chamando a função e mostrando
area = calcular_area_quadrado(largura, altura)
print(f"A área do retângulo de largura {largura} e altura {altura} é {area}")