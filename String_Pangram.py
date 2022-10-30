import string

from string import ascii_lowercase as asc_lower

def check(s):
return set(asc_lower) - set(s.lower()) == set([])
str=raw_input("String:")
if(check(str)==True):
print("String is a pangram")
import string
def ispangram(str):
alphabet = "abcdefghijklmnopqrstuvwxyz"
for char in alphabet:
if char not in str.lower():
return False
return True

string = 'Five boxing wizards jumping.'
if(ispangram(string) == True):
print("Yes")
else:
print("String isn't a pangram")
print("No")
