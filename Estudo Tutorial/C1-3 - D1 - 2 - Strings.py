print("9 -")
"""

3.1.2 Strings
Besides numbers, Python can also manipulate strings, which can be
expressed in several ways. They can be enclosed in single quotes ('...')
or double quotes ("...") with the same result2. \ can be used to escape quotes:

>>> 'vrau shablau' # single quotes
'vrau shablau'
>>> 'doesn\'t' # use \' to escape the single quote...
"doesn't"
>>> "doesn't" # ...or use double quotes instead
"doesn't"
>>> '"Yes," he said.'
'"Yes," he said.'
>>> "\"Yes,\" he said."
'"Yes," he said.'
>>> '"Isn\'t," she said.'
'"Isn\'t," she said.'

"""

print('Iago\'s hot')
print("Iago's hot dog")


print()


print("10 -")
"""

The print() function produces a more readable
output, by omitting the enclosing quotes and
by printing escaped and special characters:

>>> '"Isn\'t," she said.'
'"Isn\'t," she said.'

>>> print('"Isn\'t," she said.')
"Isn't," she said.

>>> s = 'First line.\nSecond line.' # \n means newline

>>> s # without print(), \n is included in the output
'First line.\nSecond line.'

>>> print(s) # with print(), \n produces a new line
First line.
Second line.

"""

a = 'Iago\nLima'
print(a)

print()


print("11 -")
"""

If you don’t want characters prefaced by \ to be interpreted
as special characters, you can use raw strings
by adding an r before the first quote:

>>> print('C:\some\name') # here \n means newline!
C:\some
ame
>>> print(r'C:\some\name') # note the r before the quote
C:\some\name

"""

print('dezoito_Iagos\nove_Iagos = 2_Iagos')
print(r'dezoito_Iagos\nove_Iagos = 2_Iagos')


print()


print("12 -")
"""

String literals can span multiple lines. One way is using
triple-quotes: \"""...\""" or \'''...\'''. End of lines
are automatically included in the string, but it’s possible
to prevent this by adding a \ at the end of the line.

"""
print("""\
A+B = 10
A+A = B
A = 10-(A+A)
A = 10-2A \
-> 3A = 10
A = 10/3
B = 10-A \
 ->  B = 10-10/3
B = 20/3
""")


print()


print("13 -")
"""

Strings can be concatenated (glued together) with the + operator, and repeated with *:
>>> # 3 times 'un', followed by 'ium'
>>> 3 * 'un' + 'ium'
'unununium'

"""
i = 'Iago'
l = 'Lima'
print(7*i)
print(i+l)
print(7*i+l)


print()


print("14 -")
"""

Two or more string literals (i.e. the ones enclosed between quotes) next to each
other are automatically concatenated.
>>> 'Py' 'thon'
'Python'

This only works with two literals though, not with variables or expressions:
>>> prefix = 'Py'
>>> prefix 'thon' # can't concatenate a variable and a string literal
...
SyntaxError: invalid syntax
>>> ('un' * 3) 'ium'
...
SyntaxError: invalid syntax

"""
print('I' 'ago')


print()


print("15 -")
"""

If you want to concatenate variables or a variable and a literal, use +:
>>> prefix + 'thon'
'Python'

"""
print('Iago'+' '+l)


print()


print("16 -")
"""

This feature is particularly useful when you want to break long strings:
>>> text = ('Put several strings within parentheses '
... 'to have them joined together.')
>>> text
'Put several strings within parentheses to have them joined together.'

"""
nome = ('Iago '
        'Lima '
        'Toledo')
print(nome)


print()


print("17 -")
"""

Strings can be indexed (subscripted), with the first character having index 0. There is no separate character
type; a character is simply a string of size one:
>>> word = 'Python'
>>> word[0] # character in position 0
'P'
>>> word[5] # character in position 5
'n'

"""
print(i[0])


print()


print("18 -")
"""

Indices may also be negative numbers, to start counting from the right:
>>> word[-1] # last character
'n'
>>> word[-2] # second-last character
'o'
>>> word[-6]
'P'

Note that since -0 is the same as 0, negative indices start from -1.

"""
print(i[-1], i[-4])



print()


print("19 -")
"""

Note that since -0 is the same as 0, negative indices start from -1.
In addition to indexing, slicing is also supported. While indexing is
used to obtain individual characters, slicing allows you to obtain substring:
>>> word[0:2] # characters from position 0 (included) to 2 (excluded)
'Py'
>>> word[2:5] # characters from position 2 (included) to 5 (excluded)
'tho'

# print(list(nome))
# ['I', 'a', 'g', 'o', ' ', 'L', 'i', 'm', 'a', ' ', 'T', 'o', 'l', 'e', 'd', 'o']

for x in range(len(nome)):
    print("%d - %c" %(x, nome[x]))

0 - I
1 - a
2 - g
3 - o
4 -  
5 - L
6 - i
7 - m
8 - a
9 -  
10 - T
11 - o
12 - l
13 - e
14 - d
15 - o

# nome = list(enumerate("Iago Lima Toledo")) -> tupla

"""

print(nome)
f_name = nome[0:4]
m_name = nome[5:9]
l_name = nome[10:18]
print(f_name, m_name, l_name)


print()


print("20 -")
"""

Note how the start is always included, and the end always excluded.
This makes sure that s[:i] + s[i:] is always equal to s:
>>> word[:2] + word[2:]
'Python'
>>> word[:4] + word[4:]
'Python'

For non-negative indices, the length of a slice is the difference
of the indices, if both are within bounds. For example,
the length of word[1:3] is 2.

"""
print(i[:2], i[2:])
print(i[:2]+i[2:])


print()


print("21 -")
"""

Attempting to use an index that is too large will result in an error:
>>> word[42] # the word only has 6 characters
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
IndexError: string index out of range

However, out of range slice indexes are handled gracefully when used for slicing:
>>> word[4:42]'on'
>>> word[42:]
''

"""
print('|',i[2:777],'|', i[4:],'|')


print()


print("22 -")
"""

>>> word[0] = 'J'
...
TypeError: 'str' object does not support item assignment
>>> word[2:] = 'py'
...
TypeError: 'str' object does not support item assignment
If you need a different string, you should create a new one:
>>> 'J' + word[1:]
'Jython'
>>> word[:2] + 'py'
'Pypy'

"""
print(nome)
nome = 'Kaio '+nome[5:]
print(nome)

print()


print("23 -")
"""

The built-in function len() returns the length of a string:
>>> s = 'supercalifragilisticexpialidocious'
>>> len(s)
34

"""
print(nome)
print("A string %s tem %d carcteres" %(nome, len(nome)))



"""

pack strcmp

if 'foo' in 'foobar':
    print True

if 'foo' in 'barfoo':
    print True

if 'foobar'.startswith('foo'):
    print "it does!"

if 'foobar'.endswith('bar'):
    print "Yes sir :)"

if a[:n] == b[:n]:
    print 'strncmp success!'


"""





