"""
# TIPOS DE VARIÁVEIS
variavel_string = "Texto"
variavel_int = 1
variavel_float = 1.23
variavel_bool = True
print(variavel_string)
print(variavel_int)
print(variavel_float)
print(variavel_bool)
"""

"""
# OPERAÇÕES MATEMÁTICAS
adicao = 72+23
subtracao =108-204
multiplicacao = 108 * 0.5
divisao = 108 / 9
# Toda divisão e multiplicação resulta em float
exponenciacao = 2 ** 3
resto = 100 % 10
print(adicao)
print(subtracao)
print(multiplicacao)
print(divisao)
print(exponenciacao)
print(resto)
"""

"""
# CÁLCULO
valor_refeicao = 42.54
valor_taxa = valor_refeicao * 0.1
valor_total = valor_refeicao + valor_taxa
print("%.2f" % valor_total)
# "%.2f" % (variavel) define 2 casas depois da vírgula numa variável tipo float
"""

"""
variavel_string = "Computador"
primeira_letra = variavel_string[0]
segunda_letra = variavel_string[1]
print(primeira_letra)
print(segunda_letra)
# O Índice sempre começará pelo zero
quantidade_caracteres = len(variavel_string)
ultima_letra = variavel_string[quantidade_caracteres - 1]
print(quantidade_caracteres)
print(ultima_letra)
# len( ) conta a quantidade de caracteres de uma string
"""

"""
# String sempre entre aspas
string = "Panettone"
print(string.upper())
print(string.lower())
#OU
string2 = "Panettone".upper()
print(string2)
"""

"""
# Transformar variáveis em String > str()
nome = "Monica"
idade = 26
print(nome + " - " + str(idade))
# A variável idade, por ser um número inteiro, é classificada como int. Para concatená-la com o nome é preciso transforma-la em string
"""

"""
# Concatenação simples
nome = "Mônica"
sobrenome = "Rezende"
idade = 26
print(nome + " " + sobrenome + " tem " + str(idade) + " anos.")
# Lembrar de utilizar espaços
print(nome.upper() + " " + sobrenome.upper())
# Concatenação usando .format
print("{} {} tem {} anos.".format(nome, sobrenome, idade))
print("{0} {1} tem {2} anos.".format(nome, sobrenome, idade))
# \n para pular linha e \t para 4 espaços
print("{0} {1}\ntem {2} anos.".format(nome, sobrenome, idade))
print("{0} {1}\n\ttem {2} anos.".format(nome, sobrenome, idade))
"""

# () > método ou função
# " " > string
"""
# OBTENDO INFORMAÇÕES DIGITADAS
nome = input("Insira seu nome: ")
sobrenome = input("Insira seu sobrenome: ")
print(nome + " " + sobrenome)
"""

"""
# IMPORTAR PACOTE DE DATA E HORA
from datetime import datetime
agora = datetime.now()
dia = agora.day
mes = agora.month
ano = agora.year
print("{}/{}/{}".format(dia,mes,ano))
print("{1}/{0}/{2}".format(dia,mes,ano))
# Para delimitar o número de caracteres {02d}
print("{:02d}/{:02d}/{:04d}".format(dia,mes,ano))

hora = agora.hour
minuto = agora.minute
segundo = agora.second
print("{:02d}/{:02d}/{:04d} - {}:{}'{}\"".format(dia,mes,ano,hora,minuto,segundo))
# Colocar \ antes de "" faz com que ele não entenda como um código, e sim uma string
"""

# Exercícios 1 a 4 em https://paulosalvatore.github.io/exercicios_python/

"""
from datetime import datetime

dia_nascimento = int(input("Informe o seu dia do nascimento: "))
mes_nascimento = int(input("Informe o seu mês de nascimento: "))
ano_nascimento = int(input("Informe seu ano de nascimento: "))
data_nascimento = datetime(ano_nascimento, mes_nascimento, dia_nascimento)
print(data_nascimento)
data_agora = datetime.now()
diferenca_datas_dias = data_agora - data_nascimento
print(diferenca_datas_dias)
# Para calcular a diferença em segundos, multiplicar por 24(horas)*60(minutos)*60(segundos)
diferenca_datas_seg = diferenca_datas_dias.days * 24 * 60 * 60 + diferenca_datas_dias.seconds
print(diferenca_datas_seg)
"""

