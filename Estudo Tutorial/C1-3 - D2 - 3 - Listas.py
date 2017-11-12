"""

list can be written as a list of comma-separated values (items) between square
brackets. Lists might contain items of different types, but usually the items
all have the same type.

>>> squares = [1, 4, 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]

"""

print('1 -')
notas_atp = [1, 3, 2.7, 'Z E R O']
print(notas_atp)


print()


"""

Like strings (and all other built-in sequence type), lists can be indexed and sliced:
>>> squares[0] # indexing returns the item
1
>>> squares[-1]
25
>>> squares[-3:] # slicing returns a new list
[9, 16, 25]
>>> squares[:]
[1, 4, 9, 16, 25]

"""
print('2 -')
print(notas_atp[0])



print()



"""

Lists also support operations like concatenation:
>>> squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

"""
print('3 -')
notas_atp += [0,0,0.7,0]
print(notas_atp)



print()



"""

Unlike strings, which are immutable, lists are a mutable
type, i.e. it is possible to change their content:

>>> cubes = [1, 8, 27, 65, 125] # something's wrong here
>>> 4 ** 3 # the cube of 4 is 64, not 65!
64
>>> cubes[3] = 64 # replace the wrong value
>>> cubes
[1, 8, 27, 64, 125]

is also possible to change the size of the list or clear it entirely:

>>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> # replace some values
>>> letters[2:5] = ['C', 'D', 'E']
>>> letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
>>> # now remove them
>>> letters[2:5] = []
>>> letters
['a', 'b', 'f', 'g']
>>> # clear the list by replacing all the elements with an empty list
>>> letters[:] = []
>>> letters
[]

"""
print('4 -')
print(notas_atp)
notas_atp[:] = []
print(notas_atp)



print()



"""

The built-in function len() also applies to lists:
>>> letters = ['a', 'b', 'c', 'd']
>>> len(letters)
4

"""
print('5 - ')
print(len([1,2,3,4,5,6,7]))



print()



"""

It is possible to nest lists (create lists containing other lists), for example:
>>> a = ['a', 'b', 'c']
>>> n = [1, 2, 3]
>>> x = [a, n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]
['a', 'b', 'c']
>>> x[0][1]
'b'

"""
print('6 -')
a = [1]
b = [2]
c = [a,b]
d = [a+b]
print(a)
print(b)
print(c)
print(d)
print(c[0][-1])



"""

adiciona s como o indice x e empurra pra frente o anterior
.insert(x, s)

deleta o valor do indice i da lista L
del(L[i])
deleta num intervalo
del(L[1:4])
del(L[::2])

limpa lista L
L.clear()


função pop() a mesma retornará e removerá o último elemento da lista.
Porém, se desejarmos um elemento em especifico, basta passarmos como
parâmetro o índice e então, o mesmo será retornado e excluído da lista.

L.pop()

"""
words = ['cat', 'window', 'defenestrate']
print(words)
words.insert(0,'dog') # 'dog' inserido no inicio
print(words)
del(words[0])
print(words)
print(words.pop(),'foi deletado')
print(words)
words.clear()
print(words)











