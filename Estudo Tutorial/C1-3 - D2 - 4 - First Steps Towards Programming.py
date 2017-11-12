"""

Of course, we can use Python for more complicated tasks than adding two
and two together. For instance, we can write an initial sub-sequence of
the Fibonacci series as follows:

"""
print(1,'-')
print('Fibonacci series:')
# the sum of two elements defines the next
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b



print()



"""

NOVOS CONCEITOS

1 - Atribuição múltipla

a,b = 0,1
a = 0
b = 1
a,b = a+b,a+b
a,b = (1, 1) -> direita para esquerda


2 - while(condição)

while(0) -> false

while(anything not null) -> true

The standard comparison operators
are written the same as in C:
< (less than),
> (greater than),
== (equal to),
<= (less than or equal to),
>= (greater than or equal to)
!= (not equal to).

3 - identação

blocos separados por TAB

4 - print()

Strings are printed without quotes, and a
space is inserted between items, so you can
format things nicely, like this:

>>> i = 256*256
>>> print('The value of i is', i)
The value of i is 65536


The keyword argument end can be used to avoid the
newline after the output, or end the output with
a different string:

>>> a, b = 0, 1
>>> while b < 1000:
... print(b, end=',')
... a, b = b, a+b
...
1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,


"""
print(2,'-')
a = 1
while(a<10):
    print(a, end=' < ')
    a += 1
print(a)