"""
#EXERCÍCIO 4
data_agora = datetime.now()
print(data_agora)
ano_agora = data_agora.year
mes_agora = data_agora.month
dia_agora = data_agora.day
hora_agora = data_agora.hour
minuto_agora = data_agora.minute
segundo_agora = data_agora.second
print("{}/{}/{} - {}h{}'{}\"".format(ano_agora, mes_agora, dia_agora, hora_agora, minuto_agora, segundo_agora))

dia_nascimento = int(input("Informe o dia do seu nascimento: "))
mes_nascimento = int(input("Informe o mês do seu nascimmento: "))
ano_nascimento = int(input("Informe o ano do seu nascimento: "))
data_nascimento = datetime(ano_nascimento,mes_nascimento,dia_nascimento)
dia_semana = datetime.weekday(data_nascimento)
print("{:02d}/{}/{} - Dia da semana: {}".format(dia_nascimento, mes_nascimento, ano_nascimento, dia_semana))

diferenca_datas = data_agora - data_nascimento
print(diferenca_datas.days)
"""

"""
# EXERCÍCIO 1
a = 7
b = 12
resultado = a + b
print(resultado)

subtracao = a - b
multiplicacao = a * b
divisao = a / b
exponenciacao = a ** b
resto = a % b

print(subtracao)
print(multiplicacao)
print(divisao)
print(exponenciacao)
print(resto)
"""

"""
# EXERCÍCIO 2
total_conta = 82.57
valor_pago = 100
troco = valor_pago - total_conta
print(troco)
print("%.2f" % troco)
print("O total da conta foi de R${:.2f}, você pagou R${:.2f} e o seu troco foi de R${:.2f}.".format(total_conta, valor_pago, troco))
# Não consegui fazer o troco ficar com apenas 2 casas depois da vírgula
"""

"""
# EXERCÍCIO 3
nome = input("Insira seu nome: ")
idade = int(input("Informe quantos anos você tem: "))
genero = input("Informe seu gênero: ")
aniv = idade + 1
print("Olá, {}, você possui {} anos de idade e é do gênero {}. Já pensou no que fará no seu aniversário de {} anos?".format(nome, idade, genero, aniv))
# Quando for utilizar um input de número, colocar a função int() primeiro.
"""

"""
# Uma catapulta lançou 300 pedras em 5 baterias de 15 minutos, cada. Quantas pedras ela lançaria em 8 baterias de 7 minutos, cada?
# Crie um programa que recebe os valores base para que a aplicação funcione de forma que, se alterarmos o número de baterias e a duração de cada bateria, o programa funciona sem precisar de mais modificações.

pedra_por_min = (300 / 5)/ 15
#print(pedra_por_min)
pedras2 = 8 * 7 * 4
#print(pedras2)

baterias = int(input("Informe a quantidade de baterias: "))
minutos = int(input("Informe quantos minutos terá cada bateria: "))
qtde_pedras = baterias * minutos * 4

print("A catapulta lançou {} pedras em {} baterias de {} minutos cada.".format(qtde_pedras, baterias, minutos))
"""

"""
# Escreva um programa que receba um número e arredonde ele para o múltiplo de 10.
# Exemplo: Se receber o número 22, arredonda para 20
# Se receber o número 79, arredonda para 70

numero = int(input("Insira um número: "))
resto = numero % 10
multiplo = numero - resto
print("Recebido o número {}, ele é arredondado para {}.".format(numero, multiplo))
"""

"""
# Igual a ==
# Diferente de !=
# Menor que <
# Menor ou igual a <=
# Maior que >
# Maior ou igual a >=

# Usar === para saber se é o tipo também é igual (int, str ou float)

print(646 > (45 * 3))
print("abc" == "abc")
print("abc" != "abc")
print(45 != 76)
print(3 < 2)

# NO PHP E OUTRAS LINGUAGENS >> AND = && e OR = || e NOT = !

NOT >> inverte o resultado do bool
"""

"""
print(not(not(True)))
# True
print(not True != (not False) or True == False)
# True
print(True == False and True)
# False
print(True != (not(not False)) and True)
# True
print(True or False or False)
# True
print(False or True and True and False)
# False

# NOT é feito primeiro, AND em seguida e, por fim, OR. Sempre usar parentesis!
"""


# IF, ELIF (elseif - caso contrário SE) e ELSE (caso contrário - todas demais condições)
# IF só é usado uma vez, sendo o primeiro sempre. o ELIF pode ser usado quantas vezes necessário, e o ELSE é usado uma só vez, como último sempre)

