'''
Faça um programa que fique pedindo uma resposta do usuário, entre 1, 2 e 3. 
Se o usuário digitar 1, o programa deve cadastrar um novo usuário, solicitando 
nome, idade, e-mail e CPF, guardando esse cadastro num dicionário cuja chave 
será o CPF da pessoa. Quando o usuário digitar 2, o programa deve imprimir os 
usuários cadastrados; e se o usuário digitar 3, o programa deve fechar.        
'''

#-- funções

def escolha():
    '''
    A função apresenta um menu de opções, registra e valida a
    opção escolhida pelo cliente. Retorna a opção validada.'''
    
    print('\nO QUE VOCÊ DESEJA FAZER?')
    print('[1] novo cadastro [2] mostrar cadastro [3] encerrar cadastro')
    opcao=input('\nPOR FAVOR, INFORME SUA OPÇÃO: ')
    while opcao not in '123' or len(opcao)!=1:
        opcao=input('\nOpção inválida. Tente novamente: ') 
    return opcao

def valida_cpf(cpf):
    '''
    A função recebe um número de cpf e verifica:
    a) se a cadeia contém apenas dígitos
    b) se foram digitados 11 caracteres
    c) se não foram digitados apenas números repetidos
    d) se o dígito verificador é consistente
    Retorna True se as condições forem atendidas.'''
    
    lista_cpf=[int(num) for num in cpf if num.isdigit()]
    if len(lista_cpf)!=11:
        return False
    if lista_cpf==lista_cpf[::-1]:
        return False
    for i in range(9,11):
        valor=sum((lista_cpf[x]*((i+1)-x) for x in range(0,i)))
        digito=((valor*10)%11)%10
        if digito!=lista_cpf[i]:
            return False
    return True

def valida_mail(email):
    '''
    A função recebe um e-mail e compara com uma expressão regular,
    retornando True se a condição for atendida.'''
    
    import re
    regex='^[a-z0-9]+[\.-_]?[a-z0-9]+[@]\w+[.]\w{2,3}([.]\w{2,3})?$'
    if (re.search(regex,email)):
        return True
    else:
        return False

#-- PROGRAMA PRINCIPAL

cadastro={}

print(65*'=')
print('CADASTRO DE PESSOAL'.center(65))
print(65*'=')
    
while True:
    digito=escolha()
    
#-- procedimento para opção 3
    
    if digito=='3':
        print()
        print(65*'=')
        print('VOCÊ SAIU DO PROGRAMA'.center(65))
        print(65*'=')
        break
    
#-- procedimento para opção 1
    
    elif digito=='1':
        print(65*'-')
        unico={}
        nome=(input('Informe o nome: ')).strip()
        while not (nome.replace(' ','')).isalpha():
            nome=(input('Nome inválido. Tente novamente: ')).strip()
        idade=(input('Informe a idade: ')).strip()
        while idade=='0' or not idade.isdigit():
            idade=(input('Idade inválida. Tente novamente: ')).strip()
        email=(input('Informe o e-mail: ')).strip()
        while not valida_mail(email):
            email=(input('E-mail inválido. Tente novamente: ')).strip()
        cpf=(input('Informe o cpf (use apenas números): ')).strip()
        while not valida_cpf(cpf):
            cpf=(input('Cpf inválido. Tente novamente: ')).strip()
        unico['Nome']=nome
        unico['Idade']=idade
        unico['E-mail']=email
        cadastro[cpf]=unico
        print()
        print('-CADASTRO INCLUÍDO-'.center(65))
        print(65*'-')

#-- procedimento para opção 2
        
    elif len(cadastro)==0:
        print(65*'=')
        print('AINDA NÃO HÁ NENHUM CADASTRO'.center(65))
        print(65*'=')
    else:
        print()
        print(65*'=')
        print('LISTA DE PESSOAS CADASTRADAS'.center(65))
        print(65*'=')
        for chave,unico in cadastro.items():
            print(f'\nCPF: {chave}')
            for x,y in unico.items():
                print(f'     {x}: {y}')
        print(65*'-')
                


            
