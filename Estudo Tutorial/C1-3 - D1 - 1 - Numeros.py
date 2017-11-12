# -*- coding: UTF-8 -*-
# primeira linha

print()

print("1 -")
# imprimir na tela
print(7)

print()

print("2 -")
# comentário
#print(77)
print("# não é um comentario pq esta dentro das aspas")

# fecha o shell
# quit()

print()

print("3 -")
#char para ascii
c = ord('a')
#ascii para char
n = chr(97)
print(c,n) # imprime 2 variaveis com espaço

print()

print("4 -")
print(17 / 3) # classic division returns a float
print(17 // 3) # floor division discards the fractional part
print(17 % 3) # the % operator returns the remainder of the division
print(5 * 3 + 2) # result * divisor + remainder

print()

print("5 -")
# With Python, it is possible to use the ** operator to calculate powers
print(5 ** 2) # 5 squared
print(2 ** 7) # 2 to the power of 7
"""
Since ** has higher precedence than -, -3**2 will be interpreted as -(3**2) and thus result in -9. To avoid this and get 9,
you can use (-3)**2.

"""

print()

print("6 -")
# The equal sign (=) is used to assign a value to a variable
nome = 'Iago'
print(nome) # imprime a variavel

print()

print("7 -")
# operators with mixed type operands convert the integer operand to
# floating point:
print(2*3.5)


print()

print("8 -")
"""

In interactive mode, the last printed expression is assigned to the variable _.
This means that when you are using Python as a desk calculator, it is somewhat
easier to continue calculations, for example:

>>> from math import *
>>> pi
3.141592653589793
>>> _*2
6.283185307179586
>>> round(_,2)
6.28


In addition to int and float, Python supports other types of numbers,
such as Decimal and Fraction. Python also has built-in support for
complex numbers, and uses the j or J suffix to indicate the imaginary part
(e.g. 3+5j).

"""

print(((3)+(-5j))*((3)-(-5j)))


print()


"""

x + y	sum of x and y	 	 
x - y	difference of x and y	 	 
x * y	product of x and y	 	 
x / y	quotient of x and y	 	 
x // y	floored quotient of x and y 
x % y	remainder of x / y 
-x	x negated	
+x	x unchanged	 	 
abs(x)	absolute value or magnitude of x
int(x)	x converted to integer
float(x)	x converted to floating point
complex(re, im)	a complex number with real part re, imaginary part im. im defaults to zero.
c.conjugate()	conjugate of the complex number c	 	 
divmod(x, y)	the pair (x // y, x % y)
pow(x, y)	x to the power y
x ** y	x to the power y

~x	the bits of x inverted

float.is_integer()
Return True if the float instance is finite with integral value, and False otherwise

"""

"""
math

math.trunc(x)	x truncated to Integral
round(x[, n])	x rounded to n digits, rounding half to even. If n is omitted, it defaults to 0.
math.floor(x)	the greatest Integral <= x
math.ceil(x)	the least Integral >= x

math.gcd(a, b)
Return the greatest common divisor of the integers a and b.

math.isfinite(x)¶
Return True if x is neither an infinity nor a NaN, and False otherwise. (Note that 0.0 is considered finite.)

math.isinf(x)
Return True if x is a positive or negative infinity, and False otherwise.

math.trunc(x)
Return the Real value x truncated to an Integral

"""

