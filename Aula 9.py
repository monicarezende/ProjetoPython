"""
refeicoes = {"salada": 12.45,
             "prato principal": 30.95,
             "sobremesa": 7.50,
             "café": 3.50
             }


def pegar_refeicao(indice):
    refeicao = refeicoes.get(indice)
    if refeicao == None:
        print("Rfeição não existe")
    else:
        print("Refeicao: {}".format(refeicao))
    return refeicao


custo1 = pegar_refeicao("salada")
custo2 = pegar_refeicao("sobremesa")
conta = 0
conta = conta + custo1 + custo2
print(conta)


del refeicoes["café"]
print(refeicoes)

"""

"""
precos = {
    "banana": 4,
    "maçã": 2,
    "laranja": 1.5,
    "pera": 3
    }

estoques = {
    "banana": 6,
    "maçã": 0,
    "laranja": 32,
    "pera": 15
    }

total = 0
for fruta in precos:
    preco = precos[fruta]
    estoque = estoques[fruta]
    # print("Fruta {}".format(fruta))
    # print("\tPreço R${:.2f}".format(preco))
    # print("\tEstoque: {}".format(estoque))
    total += preco * estoque

# print("\nO valor total é R${:.2f}".format(total))

mantimentos = []


def computar_compra(mantimento):
    compra_total = 0
    print("Sua compra foi realizada com sucesso!")
    for mantimento in mantimentos:
        compra_preco = precos[mantimento]
        compra_estoque = estoques[mantimento]
        if compra_estoque > 0:
            compra_total += compra_preco
            estoques[mantimento] -= 1
            print("\nFruta: {}".format(mantimento))
            print("\tPreço: R${:.2f}".format(compra_preco))
            print("\tEstoque: {}".format(estoques[mantimento]))
        else:
            print("\nA fruta {} está indisponível no estoque.".format(mantimento))
    return compra_total


while True:
    frutas_disponveis = list(precos.keys())
    print("As frutas disponíveis em estoque são:\n- {}".format("\n- ".join(frutas_disponveis)))
    print("Para finalizar sua compra digite 'finalizar compra'.")
    comprar_fruta = input("Digite qual fruta deseja comprar para inseri-la na cesta de compras: ")
    if comprar_fruta == "finalizar compra":
        computar_compra(mantimentos)
        break
    else:
        mantimentos.append(comprar_fruta)
"""







