# Escreva uma função chamada reverter_string que recebe uma string como parâmetro
#  e retorna a string ao contrário.

def reverter_string(texto):
    invertida = texto[::-1]
    return invertida

resultado = reverter_string("Python")
print(resultado)  # Saída: "nohtyP"
