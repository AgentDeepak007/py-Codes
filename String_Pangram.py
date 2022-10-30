from string import ascii_lowercase as asc_lower
def check(s):
    return set(asc_lower) - set(s.lower()) == set([])
str=raw_input("String:")
if(check(str)==True):
      print("String is a pangram")
else:
      print("String isn't a pangram")
