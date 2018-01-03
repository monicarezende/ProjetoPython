"""
# Construa uma lista com 3 palavras digitadas pelo usuário;
# Pegue uma das palavras de forma aleatória;
# Exiba a palavra obtida na tela com todas as letras maiúsculas.

from random import randint

lista = []

for palavra in range(3):
    palavra_usuario = input("Insira uma palavra: ").upper()
    lista.append(palavra_usuario)

indice_aleatorio = randint(0, len(lista) - 1)
elemento_aleatorio = lista[indice_aleatorio]
print(elemento_aleatorio)
"""

"""
# Vamos criar uma função chamada ‘contar_numeros_pequenos(numeros)’ que recebe uma lista de números.
# A função deverá somar todos os números que estão dentro da lista e são menores do que 10.
# Após realizar a soma, deverá retornar o valor total.
# Exiba o valor total na tela.


def contar_numeros_pequenos(numeros):
    soma_numeros_pequenos = 0
    for numero in numeros:
        if numero < 10:
            soma_numeros_pequenos = soma_numeros_pequenos + numero
    return soma_numeros_pequenos


lista = [53, 66, 4, 6, 1, 47, 9, 32]

print(contar_numeros_pequenos(lista))
"""

"""
partidos = {
    "PT": {
        "nome": "Partido dos Trabalhadores",
        "sede": "Brasília",
        "presidente": "Gleisi Hoffmann",
        "numero_eleitoral": 13,
        "candidato_proprio": True,
        "ideologias": [
            "Socialismo democrático",
            "Desenvolvimentismo",
            "Lulismo",
            "Trotskismo",
            "Democracia"
        ]
    },
    "PV": {
        "nome": "Partido Verde",
        "sede": "São Paulo",
        "presidente": "José Luiz Penna",
        "numero_eleitoral": 43,
        "candidato_proprio": False,
        "ideologias": [
            "Ambientalismo",
            "Ecologismo",
            "Liberalismo social",
            "Progressismo",
            "Social democracia",
            "Democracia"
        ]
    }
}


def procurar_partidos_ideologia(ideologia):
    lista_partidos = []
    for partido in partidos:
        count_ideologia = partidos[partido]["ideologias"].count(ideologia)
        if count_ideologia > 0:
            lista_partidos.append(partido)
    return lista_partidos


partidos_democracia = procurar_partidos_ideologia("Democracia")
print(partidos_democracia)
partidos_socialismo = procurar_partidos_ideologia("Socialismo democrático")
print(partidos_socialismo)
"""

"""
inventario = {
    "dinheiro": 500,
    "carteira": ["joia", "cartao", "caderno"],
    "mochila": ["faca", "blusa", "guarda-chuva", "garrafa"]
}

# Adicione R$50,00 ao elemento "dinheiro" do inventário.
inventario["dinheiro"] += 50
print(inventario["dinheiro"])

# Adicione um novo item à carteira.
novo_item = "celular"
inventario["carteira"].append(novo_item)
print(inventario["carteira"])

# Ordene os itens da bolsa por ordem alfabética.
inventario["mochila"].sort()
print(inventario["mochila"])

# Exiba na tela quantos itens a pessoa tem na carteira e na bolsa.
print(len(inventario["carteira"]))
print(len(inventario["mochila"]))

# Adicione uma nova lista ao inventário chamada "bolso", e inclua alguns itens.
inventario["bolso"] = ["chave", "caneta", "botão"]
print(inventario["bolso"])
"""
