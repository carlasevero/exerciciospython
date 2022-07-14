'''
Faça um programa que receba a idade, o peso, a altura, a cor dos olhos
 (A – Azul, P- Preto, V- Verde e C- Castanho) e a cor dos cabelos (P – 
Preto, C- Castanho, L – Louro e R-Ruivo) de 20 pessoas e que calcule e 
mostre:

1) A quantidade de pessoas com idade superior a 50 anos e peso inferior
a 60 quilos;
2)A média das idades das pessoas com altura inferior a 1,50;
3)A porcentagem de pessoas com olhos azuis entre as pessoas analisadas;
4) A quantidade de pessoas ruivas que não possuem olhos azuis.
'''

print(65*'=')
print('CADASTRO'.center(65))
print(65*'=')
print('''\nAtenção: a seguir o programa vai solicitar a você o cadastro de
vinte pessoas. Preencha adequadamente os dados solicitados para
que o exercício possa ser concluído. Obrigada e vamos lá!''')
print()
print(65*'=')

#-- O programa recolhe as informações das 20 pessoas e valida as respostas

cadastro={}

for x in range(20):
    print(f'\nINCLUSÃO {x+1}:')

    pessoa={}
    
    nome=(input('Digite apenas o primeiro nome: ')).strip()
    while not nome.isalpha() or len(nome)<2:
        nome=(input('Inválido. Digite apenas o primeiro nome: ')).strip()

    idade=(input('Qual a idade dessa pessoa? ')).strip()
    while not idade.isdigit() or not 0<int(idade)<130:
        idade=((input('Inválido. Qual a idade dessa pessoa? ')).strip())
    idade=int(idade)

    peso=((input('Qual o peso dessa pessoa? ')).strip()).replace(',','.')
    while not (peso.replace('.','')).isdigit() or not 0<float(peso)<450:
        peso=((input('Inválido. Qual o peso dessa pessoa? ')).strip()).replace(',','.')
    peso=float(peso)

    altura=((input('Qual a altura? ')).strip()).replace(',','.')
    while not (altura.replace('.','')).isdigit() or not 0<float(altura)<3:
        altura=((input('Inválido. Qual a altura? ')).strip()).replace(',','.')
    altura=float(altura)

    olhos=((input('Escolha a cor dos olhos ([A] Azuis [P] Pretos [V] Verdes [C] Castanhos): ')).strip()).upper()
    while olhos not in 'APVC' or len(olhos)!=1:
        olhos=((input('Inválido. Escolha a cor dos olhos: ')).strip()).upper()

    cabelos=((input('Escolha a cor dos cabelos ([P] Pretos [C] Castanhos [L] Louros [R] Ruivos): ')).strip()).upper()
    while cabelos not in 'PCLR' or len(cabelos)!=1:
        cabelos=((input('Inválido. Escolha a cor dos cabelos: ')).strip()).upper()

#-- As respostas são alocadas no dicionário 'cadastro'

    pessoa['Nome']=nome
    pessoa['Idade']=idade
    pessoa['Peso']=peso
    pessoa['Altura']=altura
    pessoa['Olhos']=olhos
    pessoa['Cabelos']=cabelos

    chave='Pessoa '+str(x+1)

    cadastro[chave]=pessoa

print()
print(65*'=')
print('RESPOSTA ÀS QUESTÕES LEVANTADAS'.center(65))
print(65*'=')

#-- Variáveis que armazenarão os itens solicitados pelo programa

resp_um=0
resp_dois=0
resp_tres=0
resp_quatro=0
cont_idade=0

#-- O programa percorre o dicionário 'cadastro' verificando os itens pedidos

for chave in cadastro:
    if cadastro[chave]['Idade']>50 and cadastro[chave]['Peso']<60:
        resp_um+=1
    if cadastro[chave]['Altura']<1.5:
        resp_dois+=cadastro[chave]['Idade']
        cont_idade+=1
    if cadastro[chave]['Olhos']=='A':
        resp_tres+=1
    elif cadastro[chave]['Cabelos']=='R':
        resp_quatro+=1

#-- Cálculos adicionais necessários
        
resp_dois=resp_dois/cont_idade
resp_tres=resp_tres*100/20

#-- Retorno final das informações solicitadas

print()
print(f'Quantidade de pessoas com idade superior a 50 anos e peso inferior a 60 quilos: {resp_um}')
print(f'Média das idades das pessoas com altura inferior a 1,50: {resp_dois}')
print(f'Porcentagem de pessoas com olhos azuis : {resp_tres} %')
print(f'Quantidade de pessoas ruivas que não possuem olhos azuis: {resp_quatro}')
    
