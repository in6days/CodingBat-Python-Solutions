#Medium python string problems -- 1 loop.

#Given a string, return a string where for every char in the original, there are two chars.
def double_char(str):
  result = ''
  for char in str:
    result += char*2
  return result

#Return the number of times that the string "hi" appears anywhere in the given string.
def count_hi(str):
  result=0
  for i in range(len(str)-1):
    if str[i:i+2]=='hi':
      result = result+1
  return result

#Return True if the string "cat" and "dog" appear the same number of times in the given string.
def cat_dog(str):
  return str.count('cat')==str.count('dog')

#Return the number of times that the string "code" appears anywhere in the given string, except we'll accept
# any letter for the 'd', so "cope" and "cooe" count.
def count_code(str):
  sum = 0
  for i in range(len(str)-3):
    if str[i]=='c'and str[i+1]=='o'and str[i+3]=='e':
      sum = sum+1
  return sum

#Given two strings, return True if either of the strings appears at the very end of the other string,
# ignoring upper/lower case differences (in other words, the computation should not be "case sensitive").
# Note: s.lower() returns the lowercase version of a string.
def end_other(a, b):
  return a.lower().endswith(b.lower()) or b.lower().endswith(a.lower())

#Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by
# a period (.). So "xxyz" counts but "x.xyz" does not.
def xyz_there(str):
  return str.count('xyz') != str.count('.xyz')

#In6days