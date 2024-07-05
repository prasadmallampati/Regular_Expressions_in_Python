# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 20:35:34 2024

@author: prasad


"""


import re
# wroking on symbols
# ^ $ * + ? { } [ ] \ | ( )

# information about above symbols
# ^ start of string example ^hello
# end of string $   world$
# * zero of more occurennce of string
# + place holder 
# ? zero or one occurences
# {} exact number of occurences 
# [] character class [abc] matches a or b or c
# \ escape character example \w word character
# | alternataion example  a|b a or b
# () capturing group example (ab)+ matches one or more occurencs  of ab

# 1 start string ^
import re
pattern=r'^hello'
string='hello world'
match=re.search(pattern,string)
print(match)

# 2 ends string  $
import re 
pattern=r'world$'
string='hello world'
match=re.search(pattern, string)
print(match)


# 3 * zero or more occurrences
import re
pattern=r'ab*'
string='ababababab'
match=re.search(pattern, string)
print(match)


# 4  + place holder 
import re
pattern=r'ab+'
string='caabcdef'
print(len(string))
match=re.search(pattern, string) 
print(match)

# 5 ? zero or more occerrences
import re
pattern=r'abc?'
string='abchelloabchelloabc'
match=re.search(pattern, string)
print(match)

# 6 {} extract number of occuerrences
import re
pattern=r'a{3}' # a continous 3 times
string='baaabbb'
match=re.search(pattern, string)
print(match)

# 7 [] is a character class
import re
pattern=r'[abc]'
string='c' # try d none return pattren have in string return else none
match=re.search(pattern, string)
print(match)

# 8 \ escape character 
import re
pattren=r'\w+'
string='coder'
match=re.search(pattern,string)
print(match)

# | checking a or b or c or
import re
pattern=r'a|b|c'
string='hello a b c'
match=re.search(pattern, string)
print(match)

# capturing group example 
import re
pattern=r'(ab)+'
string='abacdefab'
match=re.search(pattern, string)
print(match)


# functions in regular expressions
# search()
# match()
# findall()
# sub()
# compile()

# 1 search()
import re
pattern = r'hello'
string = 'hello world'
match = re.search(pattern, string)
print(match)


# 2 Match()
import re
pattern = r'hello'
string = 'hello world'
match = re.match(pattern, string)
print(match)

# 3 findall(pattern, string)`: 
python
import re
pattern = r'\d+' #decimal
string = 'hello 123 world 456'
matches = re.findall(pattern, string)
print(matches)

# 4 sub()
import re
pattern = r'world'
repl = 'prasad' # replace prasad insted of world
string = 'hello world'
new_string = re.sub(pattern, repl, string)
print(new_string)

# 5 compile()
import re
pattern = r'hello'
regex = re.compile(pattern)
string = 'hello world'
match = regex.search(string)
print(match) 