"""
variavel_booleana = True
if variavel_booleana:
    print("Esse código será lido.")
else:
    print("Esse código nunca será lido")
"""

"""
string = input("Escolha entre uma arma medieval ou futurista: ")
if string == "medieval":
    print("espada")
elif string == "futurista":
    print("sabre de luz")
else:
    print("Tente novamente.")
"""

"""
numero = int(input("Insira um número: "))
if numero > 10:
    print("O numero {} é maior do que 10.".format(numero))
elif numero < 10:
    print("O número {} é menor que 10.".format(numero))
else:
    print("O número {} é igual a 10.".format(numero))
"""

"""
numero1 = int(input("Escolha um número inteiro: "))
numero2 = int(input("Escolha mais um número inteiro: "))
resto = numero1 % numero2
if resto == 0:
    print("O número {} é múltiplo de {}.".format(numero2, numero1))
else:
    print("O número {} não é múltiplo de {}.".format(numero2, numero1))
"""

"""
numero = int(input("Escolha um número: "))
if numero % 2 == 0:
    print("O número {} é par.".format(numero))
else:
    print("O número {} é impar.".format(numero))
"""

"""
nome = input("Qual seu nome? ")
if nome[0] == "A":
    print("A de amor")
elif nome[0] == "B":
    print("B de Baixinho")
else:
    print("Seu nome não é legal :(")
"""

"""
idade = int(input("Informe a sua idade: "))
if idade < 16:
    print("Você ainda não pode votar.")
else:
    zona = input("Informe a zona em que você mora: ").lower()
    if zona == "oeste" or "norte":
        print("Se você é morador da {}, seu local de votação é a Escola A".format(zona))
    elif zona == "leste":
        print("Se você é morador da {}, seu local de votação é a Escola B".format(zona))
    elif zona == "sul" or "centro":
        print("Se você é morador da {}, seu local de votação é a Escola C".format(zona))
"""

# Exercícios de lógica: https://wordpad.cc/logica-carro-poker

# https://docs.google.com/presentation/d/1FFMtflEGOG56rQift6FMfrxY0fUDLXQpAuZGZw5ba_U/edit

"""
# def para definir funções
def exibirMensagem():
    print("Essa mensagem irá ser exibida.")

exibirMensagem()
"""
"""
def exibirMensagem(numero):
    print("O número é {}.".format(numero))

exibirMensagem(5)
"""

# import math

"""
def calcular_bhaskara(a, b, c):
    delta = (b ** 2) - (4 * a * c)
    print("O valor de delta é {}.".format(delta))

    if delta >= 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        print("O valor de x1 é {}.".format(x1))

        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("O valor de x2 é {}.".format(x2))

    else:
        print("Delta menor que 0.")

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

calcular_bhaskara(a, b, c)
"""

# EXERCICIO 1: f(x) = 3x - 2. Determine o valor de f(5) + f(0):

"""
def calcular_funcao(equacao):

    x = int(input("Digite um valor para a equação {}.".format(equacao)))

    resultado = 3 * x - 2
    print("O resultado da equação {} é {}.".format(equacao, resultado))


    return resultado


resultado1 = calcular_funcao(1)
resultado2 = calcular_funcao(2)
resultado3 = calcular_funcao(8)

print(resultado1 + resultado2)
"""

# EXERCÍCIO 2: Na produção de peças, uma fábrica tem um custo fixo de R$30,00 mais um custo variável de R$2,00 por unidade produzida. Sendo x o número de peças unitárias produzidas, determine o custo de produção de 100 peças:

"""
def calcular_producao():
    custo_fixo = int(input("Qual é o custo fixo da produção? "))
    custo_variavel = int(input("Qual é o custo varíavel da produção? "))
    pecas = int(input("Quantas peças foram produzidas? "))

    producao = custo_fixo + (custo_variavel * pecas)

    print("A um custo fixo de R${:.2f} e custo varíavel de R${:.2f}, o custo de produção de {} peças é R${:.2f}.".format(custo_fixo, custo_variavel, pecas, producao))


calcular_producao()
"""

# EXERCÍCIO 3: Crie uma função que receba 2 números e retorne o valor maior.
# EXERCÍCIO 4: Crie uma função que receba 3 números e retorna o maior valor, use a função da questão 3.

