# Exercício 16 - Joguinho: Salão
# Objetivo: Escrever uma função que funciona como um jogo, onde o usuário deve digitar as suas escolhas e o programa irá indicar o resultado das escolhas.
# Dificuldade: Intermediário
# Crie uma função principal chamada jogo() e execute as tarefas abaixo:
# 1 - O jogador irá entrar em um salão (informe isso a ele utilizando o comando print())
# 2 - Você deve perguntar se ele quer escolher entre a porta esquerda ou a direita
# 3 - Se a resposta for "esquerda" ou "e", exiba a mensagem:
# - Você entrou na sala à esquerda, parece que não tem nada por aqui. Acho melhor você voltar correndo!
# 4 - Caso contrário, se a resposta for "direita" ou "d", exiba a mensagem:
# - Excelente escolha! A sala à direita estava te esperando esse tempo todo! Que maravilhoso isso. Pena que não tem nada aqui para você. :(
# 5 - Caso contrário, se a resposta não foi nenhum dos valores anteriores, exiba a mensagem abaixo e execute a função 'jogo()' novamente.
# - Você não escolheu nenhuma das portas. Tente novamente.

"""
def jogo():
    porta = input("Agora, você está prestes a entrar num salão. Para isso, escolha entre a porta da esquerda ou da direita. Qual das portas você deseja abrir? ").lower()
    if porta == "esquerda" or porta == "e":
        print("Você entrou na sala à esquerda, parece que não tem nada por aqui. Acho melhor você voltar correndo!")
    elif porta == "direita" or porta == "d":
        print("Excelente escolha! A sala à direita estava te esperando esse tempo todo! Que maravilhoso isso. Pena que não tem nada aqui para você. :(")
    else:
        print("Você não escolheu nenhuma das portas. Tente novamente.")
        jogo()


jogo()
"""

"""
# Exercício 17 - Par ou Ímpar: Funções
# Objetivo: Escrever uma função chamada numero_par que recebe um número e torna True caso ele seja par ou False caso seja ímpar
# Dificuldade: Principiante
# Crie uma função chamada 'numero_par(numero)' que receba um número como argumento e retorne True caso ele seja par ou False caso seja ímpar

def numero_par(n):
    print(n)
    print(n % 2)
    print(n % 2 == 0)
    if n % 2 == 0:
        return True
    else:
        return False


numero = int(input("Insira um número: "))
if numero_par(numero):
    print("O número é par.")
else:
    print("O número é impar.")
"""

# Exercício 18 - Praticando: Funções Matemáticas
# Objetivo: Escrever diversas funções que utilizem as funções matemáticas como base para trabalhar com números e praticar a formatação de números e strings.
# Dificuldade: Principiante
# 1 - Peça para o usuário digitar 3 números, envie-os para uma função chamada 'pegar_maior_valor' utilizando o método '*args' e retorne o maior deles utilizando a função max()
# 2 - Peça para o usuário digitar 3 números, envie-os para uma função chamada 'pegar_menor_valor' utilizando o método '*args' e retorne o menor deles utilizando a função min()
# 3 - Peça para o usuário digitar 3 números positivos e 3 números negativos, extraia o módulo (versão positiva) de cada número utilizando a função abs() e exiba na tela o maior e o menor número (utilize as funções criadas anteriormente no exercício 1 e 2).


"""
def funcao():
    return int(input("Insira um número: "))


def inserir_negativo():
    return int(input("Agora, insira um número negativo: "))


def negativo(n):
    if n < 0:
        return abs(n)
    else:
        print("Um dos números não é negativo. Tente novamente!")
        return inserir_negativo()


def pegar_maior_valor(*args):
    return max(args)


def pegar_menor_valor(*args):
    return min(args)


n1 = funcao()
n2 = funcao()
n3 = funcao()
maior_valor = pegar_maior_valor(n1, n2, n3)
print("O maior número é {}.".format(maior_valor))
menor_valor = pegar_menor_valor(n1, n2, n3)
print("O menor número é {}.".format(menor_valor))


n4 = inserir_negativo()
n5 = inserir_negativo()
n6 = inserir_negativo()
n4_abs = negativo(n4)
n5_abs = negativo(n5)
n6_abs = negativo(n6)

maior_valor2 = pegar_maior_valor(n1, n2, n3, n4_abs, n5_abs, n6_abs)
print("Considerando os novos números digitados, o maior número é {}.".format(maior_valor2))
menor_valor2 = pegar_menor_valor(n1, n2, n3, n4_abs, n5_abs, n6_abs)
print("Considerando os novos números digitados, o menor número é {}.".format(menor_valor2))


# 4 - Declare uma função que recebe um número e o formata de acordo com o tipo de sua variável (utilize a função type())
# - Se a variável for um float, formate-a como moeda, exemplo:
# - Entra a variável float 20.0 e exibe na tela R$ 20,00. Regra de formatação: {:.2f}, onde 2 representa o número e casas decimais.
# - Se a variável for um int, formate-a deixando com pelo menos 5 dígitos (colocando zeros na frente). Regra de formatação: {:02d}, onde 2 representa o número de dígitos.
# - Se a variável for uma string, formata-a para que utilize 10 espaços adicionais à esquerda. Regra de formatação: {:>1}, onde 1 representa o número de espaços que irá utilizar.
# - Caso a variável não seja nenhuma dessas, exiba a mensagem "Esse tipo de variável não está mapeado."


def tipo_variavel(variavel):
    if type(variavel) == float:
        print("O número digitado {:.2f} é do tipo float.".format(variavel))
    elif type(variavel) == int:
        print("O número digitado {:05d} é do tipo inteiro.".format(variavel))
    elif type(variavel) == str:
        print("O número digitado {:>10} é do tipo string.".format(variavel))
    else:
        print("Esse tipo de variável não está mapeado.")


tipo_variavel(0.6)
tipo_variavel(6)
tipo_variavel("6")
tipo_variavel(True)
"""

