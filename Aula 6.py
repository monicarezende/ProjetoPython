"""
fibonacci = [1, 1]
elementos = int(input("Quantidade de elementos: "))

for numero in range(2, elementos):
    novo_numero = fibonacci[numero - 1] + fibonacci[numero - 2]
    fibonacci.append(novo_numero)
    print(fibonacci)
"""

"""
Exercício 23
Nome: Pedra, Papel e Tesoura
Objetivo: Criar um jogo de pedra, papel e tesoura, jogador versus computador.
Dificuldade: Intermediário
1 - Crie um programa que receba uma jogada do usuário (pedra, papel ou tesoura).
Exiba a mensagem: "Você jogou {}.", onde '{}' é a jogada do usuário.
2 - Faça com que seu jogo rode infinitamente, a menos que o usuário digite "sair".
3 - Caso o usuário digite "pedra, papel ou tesoura", prossiga com o jogo, caso ele digite "sair", encerre o jogo e caso ele digite qualquer outra coisa, pergunte a jogada novamente.
4 - Faça com que o programa ignore se o usuário digitou Pedra, PEDRA, ou pEdRa, ambos devem ser entendidos como "pedra".
5 - Gere uma jogada aleatória para o computador.
Exiba a mensagem: "Computador jogou {}.", onde '{}' é a jogada do computador.
6 - Exiba o resultado da jogada.
Pedra quebra Tesoura.
Tesoura corta Papel.
Papel embrulha Pedra.
7 - Caso o jogador tenha ganhado, exiba: "Você ganhou.", caso contrário, exiba: "Você perdeu.".
8 - Você também deverá criar um placar para o jogo, onde cada jogada que o jogador vencer, adicione 1 ponto ao placar do jogador e cada jogada que o computador vencer, adicione um ponto ao placar do computador.
Ao término da execução do programa (quando o jogador digitar "sair"), exiba a quantidade de rodas, a quantidade de pontos de cada um, se o jogador venceu, perdeu ou se deu empate.
"""

"""
from random import randint

ponto_jogador = 0
ponto_computador = 0
empate = 0

while True:

    jogada_usuario = input("Insira sua jogada: ").lower()
    if jogada_usuario == "sair":
        print("Vitórias: {}. Derrotas: {}. Empates {}.".format(ponto_jogador, ponto_computador, empate))
        if ponto_jogador > ponto_computador:
            print("Você venceu!")
        elif ponto_jogador < ponto_computador:
            print("Você perdeu :(")
        elif ponto_jogador == ponto_computador:
            print("O jogo ficou empatado.")
        break
    print("Você jogou {}".format(jogada_usuario))

    aleatorio = randint(1, 3)
    if aleatorio == 1:
        jogada_aleatoria = "pedra"
    elif aleatorio == 2:
        jogada_aleatoria = "papel"
    elif aleatorio == 3:
        jogada_aleatoria = "tesoura"
    print("Computador jogou {}".format(jogada_aleatoria))

    if jogada_usuario == "pedra" and jogada_aleatoria == "tesoura":
        print("{} esmaga {}".format(jogada_aleatoria, jogada_usuario))
    elif jogada_usuario == "papel" and jogada_aleatoria == "pedra":
        print("{} embrulha {}".format(jogada_aleatoria, jogada_usuario))
    elif jogada_usuario == "tesoura" and jogada_aleatoria == "papel":
        print("{} corta {}".format(jogada_aleatoria, jogada_usuario))

    if jogada_aleatoria == "pedra" and jogada_usuario == "tesoura":
        print("{} esmaga {}".format(jogada_aleatoria, jogada_usuario))
    elif jogada_aleatoria == "papel" and jogada_usuario == "pedra":
        print("{} embrulha {}".format(jogada_aleatoria, jogada_usuario))
    elif jogada_aleatoria == "tesoura" and jogada_usuario == "papel":
        print("{} corta {}".format(jogada_aleatoria, jogada_usuario))

    if jogada_usuario == jogada_aleatoria:
        empate = empate + 1
        print("Essa jogada ficou empatada!")
    elif jogada_usuario == "pedra" and jogada_aleatoria == "tesoura" or jogada_usuario == "papel" and jogada_aleatoria == "pedra" or jogada_usuario == "tesoura" and jogada_aleatoria == "papel":
        ponto_jogador = ponto_jogador + 1
        print("Você venceu essa jogada!")
    elif jogada_aleatoria == "pedra" and jogada_usuario == "tesoura" or jogada_aleatoria == "papel" and jogada_usuario == "pedra" or jogada_aleatoria == "tesoura" and jogada_usuario == "papel":
        ponto_computador = ponto_computador + 1
        print("Você perdeu essa jogada!")
"""
"""
nome = "Mônica Rezede"
nome_split = nome.split(" ")
print(nome_split)
"""

"""
# SPLIT

frase = input("Escreva uma frase com 5 palavras: ")
palavras = frase.split(" ")
for palavra in palavras:
    print(palavra)
"""

"""
# REVERSE

lista = [1, 2, 3, 4, 5]
print(lista)
lista.reverse()
print(lista)


lista = []
for string in range(3):
    string = input("Insira uma string: ")
    lista.append(string)

lista.reverse()
print(lista)
"""

"""
# JOIN

lista = ["Monica", "Rezende"]
nome = " ".join(lista)
print(nome)
"""
"""
lista = []
for string in range(3):
    string = input("Insira uma string: ")
    lista.append(string)

nova_lista = " ".join(lista)
print(nova_lista)
"""

"""
nome_completo = input("Insira seu nome completo: ")
print(nome_completo)
lista_nome = nome_completo.split(" ")
print(lista_nome)
lista_nome.reverse()
print(lista_nome)
nome_invertido = " ".join(lista_nome)
print(nome_invertido)
"""

"""
from random import randint
lista = [5, 10, 15, 20, 25]
indice_aleatorio = randint(0, len(lista) - 1)
elemento_aleatorio = lista[indice_aleatorio]
print(elemento_aleatorio)
# O código acima irá obter um elemento aleatório da lista e exibí-lo na tela.
"""

from random import randint

palavras = input("Insira uma frase: ")
# lista_palavras = palavras.split(" ")
print(palavras)
aleatorio = randint(0, len(palavras) - 1)
elemento_aleatorio = palavras[aleatorio].upper()
print(elemento_aleatorio)