"""
def checar_maior(a, b):
    if a > b:
        return a
    else:
        return b


numero1 = int(input("Digite um número 1: "))
numero2 = int(input("Digite um número 2: "))
numero3 = int(input("Digite um número 3: "))

maior = checar_maior(numero1, numero2)
maior = checar_maior(maior, numero3)
print(maior)
"""
"""
# EXERCÍCIO 5: Dadas as funções f(x) = x - 5 e g(x) = 3x + 1, o valor da soma de f(9) + g(2) é:


def equacao():
    variavel_f = int(input("Digite um valor para a função f: "))
    variavel_g = int(input("Digite um valor para a função g: "))
    funcao_f = variavel_f - 5
    funcao_g = 3 * variavel_g + 1
    resultado = funcao_f + funcao_g
    print("O resultado da equação f(9) + g(2) é {}.".format(resultado))

equacao()

# REFAZER UTILIZANDO return
"""
"""
# EXERCÍCIO 6: Considere as seguintes funções: f(x) = x-4 e g(x)=5x-1. Qual é o valor da função composta g(f(3))?


def funcao_f(x):
    return x - 4


def funcao_g(x):
    return 5 * x - 1


x = int(input("Escolha um valor para x: "))
resultado1 = funcao_g(funcao_f(x))
print(resultado1)
"""
"""
# EXERCÍCIO 7: Crie uma função chamada dado() que retorna, através de sorteio, um número de 1 até 6.
# Exiba 10 números sorteados utilizando a mesma função criada.
# Números aleatórios: random.randint(inicio, fim)

import random

def dado():
    return random.randint(1, 6)


print("O número sorteado é {}.".format(dado()))
print("O número sorteado é {}.".format(dado()))
print("O número sorteado é {}.".format(dado()))
print("O número sorteado é {}.".format(dado()))
print("O número sorteado é {}.".format(dado()))
print("O número sorteado é {}.".format(dado()))
print("O número sorteado é {}.".format(dado()))
print("O número sorteado é {}.".format(dado()))
print("O número sorteado é {}.".format(dado()))
print("O número sorteado é {}.".format(dado()))
"""
"""
# EXERCICIO 8: Crie um aplicativo de conversão entre as temperaturas Celsius e Farenheit. Primeiro o usuário deve escolher se vai entrar com a temperatura em Celsius ou Farenheit, depois a conversão escolhida é realizada.
# Se C é a temperatura em Celsius e F em Farenheit, as fórmulas de conversão são:
# C = 5 * (F - 32) / 9
# F = (9 * C / 5) + 32


def transformar_celsius(F):
    return 5 * (F - 32) / 9


def transformar_farenheit(C):
    return (9 * C / 5) + 32


escolha_usuario = input("Você deseja inserir uma temperatura em Celsius ou Farenheit? ")
if escolha_usuario == "Celsius":
    c = float(input("Informe sua tempera em Celsius: "))
    resultado1 = transformar_celsius(c)
    print("Para essa temperatura em Celsius, o valor em Farenheit é {}.".format(resultado1))
elif escolha_usuario == "Farenheit":
    f = float(input("Informe sua temperatura em Farenheit: "))
    resultado2 = transformar_farenheit(f)
    print("Para essa temperatura em Farenheit, o valor em Celsius é {}.".format(resultado2))
else:
    print("Tente novamente.")
"""
"""
# EXERCÍCIO 9: Um professor, muito legal, fez 3 provas durante um semestre mas só vai levar em conta as duas notas mais altas para calcular a média.
# Faça uma aplicação em C que peça o valor das 3 notas, mostre como seria a média com essas 3 provas, a média com as 2 notas mais altas, bem como sua nota mais alta e sua nota mais baixa. (http://www.cprogressivo.net/2013/03/Exercicios-sobre-funcoes-em-linguagem-de-programacao-C.html)


def nota1(a, b, c):
    return (a + b + c) / 3


def nota2(a, b):
    return (a + b) / 2


def maior(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c


def menor(a, b, c):
    if a < b and a < c:
        return a
    elif b < c:
        return b
    else:
        return c


def segunda_maior(a, b, c):
    if a < b < c or c < b < a:
        return b
    elif b < a < c or c < a < b:
        return a
    else:
        return c


prova1 = float(input("Insira a nota da P1: "))
prova2 = float(input("Insira a nota da P2: "))
prova3 = float(input("Insira a nota da P3: "))

media1 = nota1(prova1, prova2, prova3)
print("A média das provas, considerando as três notas, é {:.2f}.".format(media1))

media3 = nota2(maior(prova1, prova2, prova3), menor(prova1, prova2, prova3))
print("A média das provas, considerando apenas a maior e a menor nota, é {:.2f}.".format(media3))

media2 = nota2(maior(prova1, prova2, prova3), segunda_maior(prova1, prova2, prova3))
print("A média das provas, considerando apenas as duas notas mais altas, é {:.2f}.".format(media2))
print("Portanto, a nota final é {}!".format(media2))

"""


