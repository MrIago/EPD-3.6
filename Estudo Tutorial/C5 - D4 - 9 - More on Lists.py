e = 0 # com o exemplo comçando por 0


def n(descricao=''): 

    global e
    e += 1
    print('.'*77)
    print()
    print('.'*77)
    print('%iº EXEMPLO: %s' %(e,descricao))
    
# O tipos List possuem mais alguns métodos

l = [1,2,3]
p = lambda: print(l)
p()

n('append(x)')
# Add an item to the end of the list
l.append(4)
p()

# Equivalente a[len(a):] = [x].
l[len(l):] = [5]
p()


n('extend(iteravel)')
# Extend the list by appending
# all the items from the iterable.
l.extend([6,7])
p()

# Equivalente a[len(a):] = iteravel
l[len(l):] = [8,9]
p()


n('insert(inidice, valor)')
# Insert an item at a given position.

l.insert(0,0)
# insere 0 no inicio
p()

l.insert(len(l), 10)
# insere 10 no fim
# equivalente a l.append()
p()


n('remove(valor)')
# Remove the first item from
# the list whose value is x.
# It is an error if there is no such item.

l.insert(0,-1)
p()

l.remove(-1)
p()


n('pop([i])')
# remove o item na posição i
# retorna um valor
# [i] - opicional
# caso não tenha argumentos
# remove o ultimo

l.pop(0)
p()

l.pop()
p()

n('clear()')
# Remove all items from the list.
# Equivalent to del a[:].

l.clear()
p()

l = list(range(10))
p()

del l[:]
p()


n('index(x[, start[, end ] ])')
# Return zero-based index in the list
# of the first item whose value is x.
# Raises a ValueError if there is no such item.


l = list(range(1,11))
p()

print(l.index(8))


n('count(item)')
# Return the number of times
# x appears in the list.

l = "Iago Lima Toledo"

print(l.count('o'))




n('sort(key=None, reverse=False)')
# Sort the items of the list in place

l = 'aoIg'
p()
l = list(l)
p()

l.sort()
p()

print()

nn = [0,6,7,9,8,5,4,2,3,1]
print(nn)

nn.sort()
print(nn)

nn.sort(reverse=True)
print(nn)



n('converter para string')

l = ''.join(l)
p()


n('ou converter para str e retirar []')

l = [1,2,3]
p()

# no caso de numero
l = str(l)
p()
l = l.strip("[]")
p()


n('ou usando os métodos split')

l = list("Iago")
p()

l = str(l)[1:-1]
# string a partir da 1 posição ate a última
p()


n('Ou juntar tudo')

l = list("Iago")
p()

l = ''.join(map(str,l))
p()


n('reverse()')
# Reverse the elements of the list in place.

nn.sort()
print(nn)
nn.reverse()
print(nn)


l = 'Paralelepípedo'
p()

l = list(l)
l.reverse()
l = ''.join(l)
p()


print('\n\nMAIS EXEMPLOS\n\n')

n('An example that uses most of the list methods:')
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
p = lambda: print(fruits)
p()


n("fruits.count('apple')")
print(fruits.count('apple'))

n("fruits.count('tangerine')")
print(fruits.count('tangerine'))

n("fruits.index('banana')")
print(fruits.index('banana'))


n("fruits.index('banana', 4)")
print(fruits.index('banana', 4))# Find next banana starting a position 4

n("fruits.reverse()")
fruits.reverse()
p()

n("fruits.append('grape')")
fruits.append('grape')
p()

n("fruits.sort()")
fruits.sort()
p()

n("fruits.pop()")
print(fruits.pop())




































