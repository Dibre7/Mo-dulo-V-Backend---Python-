# Faça um programa no qual o usuário precisa cadastrar as informações de um produto: 
# código, nome, quantidade e preço. 
# No final o programa deve mostrar as informações cadastradas e exibir o valor total da compra. 


# Informações do produto
print("Preencha as informções do produto:")
cod = input("Código do produto:")
nome = input("Nome do produto:")
quant = int(input("Quantidade:"))
preco = float(input("Preço:"))

# Mostrando as informações e valor final
valorf = quant * preco
print(f"O produto {nome}, código: {cod}, de valor {preco} foi pego em {quant} unidades\n 
      Terá um preço total de {valorf}")