def criar_planeta(nome, bioma, /, alinhamento_politico):
    print(nome, bioma, alinhamento_politico)

criar_planeta('Tatooine', 'Deserto', 'Neutro')



def criar_planeta(*, nome, bioma, alinhamento_politico):
    print(nome, bioma, alinhamento_politico)

criar_planeta(nome='Tatooine', bioma='Deserto', alinhamento_politico='Neutro')

#funções são objetos de primeira classe, ou seja, podem ser passadas como argumentos para outras funções

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado(funcao, a, b):
    print(funcao(a, b))

exibir_resultado(somar, 10, 5)
exibir_resultado(subtrair, 10, 5)

#Há escopo local e global, como em outras linguagens
#global é uma palavra reservada que permite que uma variável seja acessada em qualquer lugar do código
#Utilizar global não é uma boa prática