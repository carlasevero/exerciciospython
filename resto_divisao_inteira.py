'''
Escreva um programa que calcule o resto da divisão inteira entre dois números.
Utilize apenas as operações de soma e subtração para calcular o resultado.
'''

#--imprimindo o cabeçalho
print(65*'-')
print('RESTO DA DIVISÃO INTEIRA'.center(65))
print('(apenas com operações de soma e subtração)'.center(65))
print(65*'-')

#--recebendo e validando os dados
while True:
    dividendo = input('\nPor favor, digite um dividendo inteiro: ')
    while not dividendo.isnumeric():
        dividendo = input('Valor inválido. Digite um inteiro: ')
    dividendo = int(dividendo)

    divisor = input('\nPor favor, digite um divisor inteiro: ')
    while not divisor.isnumeric():
        divisor = input('Valor inválido. Digite um inteiro: ')
    divisor = int(divisor)

    if dividendo>=divisor:
        break
    else:
        print('\nPara este exercício, o dividendo deve ser maior que o divisor.')
        print('Tente novamente:')
        print(65*'-')

#--realizando a operação de divisão
contador = 0
temporario = dividendo
while temporario >= divisor:
    temporario = temporario - divisor
    contador += 1

#--imprimindo o resultado    
print()
print(65*'-')
print(f'O resultado da divisão de {dividendo} por {divisor} é {contador}.'.center(65))
print(f'* O RESTO DA OPERAÇÃO É {temporario} *'.center(65))
print(65*'-')


    
