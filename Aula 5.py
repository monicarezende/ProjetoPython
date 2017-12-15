"""
# Exercício slide 131

nomes = ["Edi", "Camila", "Amanda", "Monica", "Victoria"]
for nome in nomes:
    print(nome)

for nome in nomes:
    upper_case = nome.upper()
    print(upper_case)

qtde_elementos = len(nomes)
print(qtde_elementos)
"""

"""
Exercício 20
Nome: Números primos
Objetivo: Criar um for (loop) para detectar se um número é primo ou não.
Dificuldade: Avançado
Os números primos são aqueles números divisíveis APENAS por ele mesmo e por um.
Ele NÃO PODE ser divisível por qualquer número entre esses.
Por exemplo:
2 é primo pois ele é divisível apenas por 1 e por 2.
3 é primo pois ele é divisível apenas por 1 e por 3.
4 não é primo pois ele é divisível por 1, por 2 e por 4.
E assim por diante.
Para checar se um número é primo na programação, precisamos checar se ele é divisível por cada número que está entre ele e 1, para isso, utilizamos o 'for'.
1 - Crie um programa que receba um número digitado pelo usuário e execute um 'for' pelo exato número de vezes do número digitado.
2 - Para cada vez que o 'for' rodar, cheque se o número principal que foi digitado é divisível por aquele número que está no for em questão.
Para saber se um número é divisível pelo outro, saiba que o resto da divisão inteira deve resultar em 0 (zero).
Dica: Crie uma variável chamada 'contador' e para cada vez que um número for divisível pelo outro, acrescente 1 (um) ao valor do contador, se ao final da execução do loop, o contador for igual a 2, significa que o número é primo, caso contrário (3 ou mais) o número NÃO é primo.
Outra dica: Quando o range é utilizado, o for começa a ser executado a partir do índice 0, por tanto, o número que você terá que começar a realizar a divisão é 1.


numero_digitado = int(input("Insira um número: "))
contador = 0

for numero in range(1, numero_digitado + 1):
    n = numero_digitado % numero
    if n == 0:
        contador = contador + 1


if contador >= 3:
    print("O número não é primo.")
else:
    print("O número é primo.")
"""
"""
lista = [46, 64, 1, 4, 0, 62, 7, 2, 8, 231, 75]
for numero in lista:
    if numero % 2 == 0:
        print(numero)
"""
"""
# Exercício slide 132

lista = [46, 64, 1, 4, 0, 62, 7, 2, 8, 231, 75]
for numero in lista:
    if numero % 2 != 0:
        print(numero)
"""


"""
# LISTA UNICA

lista = [4, 2, 5, 4, 7, 2, 7, 9, 5, 10]

print(lista)
lista_unica = (set(lista))
print(lista_unica)
print(lista.count(4))
print(lista.count(lista[0]))
"""
"""
lista_vazia = []

for numero in lista:
    if lista_vazia.count(numero) == 0:
        lista_vazia.append(numero)
        print("Estou veficando o número {}.".format(numero))
        print("O número {} está presente {} vezes na lista.".format(numero, lista.count(numero)))
"""


"""
# WHILE LOOP

while True:
    print('Essa mensagem será exibida infinitamente.')
"""
"""
while True:
    mensagem = input("Digite uma mensagem: ")
    print("Você digitou a mensagem {}".format(mensagem))
"""
"""
numero = 0
while numero <= 10:
    print("Número {}".format(numero))
    numero = numero + 1
"""
"""
while True:
    numero = int(input("Insira um número inteiro: "))
    if numero > 50:
        print("O número digitado é muito alto.")
    else:
        print("O número digitado é {}".format(numero))
"""
"""
numero = 0
while numero <= 50:
    numero = int(input("Insira um número inteiro: "))
    print("O número digitado é {}".format(numero))
"""
"""
numero = 0
while numero <= 50:
    numero = int(input("Insira um número inteiro: "))
    if numero > 50:
        print("O número digitado é muito alto.")
    else:
        print("O número digitado é {}".format(numero))
"""
