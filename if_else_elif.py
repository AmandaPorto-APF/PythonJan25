idade = int(input('Entre com sua idade: '))

# if idade < 18:
#     print(f'Voce e muito jovem. \n Va para a casa beber leite.')

# else:
#     print(f'Voce e maio de idade')
#     print(f'Pode beber a vontade')

#%% AND
# if idade <18 or idade >60:
#     print(f'voce nao esta autorizado a beber')

# else:
#     print(f'Voce e maio de idade e pode beber a vontade')

#%% ELIF
if idade <18:
    print(f'voce nao esta autorizado a beber')

elif idade >90:
    print(f'va pro bingo tomar sopa')

else:
    print(f'Voce e maio de idade e pode beber a vontade')