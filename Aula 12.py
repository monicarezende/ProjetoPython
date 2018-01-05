"""
# 1 - Dada a lista 'n' com duas listas de números dentro:
# n = [[1,2,3],[4,5,6,7,8,9]]
# Crie uma função que recebe a lista de listas como argumento e retorna uma única lista com todos os números encontrados.


def funcao(lista):
    nova_lista = []
    for sublista in lista:
        for numero in sublista:
            nova_lista.append(numero)
    return nova_lista


n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
print(funcao(n))
"""

"""
# 2 - Crie uma função que receba uma lista de números qualquer e retorne todos os elementos dessa lista multiplicados por 2.


def multiplicar_numeros(lista):
    lista_multiplicada = []
    for numero in lista:
        lista_multiplicada.append(numero * 2)
    return lista_multiplicada


# 3 - Crie uma função que receba uma lista qualquer e exiba todos os elementos dessa lista na tela.


def exibir_lista(lista):
    for item in lista:
        print(item)


# 4 - Declare uma lista qualquer, passe-a pela função criada no item 2 e exiba-a utilizando a função criada no item 3.

n = [4, 5, 6, 7, 8, 9]
exibir_lista(multiplicar_numeros(n))
"""


"""
# TUPLAS
# As tuplas são similares as listas, com a diferença que são imutáveis, ou seja, não podem ser alteradas após a criação.

tupla = 1, 2, 3
print(tupla)
print(type(tupla))


# FUNÇÃO LIST
# A função ‘list’ funciona da mesma forma que as funções ‘str’, ‘int’, ‘float’, para transformar informações. Geralmente ela é útil para transformar tuplas em listas, ou para transformar o resultado da função ‘range’ em listas.

lista_tupla = list(tupla)
print(lista_tupla)
print(type(lista_tupla))
lista_tupla[0] = 5
print(lista_tupla)

# Exemplo com range:
objeto_range = range(6)
print(objeto_range)
lista_objeto_range = list(objeto_range)
print(lista_objeto_range)


# FUNÇÃO RANGE

# A função ‘range’ cria um objeto que funciona como uma espécie de lista com diversos itens.
# Ela vem com dois conjuntos de parâmetros:

# range(stop)
    # range(stop)
    # stop: número de inteiros para gerar, iniciando a partir do zero.
    # Exemplo:
    # range(6) irá retornar [0, 1, 2, 3, 4, 5]

# range([start], stop[, step])
    # range([start], stop[, step])
    # start: número inicial da sequência
    # stop: gera números até esse, porém, não inclui o número informado
    # step: Diferença entre cada número da sequência, onde o padrão é 1
    # Exemplo:
    # range(2, 7, 2) irá retornar [2, 4, 6]


# 5 - Um parque possui 10 árvores a cada 2 metros. Sabendo que o parque começa a ter árvores a partir de 5 metros e tem árvores até 100 metros, qual o total de árvores existentes?

arvores = range(5, 100, 2)
print(len(arvores) * 10)
"""

"""
# FUNÇÕES COM ARGUMENTOS OPCIONAIS


def funcao(argumento1, argumento2=0):
    print(argumento1)
    print(argumento2)


funcao(1)
"""

"""
def somar(a, b, exibir=False):
    total = a + b
    if exibir:
        print(total)
    return total


somar(1, 2, True)
# OU
somar(1, 2, exibir=True)
"""

"""
# 6 - Utilizando a função criada no item 3, crie uma nova função que tenha um argumento opcional chamado 'exibir_chaves' sendo iniciado como padrão 'False'. Caso o valor da variável 'exibir_chaves' seja passado como True, a função irá exibir as chaves da lista, seguindo o modelo: Chave: {}, Valor: {}. Caso contrário, exiba apenas o valor: Valor: {}


def exibir_lista(lista, exibir_chaves=False):
    for chave in range(len(lista)):
        item = lista[chave]
        if exibir_chaves:
            print("Chave: {}, Valor: {}".format(chave, item))
        else:
            print("Valor: {}".format(item))


lista1 = [1, 2, 3, 4, 4]
exibir_lista(lista1, True)
"""

