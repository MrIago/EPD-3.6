# Aproveitando o conhecimento atual de função, já podemos criar uma função para
# dizer automaticamente o número do exemplo:
# None - NADA - VAZIO - OPERADOR NULO - QUE NÃO FAZ NADA

e = 0 # com o exemplo comçando por 0


def n(descricao=''): 

    global e
    e += 1
    print('.'*77)
    print()
    print('.'*77)
    print('%iº EXEMPLO: %s' %(e,descricao))
    

n('Essa é uma descrição opcional')

# Uma função não modifica o valor de uma variavel
# A não ser que você defina na função, que a variável será manipulada globalmente



n('Expressão Lambda')

# Função Lambda
# Pequena função anônima
# É restrita sintaticamente a uma única expressão

# É útil pra casos de função como conhecemos na matemática -> f(x) = ...


f = lambda x,a=1,b=0,c=0: print('f(%s) = %s*(%s)²+%s*(%s)+(%s) = %s' %(str(x), str(a),str(x), str(b), str(x), str(c), str((a*((x)**2))+b*x+c)))

f(2)


n('Um pouco mais simples')

dobro = lambda y : print(2*y)
dobro(2)


n('Podemos usar uma expressão lambda como retorno de uma função')

def adiciona(n):
    return lambda x: print(x+n)

num = adiciona(1)

num(2)
num(3)


# Mas ainda parece meio confuso
# Então vamos ver outras funções, para depois voltar ao lambda com alguma utilidade visível


n('Função Map')

# Essa função, em Python, serve para aplicarmos uma função a cada elemento de uma lista,
# retornando uma nova lista contendo os elementos resultantes da aplicação da função.

import math

def pot(x):
    return x**2


L = [1,4,9,16,25]
print(L)

L = list(map(math.sqrt, L))
print(L)

L = list(map(pot, L))
print(L)

n('List comprehensions')

# A  função map pode ser facilmente substituída por um list comprehension

L = [math.sqrt(x) for x in L]
print(L)


L = [math.pow(x,2) for x in L]
print(L)


"""

n('Função Reduce')

# está disponível no módulo functools
# é outra meio inútil
# Sua utilidade está na aplicação de uma
# função a todos os valores do conjunto, de forma a agregá-los todos em um único valor.

import functools

import operator #necessário para obter a função de soma
valores = [1, 2, 3, 4, 5]
soma = reduce(operator.add, valores)
print(soma)

"""

n('Função sum()')

# É claro que, para realizar a soma de todos os elementos
# de uma sequência, é muito mais claro utilizarmos a função sum():

valores = [1, 2, 3, 4, 5]
print (sum(valores))



n('Função Filter')
"""

Como o próprio nome já deixa claro, filter() filtra os elementos de
uma sequência. O processo de filtragem é definido a partir de uma
função que o programador passa como primeiro argumento da função.
Assim, filter() só “deixa passar” para a sequência resultante aqueles
elementos para os quais a chamada da função que o usuário passou retornar True. 


"""

valores = [10, 4, -1, 3, 5, -9, -11]
print('Lista antes:', valores)

def mqz(x):
    return x>0

valores  =  list(filter(mqz, valores))

print('Lista depois:', valores)


n('Lista comprehension 2.0')
# Assim, como no exemplo da builtin map(),
# aqui também podemos escrever com facilidade uma
# comprehension com a mesma funcionalidade:


valores = [10, 4, -1, 3, 5, -9, -11]
print('Lista antes:', valores)

valores  =  [x for x in valores if x>0]
print('Lista depois:', valores)



n('Continuação Lambda')

print("""
No exemplo da função filter(), tivemos que definir uma
nova função (chamada maior_que_zero) para usar somente
dentro da função filter(), sendo chamada uma vez para cada
elemento. Ao invés de definir uma nova função dessa forma,
poderíamos definir uma função válida somente enquanto durar
a execução do filter. Não é necessário nem dar um nome a tal
função, sendo portanto chamada de função anônima ou função lambda
""")


valores = [10, 4, -1, 3, 5, -9, -11]
print('Lista antes:', valores)



valores  =  list(filter(lambda x: x>0, valores))
print('Lista depois:', valores)

print("""
Definimos uma função anônima (portanto, não tem nome),
que recebe uma entrada (a variável x) e retorna o
resultado da operação x > 0, True ou False.
""")






