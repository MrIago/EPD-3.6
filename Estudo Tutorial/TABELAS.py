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

math.trunc(x)	x truncated to Integral
round(x[, n])	x rounded to n digits, rounding half to even. If n is omitted, it defaults to 0.
math.floor(x)	the greatest Integral <= x
math.ceil(x)	the least Integral >= x

~x	the bits of x inverted

float.is_integer()
Return True if the float instance is finite with integral value, and False otherwise

"""


"""

x in s	True if an item of s is equal to x, else False
x not in s	False if an item of s is equal to x, else True
s + t	the concatenation of s and t
s * n or n * s	equivalent to adding s to itself n times
s[i]	ith item of s, origin 0
s[i:j]	slice of s from i to j
s[i:j:k]	slice of s from i to j with step k
len(s)	length of s	 
min(s)	smallest item of s	 
max(s)	largest item of s	 
s.index(x[, i[, j]])	index of the first occurrence of x in s (at or after index i and before index j)
s.count(x)	total number of occurrences of x in s

"""

"""

Python String Methods
capitalize() - Returns the string with first letter capitalized and the rest lowercased.
casefold() - Returns a lowercase string, generally used for caseless matching. This is more aggressive than the lower() method.
center() - Center the string within the specified width with optional fill character.
count() - Count the non-overlapping occurrence of supplied substring in the string.
encode() - Return the encoded version of the string as a bytes object.
endswith() - Returns ture if the string ends with the supplied substring.
expandtabs() - Return a string where all the tab characters are replaced by the supplied number of spaces.
find() - Return the index of the first occurrence of supplied substring in the string. Return -1 if not found.
format() - Format the given string.
format_map() - Format the given string.
index() - Return the index of the first occurrence of supplied substring in the string. Raise ValueError if not found.
isalnum() - Return true if the string is non-empty and all characters are alphanumeric.
isalpha() - Return true if the string is non-empty and all characters are alphabetic.
isdecimal() - Return true if the string is non-empty and all characters are decimal characters.
isdigit() - Return true if the string is non-empty and all characters are digits.
isidentifier() - Return true if the string is a valid identifier.
islower() - Return true if the string has all lowercased characters and at least one is cased character.
isnumeric() - Return true if the string is non-empty and all characters are numeric.
isprintable() - Return true if the string is empty or all characters are printable.
isspace() - Return true if the string is non-empty and all characters are whitespaces.
istitle() - Return true if the string is non-empty and titlecased.
isupper() - Return true if the string has all uppercased characters and at least one is cased character.
join() - Concatenate strings in the provided iterable with separator between them being the string providing this method.
ljust() - Left justify the string in the provided width with optional fill characters.
lower() - Return a copy of all lowercased string.
lstrip() - Return a string with provided leading characters removed.
maketrans() - Return a translation table.
partition() - Partition the string at first occurrence of substring (separator) and return a 3-tuple with part before separator, the separator and part after separator.
replace() - Replace all old substrings with new substrings.
rfind() - Return the index of the last occurrence of supplied substring in the string. Return -1 if not found.
rindex() - Return the index of the last occurrence of supplied substring in the string. Raise ValueError if not found.
rjust() - Right justify the string in the provided width with optional fill characters.
rpartition() - Partition the string at last occurrence of substring (separator) and return a 3-tuple with part before separator, the separator and part after separator.
rsplit() - Return a list of words delimited by the provided subtring. If maximum number of split is specified, it is done from the right.
rstrip() - Return a string with provided trailing characters removed.
split() - Return a list of words delimited by the provided subtring. If maximum number of split is specified, it is done from the left.
splitlines() - Return a list of lines in the string.
startswith() - Return true if the string starts with the provided substring.
strip() - Return a string with provided leading and trailing characters removed.
swapcase() - Return a string with lowercase characters converted to uppercase and vice versa.
title() - Return a title (first character of each word capitalized, others lowercased) cased string.
translate() - Return a copy of string that has been mapped according to the provided map.
upper() - Return a copy of all uppercased string.
zfill() - Return a numeric string left filled with zeros in the provided width.

sort alphabetically the words form a string provided by the user
breakdown the string into a list of words
words = my_str.split()

sort the list
words.sort()

"""

"""

enumerate() -> tuplas

>>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
>>> list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
>>> list(enumerate(seasons, start=1))
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

"""

