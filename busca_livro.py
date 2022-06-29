'''
Um pesquisador procura títulos de livros que contenham determinada palavra-chave.
Elabore uma função que receba uma lista de títulos e retorne uma outra lista, contendo
apenas os índices dos títulos que atendem a solicitação. 
a) A função deve aceitar tanto 'Azul' como 'azul', por exemplo.
b) Para esse exercício considere apenas '.' e ',' como pontuação.
c) Se a busca é por 'azul', não deve retornar 'azulado'.
'''


def busca_tit(lista, chave):
    '''A função recebe, como parâmetros, uma lista de títulos e uma palavra-chave.
       Procura a palavra-chave nos títulos e retorna uma lista dos índices em que
       a chave é encontrada.
    '''
    indices=[]
    #--padronizando a palavra-chave
    chave=chave.lower()
    for indice,titulo in enumerate(lista):
    #--apagando a pontuação
        for letra in titulo:
            if letra in '.,!:?': 
               titulo=titulo.replace(letra,'')
    #--padronizando cada título e transformando em lista de palavras
        titulo=(titulo.lower()).split()
    #--conferindo a presença da chave em cada título e armazenando o índice
        for palavra in titulo:
            if chave==palavra:
                indices.append(indice) 
    return indices

#--teste da função
livros=['O menino do dedo verde', 'Como era verde o meu vale', 'Olhando a campina verdejante',
        'Salve o verde, Frederico!', 'Olhar o Verde. Uma necessidade.', 'A queda de Roma.']

print(busca_tit(livros,'verde'))
        
        
    
