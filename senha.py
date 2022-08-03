'''
Faça um programa de validação de senha. Solicite o nome completo, a data de nascimento e uma senha. 
Realize uma validação na senha, a mesma não pode conter nome, sobrenomes e/ou da data de nascimento. 
Peça uma nova senha até que ela seja válida.'''

def busca(senha, lista):
    '''A função recebe, como parâmetros, a senha escolhida e uma lista com
    nome e sobrenomes do usuário. Retorna True se algum dos nomes da lista
    for encontrado na senha.'''
    return any([nome in senha.upper() for nome in lista])

#---Definindo qual o ano atual
from datetime import date
ano_atual = date.today().year

print(65*'=')
print('VALIDAÇÃO DE SENHA'.center(65))
print(65*'=')

#---Recebendo e validando o nome completo do usuário
while True:
    nome=((input('Por favor, informe seu nome completo: ')).strip()).upper()
    if len(nome)>5 and (nome.replace(' ','')).isalpha():
        break
    else:
        print('\nInformação inválida!')

#---Transformando o nome completo em uma lista de nomes
lista_n=nome.split()


print('\nA seguir, informe sua data de nascimento:')

#---Recebendo e validando o ano de nascimento
while True:
    ano=input('   Ano: ')
    try:
        int(ano)
    except:
        print('\nInformação inválida!')
        continue
    if 1900<int(ano)<ano_atual:
        break
    else:
        print('\nInformação inválida!')

#---Recebendo e validando o mês de nascimento
while True:
    mes=input('   Mês (um número, de 1 a 12): ')
    try:
        int(mes)
    except:
        print('\nInformação inválida!')
        continue
    if 0<int(mes)<13:
        break
    else:
        print('\nInformação inválida!')

#---Recebendo e validando o dia de nascimento
while True:
    dia=input('   Dia: ')
    try:
        int(dia)
    except:
        print('\nInformação inválida!')
        continue
    if 0<int(dia)<32:
        break
    else:
        print('\nInformação inválida!')


#---Solicitando a senha
print(65*'=')
print('''A seguir, escolha uma senha com 8 dígitos. Atenção: sua senha não
deve conter suas informações de nome e data de nascimento.''')
print()
senha=(input('Informe a senha: ')).strip()

#---Verificando se a senha está de acordo com os itens permitidos
while True:
    if busca(senha, lista_n):
        senha=(input('Senha inválida!Tente novamente: ')).strip()
        continue
    elif len(senha)!=8:
        senha=(input('Senha inválida!Tente novamente: ')).strip()
        continue
    elif ano in senha or dia in senha or mes in senha:
        senha=(input('Senha inválida!Tente novamente: ')).strip()
        continue
    else:
        break

#---Aceitando a senha    
print()
print(65*'=')
print('Sua senha foi aceita. Obrigada.')
print(65*'=')
        

