"""
Python’s for statement iterates over the items of any
sequence (a list or a string), in the order that they
appear in the sequence. For example (no pun intended):

"""
print('1 -\nMeasure some strings:')
words = ['cat', 'window', 'defenestrate']
for w in words:
    print('a string',w,'possui',len(w),'caracteres')


print()


"""
If you need to modify the sequence you are iterating over while inside the loop
(for example to duplicate selected items), it is recommended that you first
make a copy. Iterating over a sequence does not implicitly make a copy.
The slice notation makes this especially convenient:

With for w in words:, the example would attempt to create an infinite list, inserting defenestrate over and
over again.
>>> for w in words:
... if len(w) > 6:
... words.insert(0, w)
...
>>> words
['defenestrate','defenestrate',...]

"""
print('2 -\nPreventing infinite loop:')
words = ['cat', 'window', 'defenestrate']
for w in words[:]:
    print(w)
    if len(w) > 6:
        words.insert(0, w)
        print(words)


print()




"""

The range() Function
If you do need to iterate over a sequence of numbers,
the built-in function range() comes in handy. It
generates arithmetic progressions:

range(inicio, fim[intervalo aberto], passo)

c -> for(x = 1; x < 11; x++)
p -> for x in range(1,11)

"""
print('3','-')
print(list(range(1,11)))
print(list(range(10,-11,-1)))


print()



"""

To iterate over the indices of a sequence, you can combine
range() and len() as follows:

"""
print(4,chr(45))
vrau = ['Mary', 'had', 'a', 'little', 'lamb']
for indice in range(len(vrau)):
    print(indice, vrau[indice])


print()


"""

In most such cases, however, it is convenient to use the enumerate() function.

for indice, valor in enumerate(lista):
    print(indice, valor)

[(indice0, valor0),(indice1, valor1),...]
  indice, valor     indice   valor   ...

"""
print(5,''
      '-')
for indice, valor in enumerate(vrau):
    print(indice, valor)



print()



"""

A strange thing happens if you just print a range:
>>> print(range(10))
range(0, 10)


range() behaves as if it is a list, but in fact it isn’t.
It is an object which returns the successive items of the
desired sequence when you iterate over it
for statement is such an iterator.
The function list() is another; it creates lists from iterables:

"""
print(6,'\
-')
print(range(10))
print(list(range(10)))




print()



"""

break and continue Statements, and else Clauses on Loops

The break statement, like in C, breaks out of the
innermost enclosing for or while loop.

Loop statements may have an else clause;
it is executed when the loop terminates
through exhaustion of the list (with for)
or when the condition becomes false (with while),
but not when the loop is terminated by a break statement.

This is exemplified by the following loop,
which searches for prime numbers:

############## script resumido #################

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
        else:
            print(n, 'is a prime number')

############### mais resumido ##################

for n in range(2, 10):
    for x in range(2, n):
        if n % x != 0:
            print(n, 'is a prime number')
            
#################################################

"""
print(7,'-')
prime = []
for n in range(2, 10):
    print('n -',n)
    for x in range(2, n):
        print('x -',x)
        if n%x == 0:
            print(n,'dividiu por',x)
            print(n,'equals',x,'*',n//x)
            break
        else:
            print(n,'não dividiu por',x)
    else:
        print(n,'is a prime number')
        prime += [n]
print('Os primos encontrados no',range(2,10),'foram:',prime)


print()


"""

The continue statement, also borrowed from C,
continues with the next iteration of the loop:

"""
print(8,'-')
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num) # caso seja par nao printa


"""

pass Statements
The pass statement does nothing. It can be used when a statement is
required syntactically but the program
requires no action. For example:
>>> while True:
... pass # Busy-wait for keyboard interrupt (Ctrl+C)
...

This is commonly used for creating minimal classes:
>>> class MyEmptyClass:
... pass
...

Another place pass can be used is as a place-holder for a function or
conditional body when you are working
on new code, allowing you to keep thinking at a more abstract level.
The pass is silently ignored:
>>> def initlog(*args):
... pass # Remember to implement this!

"""

while(1):
    pass # ctrl+c para sair








