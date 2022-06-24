'''
Escreva um programa que recebe como entrada a data de nascimento do usuário e informa
qual o seu signo.
'''

#--função
def valida_num(num, limite):
    '''
    parametro num: dia do mês em que a pessoa nasceu
    parametro limite: máximo de dias que o mês pode possuir (29,30 ou 31)
    
    Se o usuário informou um número diferente de zero e dentro do limite permitido,
    retorna o inteiro de num. Se não, continua a solicitar o número.
    '''
    while not num.isnumeric() or int(num) > limite or int(num) == 0:
        num = input('Dia inválido. Tente novamente: ')
    return int(num)

#--tabelas de dados          
meses_29 = ['fevereiro']
meses_30 = ['abril','junho','setembro','novembro']
meses_31 = ['janeiro','março','maio','julho','agosto','outubro','dezembro']
todos_meses = [21,'janeiro',19,'fevereiro',21,'março',21,'abril',21,'maio',21,'junho',23,'julho',23,'agosto',
         23,'setembro',23,'outubro',22,'novembro',22,'dezembro']
signos = ['aquário','peixes','áries','touro','gêmeos','câncer','leão','virgem','libra','escorpião','sagitário','capricórnio']
         
#--imprimindo o cabeçalho
print(65*'-')
print('DESCUBRA QUAL É O SEU SIGNO'.center(65))
print(65*'-')

#--recebendo e validando os dados de dia e mês
mes = (input('Por favor, em que mês você nasceu? ')).lower()
while True:
    if mes in meses_29:
        num = input(f'Em que dia de {mes} você nasceu? ')
        dia = valida_num(num, 29)
        break
    elif mes in meses_30:
        num = input(f'Em que dia de {mes} você nasceu? ')
        dia = valida_num(num, 30)
        break
    elif mes in meses_31:
        num = input(f'Em que dia de {mes} você nasceu? ')
        dia = valida_num(num, 31)
        break
    else:
        mes = (input('Mês inválido. Tente novamente: ')).lower()

#--efetuando a pesquisa e retornando o resultado
x = 1
while x < 24:
    if mes == todos_meses[x]:
        if dia < todos_meses[x-1]:
            print(f'\nSeu signo é {signos[x//2-1]}.')
        else:
            print(f'\nSeu signo é {signos[x//2]}.')
        break
    x+=2
        
    


    
    
