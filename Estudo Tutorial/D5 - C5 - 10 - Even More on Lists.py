e = 0

def n(*descricao:''):

    global e

    print('.'*77)
    
    print()

    print('.'*77)

    print()
    
    print('EXEMPLO %i - %s :' %(e, descricao))

    print()

    

    e += 1

n('USANDDO LISTA COMO PILHA')

# LAST IN FIRST OUT


pilha = [3, 4, 5]

p = lambda: print('pilha = ', pilha, '\n')

p()

pilha.append(6)

p()

pilha.pop()

p()


n('USANDO LISTA COMO FILA')

# FIRST IN FIRST OUT

# collections.deque

from collections import deque

f = lambda: print('fila = ', fila, '\n')

fila = deque(['Iago', 'João', 'Maria']) # torna uma fila

print(type(fila))

f()

fila.append('Jusesvaldo')

f()

fila.popleft()

f()

n('LIST COMPREHENSIONS')

l = [x**2 for x in range(1,11)]

print(l)

"""
Uma list comprehension consiste em colchetes
contendo uma expressão seguida de uma cláusula
for, e então zero ou mais cláusulas for ou if.
O resultado será uma nova lista resultante da
avaliação da expressão no contexto das cláusulas
for e if seguintes.
"""

vec = [-4, -2, 0, 2, 4]

print(vec)

# create a new list with the values doubled

print([x**2 for x in vec])

# filter the list to exclude negative numbers

print([x for x in vec if x>=0])

# apply a function to all the elements

import math

print([math.sqrt(x) for x in vec if x%2==0])

# call a method on each element

frutas = ['_maçã-', '-morango*', ' banana-', '-limão-_']

print(frutas)


print([x.strip('-' ' ' '*') for x in frutas])

# create a list of 2-tuples like (number, square)

# the tuple must be parenthesized, otherwise an error is raised

print([(x, x**2) for x in range(1, 11)])


# flatten a list using a listcomp with two 'for'

l = [[1,2], [3,4], [5,6,7]]

print([n for x in l for n in x])


# List comprehensions can contain complex expressions and nested functions:

from math import pi
print([str(round(pi, x)) for x in range(8)])


