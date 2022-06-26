'''
Uma sorveteria vende cinco produtos diferentes, cada um com um preço. Faça um programa que processe
diversas vendas, lembrando que cada venda efetuada pode ser composta por diversas unidades de diversos
produtos. O programa deverá utilizar:
(a) uma função que apresente na tela um menu indicando os preços dos produtos. Esse menu deve ser
apresentado no início de cada venda.
(b) uma função que processe cada venda individual e forneça o valor a pagar.
(c) uma terceira função que emita um relatório no final do dia, informando dados gerais das vendas do
dia (número total de itens vendidos de cada produto, total pago para cada produto, total arrecadado e
valor médio de cada compra)
'''

#--funções solicitadas pelo exercício
def chama_menu():
    '''Exibe a lista completa de produtos oferecidos: código, nome e preço.
    '''
    print('\nNossos produtos:')
    print(19*' ','CÓD','PRODUTO'.ljust(31),'PREÇO(R$)')
    print(19*' ',45*'-')
    for produto in menu:
        print(19*' ',produto[0].ljust(3),produto[1].ljust(31),f'{produto[2]:.2f}'.replace('.',','))

def venda():
    '''Receba a solicitação de compra do usuário e valida os dados, exibindo a nota
    de compra com totais individuais e total geral a ser pago. Retorna uma lista
    com a quantidade de cada produto adquirida pelo cliente.
    '''
    compra=[[] for produto in menu]
    chama_menu()
    opcoes='ABCDE'
    continua='S'
    print(65*'-')
    print('\nSeu pedido: ')
    while continua=='S':
        codigo=(input('\nPor favor, informe o código do produto desejado: ')).upper()
        codigo=testa_string(codigo,opcoes)
        quantidade=input('Qual a quantidade? ')
        quantidade=testa_inteiro(quantidade)
        for x in range(5):
            if codigo==opcoes[x]:
                compra[x].append(quantidade)
        continua=(input('Deseja adicionar mais algum produto? Digite S ou N: ')).upper()
        continua=testa_string(continua,'SN')
    print(65*'-')
    print('\nSua nota: ')
    print(19*' ','QTD','PRODUTO'.ljust(31),'PREÇO(R$)')
    print(19*' ',45*'-')
    total=0
    for x in range(len(menu)):
        if compra[x]!=[]:
            qtd=sum(compra[x])
            tot=qtd*menu[x][2]
            print(19*' ',f'{qtd:<3}',menu[x][1].ljust(31),f'{tot:.2f}'.replace('.',','))
            total+=tot
    print()
    print(19*' ','Valor total a pagar: R$',f'{total:.2f}'.replace('.',','))
    return compra

def relatorio(final,clientes):
    '''Recebe uma lista com o total de vendas de cada produto (final) e o número total de clientes
    atendidos no período. Exibe o relatório final do período e encerra o programa.
    '''
    print('\nRelatório do dia: ')
    print(19*' ','QTD','PRODUTO'.ljust(31),'PREÇO(R$)')
    print(19*' ',45*'-')
    total=0
    for x in range(len(menu)):
        qtd=final[x]
        tot=qtd*menu[x][2]
        print(19*' ',f'{qtd:<3}',menu[x][1].ljust(31),f'{tot:.2f}'.replace('.',','))
        total+=tot
    media=total/clientes
    print()
    print(19*' ','Valor total arrecadado:  R$',f'{total:.2f}'.replace('.',','))
    print(19*' ','Valor médio por tíquete: R$',f'{media:.2f}'.replace('.',','))
    print(19*' ','Total de tíquetes:      ',f'{clientes}')
    print()
    print(65*'-')
    print('FINAL DE EXECUÇÃO DO PROGRAMA'.center(65))
    print(65*'-')
    
#--outras funções adicionais
def testa_inteiro(num):
    '''Verifica se a string informada (num) contém um número inteiro.
    Quando positivo, retorna o inteiro da string.
    '''
    while not num.isnumeric():
        num = input('Valor inválido. Tente novamente: ')
    return int(num)

def testa_string(txt, conj):
    '''Verifica se a string (txt) informada contém um único caracter e se este pertence ao conjunto (conj)
    de caracteres possíveis. Quando positivo, retorna a própria string.
    
    Exemplo: 'Responda sim [S] ou não [N]'
    Caracteres possíveis (conj): 'SN'
    A função finaliza quando o usuário digitar s,S,n ou N (txt).
    '''
    while len(txt)!=1 or txt not in conj:
        txt=(input('Valor inválido. Tente novamente: ')).upper()
    return txt

        
#---PROGRAMA PRINCIPAL

#--listas
menu = [['A','Refrigerante',3.50],
        ['B','Casquinha Simples',4.00],
        ['C','Casquinha Dupla',5.50],
        ['D','Sundae',7.50],
        ['E','Banana Split',9.00]]

final=[0 for produto in menu]

#--variáveis
clientes=0

#--imprimindo o cabeçalho
print(65*'-')
print('SORVETERIA BEM GELADO'.center(65))
print(65*'-')

while True:
    #--processando cada pedido
    parcial=venda()
    #--transformando a lista de listas em lista de inteiros
    parcial=[0 if parcial[x]==[] else sum(parcial[x]) for x in range(len(parcial))]
    #--acumulando as quantidades de cada pedido e o número de clientes
    final=[final[x]+parcial[x] for x in range(len(menu))]
    clientes+=1
    #--recolhendo e validando a opção de continuidade ou finalização
    print(65*'-')
    print('\nDeseja processar um novo pedido?')
    opta=(input('Digite P para novo pedido ou F para finalizar: ')).upper()
    opta=testa_string(opta,'PF')
    print()
    print(65*'*')
    if opta=='F':
        break

#--processando o relatório final do período
relatorio(final,clientes)











    
    

