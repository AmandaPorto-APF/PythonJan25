# idade = int(input('Qual a sua idade? '))
# cnh = input('Voce tem CNH? ')

##Teo resolution
# if idade >= 18 and cnh == 'sim':
#     print('Siga em frente')

# else:
#     print('Preso em nome da lei!')

#minhas melhorias:
#resposta da cnh sim/nao - input s/n
#entender sim Sim/ etc - upper/lowe
#categorias de carteira - qual categoria? vc pode dirigir X
#Menagem para quem e menor de 18 e nao tem carteira - idade <18 and chn == nao - outra mensagem
#Oferecer para fazer a cnh caso for maior de 18 e nao tiver carteira - idade >18 and chn == nao - 


idade = int(input('Qual a sua idade? \n'))

cat = ['A', 'B', 'C', 'D', 'E'] 


if idade <18:
    print(f'Ainda nao esta na hora.')

else:
    cnh = (input('Voce tem CNH? Y/N ')).upper()

    if idade >= 18 and cnh == 'N':
        print(f'Venha fazer sua CNH conosco!') 

    else:
        print(input(f'Qual categoria? {cat} ').upper())
        print(f'Parabens, voce e bixao!')

        #com categoria X voce so pode dirigir N (if!!!)