# Crie uma função que receba um número como parâmetro e aplique esse número na fórmula abaixo e exiba o resultado no console: numero ** 2 + (numero % 10)

"""
def funcao(n):
    return n ** 2 + (n % 10)


n = int(input("Insira um número: "))
numero = funcao(n)
print(numero)
"""

"""
def potencia(base, expoente):
    resultado = base ** expoente
    print("{} elevado a {} é {}.".format(base, expoente, resultado))


potencia(2, 3)
"""

"""
def somar_um(n):
    return n + 1


def somar_dois(n):
    return somar_um(n) + 2


numero = int(input("Insira um número: "))
resultado1 = somar_um(numero)
resultado2 = somar_dois(numero)
print(resultado1)
print(resultado2)
"""
"""
import math
raiz = math.sqrt(6)
print(raiz)
# help(math)

# OU
from math import sqrt
print(sqrt(n))

# OU
import math as matematica
print(matematica.sqrt(50))
"""

"""
# Para que a função aceite uma quantidade indefinida de argumentos
def nome_funcao(*args):
    print(args)


nome_funcao(1, 2, 3, 4)
"""

# FUNÇÕES MAX E MIN

"""
def nome_funcao(*args):
    print("Args recebidos: {}.".format(args))
    maior = max(args)
    print("Maior número: {}".format(maior))
    menor = min(args)
    print("Menor número: {}".format(menor))


nome_funcao(1, 2, 3, 4, 5, 6)
"""
"""
# FUNCAO ABS: retorna a distância entre um número e zero
numero = -10
abs_n = abs(numero)
print(abs_n)
"""
"""
# FUNÇÃO TYPE: Para saber qual é o tipo do argumento (int, bool, string ou float)
print(type("Paulo"))
print(type(1))
print(type(1.0))
print(type(True))

vouf = bool(input("Insira V para Verdadeiro e F para Falso: "))
print(type(vouf))

numero = 1
if type(numero) == float:
    print("O número é um float.")
else:
    print("O número não é um float.")
"""

"""
def custo_hotel(noites):
    return noites * 140


def custo_aviao(cidade):
    if cidade == "São Paulo":
        return 312.00
    elif cidade == "Porto Alegre":
        return 447.00
    elif cidade == "Recife":
        return 831.00
    elif cidade == "Manaus":
        return 986.00
    else:
        print("A cidade escolhida não está entre as opções disponíveis. Tente novamente.")


def custo_carro(dias):
    if dias >= 7:
        return (dias * 40) - 50
    elif dias >= 3:
        return (dias * 40) - 20
    else:
        return dias * 40

# OUTRA MANEIRA
# def custo_carro(dias):
    # custo = dias * 40
        # if dias >= 7:
            # return custo -= 50
        # elif dias >= 3:
            # return custo -= 20
    # return custo


def custo_total(noites, cidade, dias, extras):
    return custo_hotel(noites) + custo_aviao(cidade) + custo_carro(dias) + extras


noites = int(input("Por quantas noites pretende ficar hospedado? "))
var_custo_hotel = custo_hotel(noites)
print("O custo de sua estadia para {} noites é de R${:.2f}.".format(noites, var_custo_hotel))
cidade = input("Insira o nome da sua cidade de destino: ")
var_custo_aviao = custo_aviao(cidade)
print("O custo de passagem para o seu destino é R${:.2f}.".format(var_custo_aviao))
dias = int(input("Por quantos dias pretende utilizar o carro alugado: "))
var_custo_carro = custo_carro(dias)
print("O custo de aluguel do carro por {} dias é de R${:.2f}.".format(dias, var_custo_carro))
extras = int(input("Defina um valor para gastos extras: "))
var_custo_total = custo_total(noites, cidade, dias, extras)
print("O custo total da sua viagem é de R${:.2f}.".format(var_custo_total))
"""





























