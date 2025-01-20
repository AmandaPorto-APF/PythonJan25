# #####Faça um programa que verifique se a pessoa pertence à família “calvo”.

# familia = (input('Qual sua o nome da sua familia? ')).lower()


# if familia == 'calvo':
#     print(f'Esta e a sua familia!')
    
# else:
#     print(f'Voce esta na familia errada.')


# #####Faça um programa que verifique se a pessoa pertence à família “calvo” ou “silva”.

# familia = input('Qual sua o nome da sua familia? ').lower()


# if familia == 'calvo' or familia == 'silva':
#     print(f'Esta e a sua familia!')

# else:
#     print(f'Voce esta na familia errada.')


# #####Faça um programa que verifique se o item que a pessoa escolheu para comprar na loja está na lista: 
#   laranja, cerveja, miojo, carvão, picanha.

# produtos = ['laranja', 'cerveja', 'miojo', 'carvao', 'picanha']

# compra = input('Qual produto voce comprou? ').upper()

# if compra in produtos: 
#     print(f'Muito bem! voce comprou o item {compra}, que esta na lista!')

# else:
#     print(f'Sinto muito! O item {compra} nao esta na lista.')


# #####Faça um programa que conte quantas vezes a letra “a” aparece em uma palavra

# palavra = input(f'Digite uma palavra: ').lower()

# print(f'Na palavra {palavra}, a letra "A" aparece {palavra.count('a')} vezes')


# ####Faça um programa que vende uma garrafa de água:
# Se o cliente escolher água mineral natural, será cobrado R$1,50
# Se o cliente escolher água mineral com gás, será cobrado R$2,50
# Altere o programa anterior para considerar a quantidade de água

# escolha = input('Voce gostaria de uma garrafa de agua mineral ou com gas? [mineral/gas]: ').lower()
# escolha_qty = int(input('Quantas garrafas voce deseja? ')) 

# preco_gas = 2.5
# preco_mineral = 1.5


# if escolha == 'mineral':
#     valor_total1 = escolha_qty * preco_mineral
#     print(f'O valor da sua compra e R${valor_total1}')
# elif escolha == 'gas':
#     valor_total2 = escolha_qty * preco_gas
#     print(f'O valor da sua compra e R${valor_total2}.')
# else:
#     print('Faca uma escolha valida!')



# ####Faça o programa de uma sorveteria, onde o usuário pode escolher:
# Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
# Sabor do sorvete: morango, creme, chocolate
# Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)
# Apresente o valor a ser pago

pedido_tipo = input('Qual tipo de sorvete voce gostaria? \n Casquinha (R$1,00) \n Cascão (R$2,50) \n Cestinha (R$4,00)\n').lower()
pedido_sabor = input('Qual a cobertura voce deseja? [morango, creme ou chocolate] ').lower()
pedido_cobertura = input('Voce deseja adicionar combertura? \n Caramelo (R$1,50) \n morango (R$1,50) \n chocolate (R$1,50) \n sem cobertura (R$0,00) ').lower()


if pedido_tipo == 'casquinha' and pedido_cobertura == 'caramelo' or pedido_cobertura == 'morango' or pedido_cobertura == 'chocolate':
    print(f'O valor da {pedido_tipo}, com sorvete sabor {pedido_sabor} e cobertura de {pedido_cobertura} e de R${1.00+1.50}')

elif pedido_tipo == 'cascao' and pedido_cobertura == 'caramelo' or pedido_cobertura == 'morango' or pedido_cobertura == 'chocolate':
    print(f'O valor da {pedido_tipo}, com sorvete sabor {pedido_sabor} e cobertura de {pedido_cobertura} e de R${2.50+1.50}')

elif pedido_tipo == 'cestinha' and pedido_cobertura == 'caramelo' or pedido_cobertura == 'morango' or pedido_cobertura == 'chocolate':
    print(f'O valor da {pedido_tipo}, com sorvete sabor {pedido_sabor} e cobertura de {pedido_cobertura} e de R${4.00+1.50}')

elif pedido_tipo == 'cascao' and pedido_cobertura == 'sem cobertura': 
    print(f'O valor da {pedido_tipo}, com sorvete sabor {pedido_sabor} e sem cobertura de R$1.00')
elif pedido_tipo == 'casquinha' and pedido_cobertura == 'sem cobertura': 
    print(f'O valor da {pedido_tipo}, com sorvete sabor {pedido_sabor} e sem cobertura de R$2.50')
elif pedido_tipo == 'cestinha'and pedido_cobertura == 'sem cobertura': 
    print(f'O valor da {pedido_tipo}, com sorvete sabor {pedido_sabor} e sem cobertura de R$4.00')




# Faça um programa que receba 4 alturas, armazene em uma lista e depois mostre a soma dessas alturas.
# Faça um programa que receba uma quantidade indefinida de valores correspondentes a “saldo em conta”, 
#   mas quando o usuário apertar “enter” sem digitar valor algum, o programa para de receber valores, 
#   e exibe a soma te todos os valores digitados anteriormente.