"""
animais = "catdogfrog"
cat = animais[:3]
dog = animais[3:6]
frog = animais[6:]
print(cat)
print(dog)
print(frog)

animais = ["gato", "cachorro", "morcego"]
print(animais.index("morcego"))
# .index devolve a posição em que o item está na lista
animais.insert(0, "papagaio")
print(animais)
# .insert insere um novo item na posição definida


animais = ["gato", "cachorro", "morcego"]
for animal in animais:
    print(animal)
# Para cada item da lista animais vai haver um item chamado animal


lista = [1, 7, 4, 9, 4, 8]
for numero in lista:
    lista2 = numero * 3
    if lista2 % 2 == 0:
        print(lista2)
"""
"""
numeros = []
for numero in range(3):
    print("Posição: {}".format(numero))
    numero_digitado = int(input("Digite um número: "))
    print("Número digitado: {}".format(numero_digitado))
    numeros.append(numero_digitado)

print(numeros)
# range() cria uma lista com três números e imprime suas posições
"""
"""
animais = ["gato", "cachorro", "morcego"]
animais.sort()
print(animais)
# para ordem decrescente
animais.sort(reverse=True)
print(animais)
"""
"""
lista1 = [5, 6, 3, 2, 1]
lista_quadrado = []
for numeros in lista1:
    numero_quadrado = numeros ** 2
    lista_quadrado.append(numero_quadrado)
    lista_quadrado.sort()
print(lista_quadrado)
"""

"""
Exercício 19
Nome: Praticando: Listas/For (Loop)
Objetivo: Praticar a criação e a leitura básica de listas com números e textos.
Dificuldade: Intermediário
1 - Crie uma lista com alguns números inseridos manualmente (não há necessidade do usuário inserí-los).
2 - Crie um for que varra cada elemento da lista e exiba-o no console.
3 - Declare um novo for que exiba apenas os números maiores que 3.
4 - Declare um outro for que exiba apenas os números pares.
5 - Exiba na tela a soma de todos os elementos da lista sem a utilização de funções extras.
6 - Exiba a soma de todos os elementos utilizando a função sum().
7 - Crie uma nova lista a partir de números digitados pelo usuário, faça com que o usuário insira 10 números, porém, utilize o 'for' para isso, em vez de declarar 10 vezes o input de entrada de informação, declare apenas UMA vez e faça com que ele seja executado 10 vezes.
A cada atualização da lista, exiba a quantidade de elementos que ela possui.
8 - Exiba apenas os três primeiros elementos da lista no console.
9 - Exiba apenas os três últimos elementos da lista no console.
10 - Declare uma nova lista vazia chamada 'nomes' e armazene 3 nomes digitados pelo usuário, ordene esses nomes por ordem alfabética e exiba-os na tela, um de cada vez.


# lista = [4, 6, 3, 7, 5]
# 2 for numeros in lista:
    # print(numeros)

# 3 for numeros in lista:
    # if numeros > 3:
        # print(numeros)

#4 for numeros in lista:
    # numeros_par = numeros % 2 == 0
    # if numeros_par:
        # print(numeros)


#5 total = 0
# for numeros in lista:
    # total += numeros
# print(total)


#6 for numeros in lista:
    # total = sum(lista)
# print(total)

#7 lista = []
# for numeros in range(10):
    # numero_digitado = int(input("Insira um número: "))
    # lista.append(numero_digitado)
    # print("A posição do número digitado na lista é {}.".format(numeros))
# print(lista)
#8 print(lista[:3])
#9 print(lista[7:])

# 10 nomes = []
# for nomes_digitados in range(3):
    # nomes_digitados = input("Insira um nome: ")
    # nomes.append(nomes_digitados)
    # nomes.sort()
# for nomes_organizados in nomes:
    # print(nomes_organizados)
"""





