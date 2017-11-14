############################### F U N Ç Õ E S ###################################

# The keyword def introduces a function definition. It must be followed by the
# function name and the parenthesized list of formal parameters. The statements
# that form the body of the function start at the next line, and must be indented.
# The first statement of the function body can optionally be a string literal;
# this string literal is the function’s documentation string, or docstring.
# it’s good practice to include docstrings in code that you write,
# so make a habit of it.

# para acessar a doc de funções basta digitar no sheel ou printar
# nome_funcao.__doc__

#################################################################################

# We can create a function that writes the Fibonacci series to an arbitrary boundary:
def fib(n): # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b



# Now call the function we just defined:

print(1,'-')
print(fib(7777)) # Toda função retorna um valor, caso vazio, retorna None <built-in Name>

print()
print(2,'-') # Você pode atribuir um nome a uma função e chama-la por esse nome:

print(range) # mostra o tipo
r = range
print(r)
print(r(10))  # chama a função print

print()
print(3,'-') # podemos com isso "criar uma função" para pular linha por exemplo

print(print) # mostra o tipo
p = print
print(p) # chama a função print e mostra o tipo de p

p()
print(4,'-') # E como agora funciona como função print podemos passar os parametros
p('Essa é uma cópia da função print!')

p() # + pra frente vamos melhorar essa função
print(5,'-') # pra n precisar fazer isso

# It is simple to write a function that returns a list of the numbers of the
# Fibonacci series, instead of printing it:

def fib2(n): # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a) # see below
        a, b = b, a+b
    return result

f7777 = fib2(7777) # call it
print(f7777) # write the result

# result.append(a) calls a method of the list object result.
# A method is a function that‘belongs’ to an object and is named obj.methodname.
# The method append() shown in the example is defined for list objects;
# it adds a new element at the end of the list.
# In this example it is equivalent to result = result + [a], but more efficient.



"""

More on Defining Functions

It is also possible to define
functions with a variable
number of arguments.
There are three forms,
which
can be combined.

"""



# 1 - Argumentos com valores padrão
p()
print(6,'-')

"""

The most useful form is to specify a default value for one or more arguments.
This creates a function that can be called with fewer arguments than it is
defined to allow. For example:

"""

def pot(n, exp=2, repete=1):

    if n in (0,1): print('FALA SERIO NEH MERMAO!')
    else:
        while True:
            print(n,'elevado a',exp,'=',pow(n,exp))
            repete -= 1
            if repete == 0: return False
            else: exp += 1

pot(0)
p()
pot(1)
p()
pot(2)
p()
pot(2,3)
p()
pot(2,4,3)

# This example also introduces the in keyword.
# This tests whether or not a sequence contains a certain value.

print('Iago' in ['Lucas','João','Thiago','Iago']) # retorna True se tiver





p()
print(7,'-')
# The default values are evaluated at the point of function definition
# in the defining scope, so that

i = 5

def f(arg=i):
    print(arg)
    i = 6

i = 7

f()

# will print 5.


p()
print(8,'-')
"""
Important warning: The default value is evaluated only once.
This makes a difference when the default is a
mutable object such as a list, dictionary, or instances of
most classes. For example, the following function
accumulates the arguments passed to it on subsequent calls:
"""
def f(a, l=[]):
    l.append(a)
    return l
print(f(1),f(2),f(3))

"""

If you don’t want the default to be shared between subsequent calls,
you can write the function like this instead:

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

"""



#2 - Keyword Arguments

# Functions can also be
# called using keyword arguments
# of the form kwarg=value.

def ex(o, e1='e1', e2=2):
    print(o,e1,e2)

p()
print(9,'-')
ex(1)
ex(1,'ex1')
ex(1,'ex1',2.2) # argumentos posicionais

ex(1, e2=2.22)
ex(1, e2=2.222, e1='exx1') # 1 posicional e 2 keywords


# ex() precisa de 1 arg
# ex(e3='e3') não existe
# parrot(e2=2.2222, 1) # non-keyword argument after a keyword argument
# parrot(1, 0=1.1) # duplicate value for the same argument


# Regrinha: posicionais > keywords



# (posicionais, *arguments, **keywords)

# * quantos quiser
# ** dicionario -> chave = valor

# * < **



p()
print(10,'-')

def musicas(nome_do_album, *musicas, **estilos):

    print(nome_do_album)
    print('-'*len(nome_do_album))

    for m in musicas:

        print(m,':',estilos[m])

musicas('Ou, ou, ou mai God', 'Dididididie', 'tananana', Dididididie = 'Classico', tananana = 'Soul')
        

"""
Note that the order in which the
keyword arguments are printed is
guaranteed to match the order in which
they were provided in the function call.
"""

#3 - Arbitrary Argument Lists

# Finally, the least frequently used option
# is to specify that a function can be called
# with an arbitrary number of arguments.

p()
print(11,'-')

def lista(nome,*args,sep='|'):
    nome = sep.join(args)
    l = (sep+nome+sep)
    return l

minha_lista_1 = (lista('Lista 1',
            'chocolate',
            'travesseiro',
            'pescaria',
            'Os Feiticeiros de Waverly Place'))

minha_lista_2 = (lista('Lista 2',
                       'a',
                       'gg easy',
                       'percentual',
                       'reforma trabalhista',
                       sep='::'))

print(minha_lista_1)
print(minha_lista_2)



# Unpacking Argument Lists

p()
print(12,'-')

print(list(range(1,11))) # normal call with separate arguments

args = [1,11]

print(list(range(*args))) # call with arguments unpacked from a list


p()
print(12,'-')

# In the same fashion, dictionaries can deliver
# keyword arguments with the **-operator

def pessoa(nome, idade = 17, nas = '00/00/00'):

    print(nome, idade, nas)

pessoa('Iago',nas = '11/09/2000')


p = {'nome': 'Iago', 'idade': 17, 'nas': '11/09/2000'}

pessoa(**p)
















