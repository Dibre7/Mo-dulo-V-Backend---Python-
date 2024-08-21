# Faça um programa em que o usuário precisa cadastrar nome, idade, telefone e e-mail. 
# Depois mostre os valores digitados na tela. 

# Recebendo os dados
nome = input("Digite o seu nome inteiro: ")
idade = int(input("Digite a sua idade: "))
telefone = input("Digite o seu telefone: ")
email = input("Digite o seu e-mail: ")

#Mostrando os dados
print(f"Dados cadastrados:\n Nome:{nome}\n Idade:{idade}\n Telefone:{telefone}\n E-mail:{email}")
